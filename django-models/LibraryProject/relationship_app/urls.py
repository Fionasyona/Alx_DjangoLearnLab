from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, list_books_view, LibraryDetailView

urlpatterns = [
    path('books/', list_books_view, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
]
