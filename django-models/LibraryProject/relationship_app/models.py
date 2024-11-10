from django.db import models

# Author Model: Each author can write many books
class AuthorModel(models.Model):
    name = models.CharField(max_length=100)



# Book Model: A book is written by one author
class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name="books")



# Library Model: A library contains many books
class LibraryModel(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(BookModel, related_name="libraries")



# Librarian Model: Each library has exactly one librarian
class LibrarianModel(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(LibraryModel, on_delete=models.CASCADE, related_name="librarian")

