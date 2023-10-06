from django.db import models
from core.models import BaseModel
from product.models import Product
from account.models import Account
from django.core.validators import MinValueValidator, MaxValueValidator


class Order(BaseModel):
    user = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='orders')
    state = models.CharField(max_length=100, null=True)
    paid = models.BooleanField(default=False)
    description = models.CharField(max_length=100, null=True)
    created = models.DateField(auto_now_add=True)
    offer = models.IntegerField(default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user}'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.offer:
            discount_price = (self.offer / 100)*total
            return (total - discount_price)
        return total


class OrderItem(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.quantity}'

    def get_cost(self):
        return self.price*self.quantity


class Offer(BaseModel):
    expire_time = models.DateTimeField()
    start_time = models.DateTimeField()
    percent = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(90)])
    offer_code = models.CharField(max_length=100, unique=True)
    is_available = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.offer_code