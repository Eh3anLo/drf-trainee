from django.db import models

# Create your models here.
class Images(models.Model):
    origin_image = models.ImageField()
    processed_image = models.ImageField(blank=True, null=True)

