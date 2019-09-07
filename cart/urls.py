from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import PurchaseListView, PurchaseMainCartView, PurchaseDetailView

app_name = 'cart'

urlpatterns = [
    path('', PurchaseListView.as_view(), name='list'),
    path('main/', PurchaseMainCartView.as_view(), name='main'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='detail'),
] + staticfiles_urlpatterns()