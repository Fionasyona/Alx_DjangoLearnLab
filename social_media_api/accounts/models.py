from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Optional bio field
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)  # Optional profile picture field
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',       
        blank=True
    )  # Many-to-many relationship for followers    

    def __str__(self):
        return self.username

