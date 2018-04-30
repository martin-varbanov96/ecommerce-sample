from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('User', null=True, blank=True)
    products = models.ManyToManyField('products.Product', blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
