from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .views import  PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView, CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = "blog"

urlpatterns = [
    # Auth

    path("login/",  auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(
        template_name="registration/logout.html"
    ), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View one post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Edit post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_add'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

]
