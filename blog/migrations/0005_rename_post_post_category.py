# Generated by Django 5.0.2 on 2024-02-29 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='category',
        ),
    ]
