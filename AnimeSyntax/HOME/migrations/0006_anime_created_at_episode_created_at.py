# Generated by Django 5.1.4 on 2025-01-01 19:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0005_rename_poster_anime_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='episode',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
