from django.db import models
from product.models import Offer
from core.models import BaseModel
from product.models import Product


class Order(BaseModel):
    state = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    time = models.DateField()
    total_price = models.PositiveIntegerField()
    offer_id = models.OneToOneField(
        Offer, on_delete=models.CASCADE, related_name='order', null=True)

    def __str__(self) -> str:
        return f"{self.time} + {self.total_price}"

    def get_totorial_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.quantity

    def get_cost(self):
        return self.price*self.quantity
