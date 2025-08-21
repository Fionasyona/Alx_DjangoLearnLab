from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")
router.register(r"comments", CommentViewSet, basename="comment")

feed_view = PostViewSet.as_view({"get": "feed"})

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", feed_view, name="post-feed"),  # Custom feed endpoint
    # Additional endpoints can be added here
]
