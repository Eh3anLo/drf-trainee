from django.db import models

# Create your models here.
class Image(models.Model):
    CHOICES = {
        1 : "پردازش شده",
        0 : "پردازش نشده",
    }
    origin_image = models.ImageField()
    processed_image = models.ImageField(blank=True, null=True)
    message = models.CharField(choices=CHOICES, max_length=30, default=CHOICES[0], blank=True, null=True)

