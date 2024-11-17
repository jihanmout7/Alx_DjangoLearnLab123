from django.contrib import admin
from .models import Book
from .models import CustomUser

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
    





# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'profile_picture')
    list_filter = ('date_of_birth',)
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
