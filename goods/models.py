from tabnanny import verbose
from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        # Sorting type for Paginator
        ordering = ("id",)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True)
    # upload_to shows the way where to save img f.e. in foldeer media>goods_images
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Discount %"
    )
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} Qty - {self.quantity}"

    # Name in admin panel and db_name
    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        return self.price
