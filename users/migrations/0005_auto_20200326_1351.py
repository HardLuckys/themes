# Generated by Django 2.2.2 on 2020-03-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200326_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=15, null=True, unique=True, verbose_name='username'),
        ),
    ]
