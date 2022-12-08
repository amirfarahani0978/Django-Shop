from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    count_buying = models.PositiveIntegerField()
    status_available = models.BooleanField()
    quantity = models.PositiveIntegerField() 
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    history_price = models.JSONField()
    rate = models.PositiveIntegerField()

class Offer(models.Model):
    expire_time = models.DateField()
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    percent = models.PositiveIntegerField()
    offer_code = models.CharField(max_length=100)
    is_available = models.BooleanField()