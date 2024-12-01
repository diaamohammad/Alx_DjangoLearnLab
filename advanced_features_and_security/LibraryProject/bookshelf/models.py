from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.contrib.auth.models import Group, Permission


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year =models.IntegerField()
    
    def __str__(self):
        return self.title


    
    
class CustomUserManager(BaseUserManager):
    class Meta:
        permissions = [("can_view" , "view_book"),
                        ("can_create" , "create_book"),
                        ("can_edit" , "edit_book"),
                        ("can_delete" , "delete_book"),]
    def create_user(self, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, date_of_birth=None, profile_photo=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'date_of_birth', 'profile_photo'
    
# Create groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')


# Assign permissions to groups
can_edit_permission = Permission.objects.get(codename='can_edit')
can_create_permission = Permission.objects.get(codename='can_create')
can_view_permission = Permission.objects.get(codename='can_view')
can_delete_permission = Permission.objects.get(codename='can_delete')

editors_group.permissions.add(can_edit_permission, can_create_permission)
viewers_group.permissions.add(can_view_permission)
admins_group.permissions.add(can_edit_permission, can_create_permission, can_view_permission, can_delete_permission)  