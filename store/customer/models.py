from django.db import models

# Create your models here.

class Customer(models.Model):
    GENDER_CHOICE = (('male', 'MALE'), ('female', 'FEMALE'))
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField()
    postal_code = models.IntegerField()
    gender = models.CharField(max_length=5, choices=GENDER_CHOICE)
    def __str__(self):
        return self.firstname