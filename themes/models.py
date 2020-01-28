from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from datetime import datetime
from tinymce import HTMLField

class Categories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name="автор")
    created_at = models.DateTimeField(default=datetime.now, null=True, verbose_name="создан в")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="обновлен в")
    image = models.ImageField(upload_to='media', blank=True, verbose_name="картинка")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('themes:category', kwargs={'categories_pk':self.pk})

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ['-created_at']

class Exercises(models.Model):
    categories = models.ForeignKey(Categories, blank=True, related_name='items', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, verbose_name="автор")
    actions = models.BooleanField(default=False, verbose_name="Действия других пользователей")
    created_at = models.DateTimeField(default=datetime.now, null=True, verbose_name="создан в")
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="обновлен в")
    image = models.ImageField(upload_to='media', blank=True, verbose_name="картинка")
    body = HTMLField(null=True, verbose_name="Основной текст")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('themes:exercise', kwargs={'categories_pk':self.pk, 'exercises_pk':self.pk})

    class Meta:
        verbose_name = "Элемент темы"
        verbose_name_plural = "Элементы темы"
        ordering = ['-created_at']
