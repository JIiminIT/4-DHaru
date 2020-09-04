from django.shortcuts import render

from shop.models import Category, Product


def products_in_category(products):
    category = Category.objects.alt()
    products = Product.objects.alt()

    return render(request, 'shop/list.html', {'Categories': categories, 'products': products})
