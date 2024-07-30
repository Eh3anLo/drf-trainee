from django.db import models

# Create your models here.
class Image(models.Model):
    origin_image = models.ImageField(blank=True, null=True)
    processed_image = models.ImageField(blank=True, null=True)

