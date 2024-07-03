from django.contrib import admin
from goods.models import Categories
from goods.models import Products

# Register your models here.
# admin.site.register(Categories)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
