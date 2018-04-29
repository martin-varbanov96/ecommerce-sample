from django.shortcuts import render
from django.views import generic
from .models import Category, CategoryTree
from product.models import Product


def load_categories(request):
    """links to a the list of categories"""
    final_list = list()

    def traverse_it(it):
        """traverse the input query and extract a list of pair of names and keys of categories"""
        if (isinstance(it, list)):
            for item in it:
                traverse_it(item)
        elif (isinstance(it, dict)):
            final_list.append({"name": it["data"]["name"], "id": it["id"]})
            for key in it:
                print("*"*50)
                print(it[key])
                print("*"*50)
                print(key)
                print("*"*50)
            if ("children" in it):
                print("adsa")
                for item in it["children"]:
                    traverse_it(item)

    frontned_template = "categories.html"
    items = dict()
    items = Category.objects.all()
    categories = CategoryTree.dump_bulk()
    traverse_it(categories)
    return render(request, frontned_template,
                  {"items": items, "categories": final_list})


def category_details(request, category_id):
    """links to a template of products related to current category"""
    frontned_template = "categories_details.html"
    products = Product.objects.filter(category_key__pk=category_id)
    # print("*"*80)
    # for product in products:
    #     print(product)
    # print("*"*80)
    output_dict = {"products": products, "category_id": category_id}
    return render(request, frontned_template, output_dict)
