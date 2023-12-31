from django.contrib import admin
from .models import Game, Review_post, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Game)


@admin.register(Review_post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug','created_on')
    search_fields = ['title', 'content', 'game']
    list_filter = ('created_on', 'game')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on',)
    list_filter = ('created_on', )
    search_fields = ('name', 'email', 'body')
