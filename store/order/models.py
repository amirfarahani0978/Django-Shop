from django.db import models
from product.models import Offer
from core.models import BaseModel
from product.models import Product
from account.models import Account

class Order(BaseModel):
    user = models.ForeignKey(Account , on_delete=models.CASCADE , related_name='orders')
    state = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    description = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_created=True)
    offer_id = models.OneToOneField(
        Offer, on_delete=models.CASCADE, related_name='order', null=True)

    def __str__(self) -> str:
        return f'{self.user} - {self.id}'

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
