from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    Manufacturer = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['url', 'title', 'category', 'image', 'snippet', 'cost', 'Manufacturer', 'country', 'modified', 'created']

    def get_image(self, obj):
        return obj.image.url

    def get_category(self, obj):
        return obj.category.title

    def get_Manufacturer(self, obj):
        return obj.Manufacturer.name