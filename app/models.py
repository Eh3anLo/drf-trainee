from django.db import models

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
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        return self.person_number




