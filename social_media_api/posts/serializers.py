from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from .models import User
from rest_framework.authtoken.models import Token
from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "author", "author_username", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "author_username", "created_at", "updated_at"]

    def create(self, validated_data):
        # Set author to the currently authenticated user
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")
    post_title = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = ["id", "post", "post_title", "author", "author_username", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "author_username", "post_title", "created_at", "updated_at"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)