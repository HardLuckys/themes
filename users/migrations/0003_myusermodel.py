# Generated by Django 2.2.2 on 2020-03-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200128_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.IntegerField()),
            ],
        ),
    ]