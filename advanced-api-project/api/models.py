from django.db import models

# Create your models here.
# Author model represents a book author
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

# Book model represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=255)              # Book title
    publication_year = models.PositiveIntegerField()      # Year published
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # Link to Author model, one-to-many

    def __str__(self):
        return self.title