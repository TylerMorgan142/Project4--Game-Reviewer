# Generated by Django 3.2.21 on 2023-09-22 23:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_auto_20230921_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review_post',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='game',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
