from relationship_app import Author, Book 
from relationship_app import Library, Book 
from relationship_app import Library, Librarian


author = Author.objects.filter(name="J.K. Rowling").first()

library = Library.objects.filter(name="Central Library").first()

library = Library.objects.filter(name="Central Library").first()
