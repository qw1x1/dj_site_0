# Generated by Django 4.1.4 on 2022-12-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименование товара', max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('colum', models.IntegerField(verbose_name='Количество')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
    ]
