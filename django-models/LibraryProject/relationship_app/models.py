from django.db import models

# Author Model: Each author can write many books
class Author(models.Model):
    name = models.CharField(max_length=100)



# Book Model: A book is written by one author
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")



# Library Model: A library contains many books
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")



# Librarian Model: Each library has exactly one librarian
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

