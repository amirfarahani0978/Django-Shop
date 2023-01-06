from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"
    def get_answer(self,obj):
        result = obj.answer.all()
        return OrderItemsSerializer(instance=result , many =True).data

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()