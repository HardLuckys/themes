# Generated by Django 2.2.2 on 2020-03-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_myusermodel_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusermodel',
            name='url',
            field=models.CharField(max_length=15),
        ),
    ]