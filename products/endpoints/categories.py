from django.urls import path
from products.api import rest_category_list

app_name = 'rest_categories'

urlpatterns = [
    path('', rest_category_list, name='rest_list'),
]