# Generated by Django 3.2.21 on 2023-09-29 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0008_remove_review_post_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='review_post',
            name='status',
        ),
    ]