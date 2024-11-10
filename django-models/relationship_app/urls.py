from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('admin/', views.AdminView.as_view(), name='admin_view'),
    path('librarian/', views.LibrarianView.as_view(), name='librarian_view'),
    path('member/', views.MemberView.as_view(), name='member_view'),
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
]
