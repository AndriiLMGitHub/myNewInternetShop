# Generated by Django 3.0.7 on 2021-01-10 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogpost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
    ]
