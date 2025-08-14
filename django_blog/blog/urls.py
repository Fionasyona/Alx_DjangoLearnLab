from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView, PostDeleteView,
    PostCreateView, PostUpdateView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

app_name = "blog"

urlpatterns = [
    # Authentication
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="registration/logout.html"
    ), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Post URLs
    path('', PostListView.as_view(), name='post-list'), 
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'), # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View one post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post

    # Comment URLs (match checker requirements exactly)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
