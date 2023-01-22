from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'available', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name", )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)