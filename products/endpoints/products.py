from django.urls import path
from products.api import rest_product_list

app_name = 'rest_products'

urlpatterns = [
    path('', rest_product_list, name='rest_list'),
]