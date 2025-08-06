from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name="Jane Austen")

        # Create a book
        self.book = Book.objects.create(
            title="Pride and Prejudice",
            publication_year=1813,
            author=self.author
        )

        self.book_url = reverse('book-detail', args=[self.book.id])
        self.list_url = reverse('book-list')

    def test_create_book(self):
        data = {
            "title": "Emma",
            "publication_year": 1815,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Emma')

    def test_get_all_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        updated_data = {
            "title": "Sense and Sensibility",
            "publication_year": 1811,
            "author": self.author.id
        }
        response = self.client.put(reverse('book-update', args=[self.book.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Sense and Sensibility")

    def test_delete_book(self):
        response = self.client.delete(reverse('book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_permission_required_for_post(self):
        self.client.logout()
        data = {
            "title": "Unauthorized",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
