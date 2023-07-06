from django.db import models
from core.models import BaseModel
class Baner(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='banner/')