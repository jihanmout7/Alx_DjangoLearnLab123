from rest_framework import generics
from .models import Book
from .serializers import BookSerializer  # Make sure the path is correct

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer