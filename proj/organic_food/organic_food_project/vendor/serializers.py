# vendor/serializers.py
from rest_framework import serializers
from .models import Vendor, Product

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'username', 'email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'vendor', 'category', 'name', 'price', 'image', 'quantity')
