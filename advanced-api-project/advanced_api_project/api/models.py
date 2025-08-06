from django.db import models
from datetime import datetime

# Author model to represent book authors.
class Author(models.Model):
    name = models.CharField(max_length=255)  # Stores the name of the author.

    def __str__(self):
        return self.name

# Book model representing books written by authors.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book.
    publication_year = models.PositiveIntegerField()  # Year book was published.
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # Foreign key creates a one-to-many relationship (one author to many books).

    def __str__(self):
        return self.title
