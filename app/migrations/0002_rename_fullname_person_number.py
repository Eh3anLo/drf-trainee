# Generated by Django 5.0.7 on 2024-07-31 12:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fullname',
            new_name='number',
        ),
    ]
