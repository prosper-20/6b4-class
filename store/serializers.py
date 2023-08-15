from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # fields = ["name", "slug", "price", "image", "is_available"]


# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     slug = serializers.SlugField()

