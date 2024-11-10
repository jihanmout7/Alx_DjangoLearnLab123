from django.shortcuts import redirect, render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

# Admin view accessible only by users with 'Admin' role
class AdminView(UserPassesTestMixin, TemplateView):
    template_name = 'admin_view.html'

    def test_func(self):
        return self.request.user.profile.role == 'Admin'

# Librarian view accessible only by users with 'Librarian' role
class LibrarianView(UserPassesTestMixin, TemplateView):
    template_name = 'librarian_view.html'

    def test_func(self):
        return self.request.user.profile.role == 'Librarian'

# Member view accessible only by users with 'Member' role
class MemberView(UserPassesTestMixin, TemplateView):
    template_name = 'member_view.html'

    def test_func(self):
        return self.request.user.profile.role == 'Member'

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for a library's details
class LibraryDetailView(DetailView):
    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        return render(request, 'relationship_app/library_detail.html', {'library': library})

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('relationship_app/list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
