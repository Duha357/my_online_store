from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
    product_list, product_detail, product_model_create, product_model_update, product_model_delete

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', product_model_delete, name='product_delete'),
] + staticfiles_urlpatterns()

# urlpatterns = [
#     path('', product_list, name='product_list'),
#     path('<int:pk>/', product_detail, name='product_detail'),
#     path('product_create/', product_model_create, name='product_create'),
#     path('product_update/<int:pk>/', product_model_update, name='product_update'),
#     path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
# ]