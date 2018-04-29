from django.db import models


class Product(models.Model):
    """object that represent a product"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, default="")
    price = models.IntegerField()
    # TODO: set a default media folder
    picture = models.ImageField(blank=True)
    category_key = models.ForeignKey(
        'categories.CategoryTree', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
