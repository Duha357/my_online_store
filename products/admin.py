from django.contrib import admin
from django.template.loader import render_to_string
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
        'title', 'picture', 'cost', 'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    list_filter = [
        'modified', 'created'
    ]  # Опечатка в слове modifie_(l)_d
    search_fields = [
        'title', 'snippet'
    ]

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'image': obj.image.url}
        )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)