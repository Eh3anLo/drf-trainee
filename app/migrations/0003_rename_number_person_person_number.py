# Generated by Django 5.0.7 on 2024-07-31 12:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0002_rename_fullname_person_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='number',
            new_name='person_number',
        ),
    ]
