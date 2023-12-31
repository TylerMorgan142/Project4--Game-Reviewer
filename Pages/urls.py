from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name="home"),
    path('create_review/', views.create_review, name='create_review'),
    path('delete/<slug:slug>/', views.delete_review, name='delete_review'),
    path('edit/<slug:slug>/', views.edit_review, name='edit_review'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
]
