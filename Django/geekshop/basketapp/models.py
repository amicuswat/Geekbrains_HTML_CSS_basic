from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def product_cost(self):
        """Returns cost of all products of this type."""

        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        """Returns total quantity for this user."""
        _items = Basket.objects.filter(user=self.user)
        # _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        _total_quantity = sum([x.quantity for x in _items])

        return _total_quantity

    @property
    def total_cost(self):
        """Returns total cost for this user"""

        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum([x.product_cost for x in _items])

        return _total_cost
