from django.urls import path
from products.views import product_list, product_detail, product_model_create, product_model_update,\
    product_model_delete

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', product_detail, name='product_detail'),
    path('product_create/', product_model_create, name='product_create'),
    path('product_update/<int:pk>/', product_model_update, name='product_update'),
    path('product_delete/<int:pk>/', product_model_delete, name='product_delete'),
    path('', product_list, name='product_list'),
]