from rest_framework import serializers
from .models import Product, LineItem


class ProductSerializer(serializers.ModelSerializer):
    # put some validations in the fields
    description = serializers.CharField(min_length=5, max_length=200)
    # validate the price??? 1 euro, 300 eur.
    price = serializers.FloatField(min_value=10, max_value=255)
    line_items = serializers.SerializerMethodField()

    def get_line_items(self, instance):
        items = LineItem.objects.filter(product=instance)
        return LineItemSerializer(items, many=True).data

    class Meta:
        model = Product
        fields = ["id", "name", "description", "photo", "price", "line_items"]


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ["product", "quantity"]  # collections
