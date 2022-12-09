from django.db import models
from user.models import User
# Create your models here.

class Customer(models.Model):
    GENDER_CHOICE = (('male', 'MALE'), ('female', 'FEMALE'))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='' , null=True)
    postal_code = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE , null=True)
    history_buy = models.JSONField(null=True)
    user_id = models.OneToOneField(User , on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname


class Address(models.Model):
    address = models.CharField(max_length=200)
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE)