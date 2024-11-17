from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser ,BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Permission


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()



    date_of_birth= models.DateField()
    profile_photo=models.ImageField()
    
    def __str__(self):
        return self.username
    
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)



    

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)
    
    

from django.contrib.auth.models import Permission, User, Group

# Define permissions in your model's Meta class
class MyModel(models.Model):
    # Your model fields here

    class Meta:
        permissions = [
            ("can_view", "Can view the object"),
            ("can_create", "Can create the object"),
            ("can_edit", "Can edit the object"),
            ("can_delete", "Can delete the object"),
        ]

# Get the permission
permission = Permission.objects.get(codename="can_view")

# Assign permission to individual users
editor = User.objects.get(username="editor_username")
viewer = User.objects.get(username="viewer_username")
admin = User.objects.get(username="admin_username")

editor.user_permissions.add(permission)
viewer.user_permissions.add(permission)
admin.user_permissions.add(permission)

# Assign permission to a group
group = Group.objects.get(name="Editors")
group.permissions.add(permission)
