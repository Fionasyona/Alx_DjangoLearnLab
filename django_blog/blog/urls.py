from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView, PostDeleteView,
    PostCreateView, PostUpdateView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    PostByTagListView, register, profile, search_posts
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
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),

    # Post URLs
    path('', PostListView.as_view(), name='post-list'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search
    path('search/', search_posts, name='search-posts'),
]
