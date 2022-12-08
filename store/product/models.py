from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    count_buying = models.PositiveIntegerField()
    status_available = models.BooleanField()
    quantity = models.PositiveIntegerField() 


class Category(models.Model):
    name = models.CharField(max_length=100)
    