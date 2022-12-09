from django.db import models
from customer.models import Customer
from core.models import BaseModel
class Category(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name


class ProductFeature(BaseModel):
    amount = models.PositiveIntegerField()
    descript = models.CharField(max_length=200 , null=True)
    def __str__(self) -> str:
        return self.amount

# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=40)
    image = models.ImageField()
    price = models.PositiveIntegerField()
    count_buying = models.PositiveIntegerField()
    status_available = models.BooleanField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    history_price = models.JSONField()
    rate = models.PositiveIntegerField()
    product_feature = models.OneToOneField(ProductFeature, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return f"{self.name} {self.price} {self.status_available}"


class Offer(BaseModel):
    expire_time = models.DateField()
    start_time = models.DateField()
    min_price = models.PositiveIntegerField()
    max_price = models.PositiveIntegerField()
    percent = models.PositiveIntegerField()
    offer_code = models.CharField(max_length=100 , null=True)
    is_available = models.BooleanField()


class Comment(BaseModel):
    profile_id = models.OneToOneField(Customer , on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.profile_id} {self.product_id}"