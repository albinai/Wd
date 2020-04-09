from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import Category, Product

def products_all(request):
    products = Product.objects.all()
    products_json = [product.to_json for product in products]
    return JsonResponse(products_json,safe = False)

def product_get(request):
    try:
        product = Product.objects.get(id = product.id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error' : str(e)})
    return JsonResponse(product.to_json())

def categories_all(request):
    categories = Category.objects.all()
    categories_json = [category.to_json for category in categories]
    return JsonResponse(categories_json,safe = False)

def category_get(request):
    try:
        category = Category.objects.get(id = category.id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error' : str(e)})
    return JsonResponse(categoty.to_json())

def category_products(request, category_id):
    try:
        products = Product.objects.filter(product_id = roduct.id)
        products_json = [product.to_json() for product in products]
    except Product.DoesNotExist as e:
        return JsonResponse({'erroe': str(e)})
    return JsonResponse(products_json, safe = False)
