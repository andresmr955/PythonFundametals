# Generated by Django 5.2.1 on 2025-05-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0003_remove_author_slug_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug_author',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
