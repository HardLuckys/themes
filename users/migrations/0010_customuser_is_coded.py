# Generated by Django 2.2.2 on 2020-03-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200329_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_coded',
            field=models.BooleanField(default=False, verbose_name='Введен ли код'),
        ),
    ]