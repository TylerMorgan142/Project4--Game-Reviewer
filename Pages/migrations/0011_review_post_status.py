# Generated by Django 3.2.21 on 2023-09-29 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0010_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
