# Generated by Django 2.2.2 on 2020-03-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200330_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusermodel',
            name='code_create_time',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Время создания'),
        ),
    ]
