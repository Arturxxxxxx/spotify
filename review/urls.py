# urls.py
from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView, CommentListCreateAPIView, LikeCreateAPIView, LikeDestroyAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/likes/', LikeCreateAPIView.as_view(), name='like-create'),
    path('posts/<int:post_id>/likes/remove/', LikeDestroyAPIView.as_view(), name='like-destroy'),
]
