from django.contrib import admin
from .models import Book  # Import the Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the admin list view
    search_fields = ('title', 'author')  # Enable search functionality for these fields
    list_filter = ('title', 'author', 'publication_year')
admin.site.register(Book, BookAdmin)  # Register the Book model with the admin site
