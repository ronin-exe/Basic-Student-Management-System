# Generated by Django 5.1.3 on 2024-12-05 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fiels_of_study',
            new_name='field_of_study',
        ),
    ]
