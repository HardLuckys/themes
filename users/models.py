from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from .create_link import slug_gen

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, null=True, max_length=15, verbose_name="username")
    email = models.EmailField(unique=True,  null=True, verbose_name="емайл")
    about_me = models.TextField(max_length=350, blank=True, verbose_name="обо мне")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="создан в")
    avatar = models.ImageField(upload_to='media', default='media/icon-user-default.png', verbose_name="автарка")
    user_members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='Subs', verbose_name="подписчики")
    slug = models.SlugField(unique=True, null=True, verbose_name="ID (айди)")
    is_coded = models.BooleanField(default=False, verbose_name="Введен ли код")

    def get_absolute_url(self):
        return reverse('avataruser_detail', kwargs={'slug':self.slug})

def slug_save(sender, instance, *ags, **kwargs):
    if not instance.slug:
        instance.slug = slug_gen(instance, instance.slug)

pre_save.connect(slug_save, sender=CustomUser)

class MyUserModel(models.Model):
    url = models.CharField(max_length=15)
    code_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name="пользователь")
    code_create_time = models.CharField(null=True, blank=True, max_length=35, verbose_name="Время создания")
