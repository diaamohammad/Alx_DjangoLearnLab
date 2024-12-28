from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_picture',blank=True)
    following = models.ManyToManyField('self',symmetrical=False,related_name='followers',blank=True)

    def __str__(self):
        return self.username
