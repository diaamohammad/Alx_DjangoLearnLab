from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    bio = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_picture',blank=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='following',blank=True)

    def __str__(self):
        return self.username
