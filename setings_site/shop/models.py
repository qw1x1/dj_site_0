from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Заголовок', help_text='Наименование товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") # unique=True - не будет повторок
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name= 'Стоимость') 
    description = models.TextField(blank=True, verbose_name= 'Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name= 'Фото', null=True)
    colum = models. IntegerField(verbose_name= 'Количество') 
    available = models.BooleanField(default=True, verbose_name= 'Наличие')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null= True, verbose_name= 'Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True, verbose_name= 'Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории' 
        verbose_name_plural = 'Категории'
        ordering = ['id']

