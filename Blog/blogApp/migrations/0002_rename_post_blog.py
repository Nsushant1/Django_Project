# Generated by Django 5.1.5 on 2025-01-27 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog',
        ),
    ]
