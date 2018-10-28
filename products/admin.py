from django.contrib import admin
from products.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    list_filter = [
        'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    search_fields = [
        'title'
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'cost', 'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    list_filter = [
        'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    search_fields = [
        'title', 'snippet'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)