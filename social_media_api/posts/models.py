from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
User = settings.AUTH_USER_MODEL 

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.author} at {self.created_at}"

class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ['-created_at']

        def __str__(self):
            return f"Comment by {self.author} on {self.post}"   

class Like(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Ensure a user can like a post only once

    def __str__(self):
        return f"{self.user} likes {self.post}"         
