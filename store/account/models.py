from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AccountManager
# Create your models here.


class Account(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICE = (('male', 'MALE'), ('female', 'FEMALE'))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile/%Y/%m/%d/', blank=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICE, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = AccountManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return self.phone_number

    @property
    def is_staff(self):
        return self.is_admin


class Address(BaseModel):
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=400)
    Alley = models.CharField(max_length=400)
    Housenumber = models.PositiveIntegerField()
    Housebell = models.PositiveIntegerField()
    Postal_code = models.IntegerField(null=True, blank=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE , related_name='address')

    def __str__(self) -> str:
        return self.street



class Wishing(BaseModel):
    user_id = models.OneToOneField(Account, on_delete=models.CASCADE)


class Wishing_item(BaseModel):
    # product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    wishing = models.ForeignKey(Wishing, on_delete=models.CASCADE)


class OtpCode(BaseModel):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    create = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.phone_number} - {self.code} - {self.create}'
