from django import forms
from products.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'snippet', 'cost', 'Manufacturer', 'country']  # Опечатка большой буквы