from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contacts/', views.contacts),
    path('products/', views.products),
    path('product_1/', views.product_1),
]
