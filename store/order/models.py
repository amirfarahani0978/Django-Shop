from django.db import models
from product.models import Offer
# Create your models here.
 
class Order(models.Model):
    state = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    time = models.DateField()
    total_price = models.PositiveIntegerField()
    offer_id = models.OneToOneField(Offer , on_delete=models.CASCADE, related_name='order')


class Order_item(models.Model):
    quantity = models.PositiveIntegerField()