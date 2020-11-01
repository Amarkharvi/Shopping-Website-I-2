from django.contrib import admin
from django.db import models
from .models import Product,Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','available','created','updated']
    list_filter=['available','created','updated']
    search_fields=['name','category__name']
    list_editable=['available','price']
    prepopulated_fields={'slug':('name',)}    