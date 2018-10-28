from django.urls import path
from products.views import category_create
#, category_model_create

app_name = 'categories'

urlpatterns = [
    path('category_create/', category_create, name='category_create'),
]