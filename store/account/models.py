from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager
# Create your models here.


class Account(AbstractBaseUser):
    GENDER_CHOICE = (('male', 'MALE'), ('female', 'FEMALE'))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    image = models.ImageField(upload_to='', null=True)
    postal_code = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = AccountManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Address(BaseModel):
    address = models.CharField(max_length=200)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.address


class Wishing(BaseModel):
    user_id = models.OneToOneField(Account, on_delete=models.CASCADE)


class Wishing_item(BaseModel):
    # product_id = models.ForeignKey(Product , on_delete=models.CASCADE)
    wishing = models.ForeignKey(Wishing, on_delete=models.CASCADE)
