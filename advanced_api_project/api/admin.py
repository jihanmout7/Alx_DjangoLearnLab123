from django.contrib import admin
from .models import Author, Book

# Register the models to make them visible in the admin interface
admin.site.register(Author)
admin.site.register(Book)
