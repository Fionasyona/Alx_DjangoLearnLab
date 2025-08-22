from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")
# Custom view for post feed

feed_view = PostViewSet.as_view({"get": "feed"})

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", feed_view, name="post-feed"),  # Custom feed endpoint
    path("posts/<int:post_id>/comments/", CommentViewSet.as_view({"get": "list", "post": "create"}), name="post-comments"),
    path("posts/<int:post_id>/comments/<int:comment_id>/", CommentViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="post-comment-detail"),
    path("posts/<int:pk>/like/", PostViewSet.as_view({"post": "like"}), name="post-like"),
    path("posts/<int:pk>/unlike/", PostViewSet.as_view({"post": "unlike"}), name="post-unlike"),   
]
