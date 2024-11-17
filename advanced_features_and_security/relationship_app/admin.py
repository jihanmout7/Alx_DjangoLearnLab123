from django.contrib import admin
from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('date_of_birth', 'profile_picture')
    list_filter = ('date_of_birth',)
    #search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)