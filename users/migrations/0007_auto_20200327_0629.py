# Generated by Django 2.2.2 on 2020-03-27 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200326_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=15, null=True, unique=True, verbose_name='username'),
        ),
    ]
