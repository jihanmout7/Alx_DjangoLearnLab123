from django.urls import path 
from . models import Book
from . views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]