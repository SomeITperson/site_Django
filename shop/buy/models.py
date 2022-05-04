from django.db import models
from django.urls import reverse

class Goods(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('item', kwargs={'item_slug' : self.slug})

    class Meta():
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    #формирование ссылки для обращения в виде slug
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug' : self.slug})

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']