from shop.models.product_model import ProductModel
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['artisan', 'name_product', 'description_product','price', 'image']
