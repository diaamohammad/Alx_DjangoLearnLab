from django.db import models
from accounts.models import CustomUser
from posts.models import Post,Comment
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Notification(models.Model):

    recipient = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    verb = models.TextField()
    target_tybe = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_tybe','target_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'notification for {self.recipient.username} at {self.timestamp}')
