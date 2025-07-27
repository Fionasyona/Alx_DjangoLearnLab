from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'),
    path('search/', views.search_books, name='search_books'),

    # Secure form view using ExampleForm
    path('example-form/', views.example_form_view, name='example_form'),
]
