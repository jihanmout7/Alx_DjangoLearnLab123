from rest_framework import generics,viewsets
from .models import Book
from .serializers import BookSerializer # Make sure the path is correct
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication 


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only authenticated admin users
    authentication_classes = [TokenAuthentication]  # Use TokenAuthentication for token-based auth