from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from .create_link import slug_gen

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=15, verbose_name="username")
    email = models.EmailField(unique=True,  null=True, verbose_name="емайл")
    about_me = models.TextField(max_length=350, blank=True, verbose_name="обо мне")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="создан в")
    avatar = models.ImageField(upload_to='media', default='media/icon-user-default.png', verbose_name="автарка")
    user_members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='Subs', verbose_name="подписчики")
    slug = models.SlugField(unique=True, null=True, verbose_name="ID (айди)")

    def get_absolute_url(self):
        return reverse('avataruser_detail', kwargs={'slug':self.slug})

def slug_save(sender, instance, *ags, **kwargs):
    if not instance.slug:
        instance.slug = slug_gen(instance, instance.slug)

pre_save.connect(slug_save, sender=CustomUser)
