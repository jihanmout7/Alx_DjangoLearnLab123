from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)  # Specify max_length
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Specify max_length
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)  # Specify max_length
    books = models.ManyToManyField(Book)  # Remove the on_delete here

    def __str__(self):
        return self.name

class Librarian(models.Model):   
    name = models.CharField(max_length=100)  # Specify max_length
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
