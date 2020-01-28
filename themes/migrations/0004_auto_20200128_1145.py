# Generated by Django 2.2.2 on 2020-01-28 08:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('themes', '0003_auto_20200128_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='lol',
        ),
        migrations.AddField(
            model_name='exercises',
            name='body',
            field=tinymce.models.HTMLField(null=True, verbose_name='Основной текст'),
        ),
    ]
