from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Book

# Decorator ensures user has 'can_edit' permission before accessing the view
@permission_required('bookshelf.can_edit', raise_exception=True)
def my_view(request):
    if request.user.has_perm('bookshelf.can_edit'):
        # Logic for users with 'can_edit' permission
        return render(request, 'edit_page.html')
    
    # You can also check for other permissions inside the view
    elif request.user.has_perm('bookshelf.can_create'):
        # Logic for users with 'can_create' permission
        return render(request, 'create_page.html')
    
    elif request.user.has_perm('bookshelf.can_delete'):
        # Logic for users with 'can_delete' permission
        return render(request, 'delete_page.html')
    
    else:
        # If the user does not have any of the permissions
        return HttpResponseForbidden("You do not have permission to perform this action")


def list_books(request):
    query = request.GET.get('genre', '')
    books = Book.objects.exclude(genre=query)  # Safely exclude books of a particular genre
    return render(request, 'book_list.html', {'books': books})
