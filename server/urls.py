"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from products.api.products import ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)

default_router = [
    path('categories_endpoints/', include('products.endpoints.categories')),
    path('products_endpoints/', include('products.endpoints.products')),
    path('products/', include('products.routes')),
    path('cart/', include('cart.routes')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls.products')),
    path('categories/', include('products.urls.categories')),
    path('cart/', include('cart.urls')),
    path('', include('mainapp.urls')),
    path('default_api/', include(default_router)),
    path('api/', include(router.urls)),
    path('auth/oauth2/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
