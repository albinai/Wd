from .views import categories_all, category_get, product_get, products_all, category_products

from django.urls import path

urlpatterns = [
    path('category/', categories_all),
    path('category/<int:categoty_id>', category_get),
    path('product/', products_all),
    path('product/<int:product_id>', product_get),
    path('api/categories/<int:id>/products/', category_products),

]