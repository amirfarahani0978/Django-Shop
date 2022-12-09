from django.db import models
from product.models import Product
from core.models import BaseModel
class User(BaseModel):
    phone_number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField()
    is_admin = models.BooleanField()


class Wishing(BaseModel):
    user_id = models.OneToOneField(User , on_delete= models.CASCADE)


class Wishing_item(models.Model):
    product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    wishing = models.ForeignKey(Wishing , on_delete=models.CASCADE)
