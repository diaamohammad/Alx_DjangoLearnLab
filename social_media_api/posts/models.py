from django.db import models

from accounts.models import UserModel


class Post(models.Model):
    author = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    content = models.TextField()
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='commments',on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
