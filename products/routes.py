from django.urls import path

from .views.products import product_json_list


app_name = 'rest_main'

urlpatterns = [
    path('', product_json_list, name='list'),
]
