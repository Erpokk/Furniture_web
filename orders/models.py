from itertools import product
from tabnanny import verbose
from xml.parsers.expat import model
from django.db import models

from goods.models import Products
from users.models import User


# Create your models here.
class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_qty(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True,
        verbose_name="User",
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Date of order creation"
    )
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    requires_delivery = models.BooleanField(
        default=False, verbose_name="Does delivery requires"
    )
    delivery_address = models.TextField(
        null=True, blank=True, verbose_name="Delivery address"
    )
    payment_on_get = models.BooleanField(default=False, verbose_name="Payment on place")
    is_paid = models.BooleanField(default=False, verbose_name="Paid")
    status = models.CharField(
        max_length=50, default="In process", verbose_name="Order status"
    )

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.pk} | Client {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(
        to=Products, on_delete=models.SET_DEFAULT, default=None, null=True
    )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order_item"
        verbose_name = "Sold item"
        verbose_name_plural = "Sold items"

    objects = OrderItemQueryset.as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Item {self.name} | Order {self.order.pk}"
