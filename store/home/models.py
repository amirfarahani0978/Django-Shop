from django.db import models
from core.models import BaseModel
class Baner(BaseModel):
    banner = models.ImageField(upload_to ='banner/')