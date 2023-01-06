from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    price = serializers.IntegerField()
    count = serializers.IntegerField()