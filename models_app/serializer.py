from rest_framework import serializers
from models_app.models import PickUpWarehouseLocation, ProductType

class FilterGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpWarehouseLocation
        fields = "__all__"


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductType
        fields = ['name', 'product_quality', 'category']
        