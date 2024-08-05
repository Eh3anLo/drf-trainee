from django.db import models
from django.contrib.auth.hashers import make_password


class Field(models.Model):
    FIELDS = {
        'backend': 'backend',
        'frontend': 'frontend',
        'ceo': 'ceo',
        'ai': 'ai'
    }
    name = models.CharField(max_length=10, choices=FIELDS)

    def __str__(self):
        return f'{self.name}'

class Person(models.Model):
    person_number = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128, blank=True)
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Person, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.person_number
    

class FaildLogin(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person_number} unsuccessfull login on {self.attempt_time}'
    