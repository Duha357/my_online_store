from django.urls import path
from products.api import rest_category_list, CategoryList

app_name = 'rest_categories'

urlpatterns = [
    path('', CategoryList.as_view(), name='rest_list'),
]

# urlpatterns = [
#     path('', rest_category_list, name='rest_list'),
# ]