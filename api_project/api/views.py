from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    permission_classes = [IsAuthenticated]  
    permission_classes = [IsAdminUser]

    # BookViewSet is secured with TokenAuthentication
# Only authenticated users can access it
# Permissions can be adjusted using DRF permission classes

