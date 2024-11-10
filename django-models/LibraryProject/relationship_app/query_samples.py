# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Retrieve all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using reverse relation (books)
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")

# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # ManyToMany relation
        for book in books:
            print(f"Book Title: {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

# Query 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOne relation
        print(f"Librarian for {library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library: {library_name}")


# Run sample queries
if __name__ == "__main__":
    print("\n--- Books by Author ---")
    books_by_author("J.K. Rowling")
    
    print("\n--- Books in Library ---")
    books_in_library("Central Library")
    
    print("\n--- Librarian for Library ---")
    librarian_for_library("Central Library")
