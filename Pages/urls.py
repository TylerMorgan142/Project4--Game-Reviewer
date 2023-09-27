from . import views
from django.urls import path

urlpatterns = [
    path('', views.reviewlist, name="home"),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
