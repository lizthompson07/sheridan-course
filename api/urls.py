# api/urls.py

from django.urls import path
from . import views

# Namespace for the API app
app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/like/', views.comment_likes, name='comment-like'),
    path('comments/<int:pk>/dislike/', views.comment_dislikes, name='comment-dislike'),
]
