from django.db import models

from treebeard.mp_tree import MP_Node


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, default="")
    subcategory_key = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)


class CategoryTree(MP_Node):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, default="")
    node_order_by = ['name']

    def __unicode__(self):
        return 'Category: %s' % self.name
