from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import DefaultResultsSetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = DefaultResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "content"]  # search by title/content
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        """Ensure logged-in user is the author of the post"""
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get"], url_path="comments")
    def list_comments(self, request, pk=None):
        """List comments belonging to this post"""
        post = self.get_object()
        qs = post.comments.select_related("author").all()

        page = self.paginate_queryset(qs)
        if page is not None:  # ✅ check pagination
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(qs, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("post", "author").all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = DefaultResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["content", "post__title", "author__username"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        """Ensure logged-in user is the author of the comment"""
        serializer.save(author=self.request.user)
