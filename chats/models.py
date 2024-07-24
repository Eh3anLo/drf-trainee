from django.db import models

# Create your models here.
class Chat(models.Model):
    message_id = models.IntegerField(max_length=20)
    message = models.TextField()


