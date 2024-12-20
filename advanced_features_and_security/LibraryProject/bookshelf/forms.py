# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'description']
        widgets = {
            'publication_date': forms.SelectDateWidget(years=range(1900, 2025)),
        }
