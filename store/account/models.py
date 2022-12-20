from django.db import models
from core.models import BaseModel
# Create your models here.
class Account(BaseModel):
    GENDER_CHOICE = (('male', 'MALE'), ('female', 'FEMALE'))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='' , null=True)
    postal_code = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE , null=True)
    phone_number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField()
    is_admin = models.BooleanField()
    def __str__(self):
        return self.firstname

class Address(BaseModel):
    address = models.CharField(max_length=200)
    account_id = models.ForeignKey(Account , on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.address

class Wishing(BaseModel):
    user_id = models.OneToOneField(Account , on_delete= models.CASCADE)


class Wishing_item(BaseModel):
    # product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    wishing = models.ForeignKey(Wishing , on_delete=models.CASCADE)