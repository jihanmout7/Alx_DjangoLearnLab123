from .models import Author, Book
from rest_framework import serializers
from datetime import date

# BookSerializer to serialize Book instances
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate(self, data):
        # Validate if the publication year is in the future
        if data['publication_year'] > date.today():
            raise serializers.ValidationError("Publication year should not be in the future.")
        return data

# AuthorSerializer to serialize Author instances and include related books
class AuthorSerializer(serializers.ModelSerializer):
    # Serialize related books using BookSerializer
    books = BookSerializer(many=True, read_only=True, source='book_set')
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
