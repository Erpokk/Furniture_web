from django.contrib import admin
from goods.models import Categories
from goods.models import Products

# Register your models here.
# admin.site.register(Categories)


# Control of slug autofilling
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # Create columns for product in admin panel
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount"]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]

    fields = [
        "name",
        "category",
        "slug",
        "description",
        ("price", "discount"),
        "quantity",
    ]
