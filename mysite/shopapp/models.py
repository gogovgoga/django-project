from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ['name', 'price']
        # db_table = "tech_products"
        # verbose_name_plural = "products"

    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"


class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promo_code = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
