# Generated by Django 3.0.7 on 2020-10-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200810_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='Не нравится'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
    ]
