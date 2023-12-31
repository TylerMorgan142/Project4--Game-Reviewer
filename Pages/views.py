from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Review_post
from .forms import CommentForm, ReviewForm


class ReviewList(ListView):
    model = Review_post
    queryset = Review_post.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'review_list'
    paginate_by = 6


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review_post.objects
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Review_post.objects
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = review
            comment.save()
            messages.add_message(request, messages.INFO, 'Comment left successfully')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class ReviewLike(View):

    def post(self, request, slug):
        review = get_object_or_404(Review_post, slug=slug)

        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_detail', args=[slug]))


def create_review(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.add_message(request, messages.INFO, 'Your review was uploaded successfully')
            return redirect('home')
    else:
        review_form = ReviewForm()
    return render(
        request,
        "create_review.html",
        {
            'form': review_form,
        },
    )


def delete_review(request, slug):
    review = get_object_or_404(Review_post, slug=slug)

    if request.user == review.author:
        review.delete()
        messages.add_message(request, messages.INFO, 'Your review was deleted successfully')
        return redirect('home')


def edit_review(request, slug):
    review = get_object_or_404(Review_post, slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, 'Your review was updated successfully')
            return redirect('review_detail', slug=slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})
