from django.contrib import admin

from .models import Category, CategoryTree

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


admin.site.register(Category)


class MyAdmin(TreeAdmin):
    form = movenodeform_factory(CategoryTree)


admin.site.register(CategoryTree, MyAdmin)
