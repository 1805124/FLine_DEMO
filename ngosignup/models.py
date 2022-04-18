from django.db import models
from distributionteamsignup.models import USERS

# Create your models here.

class ngosignup(models.Model):
    req_name = models.CharField(max_length=255)
    req_phone = models.DecimalField(max_digits=10,decimal_places=0)
    req_email = models.EmailField(max_length=254)
    passkey = models.CharField(max_length=255)
    ZONE = models.CharField(max_length=255)
    AREA = models.CharField(max_length=255)
    CAPACITY = models.CharField(max_length=255)
    image_upload = models.ImageField(null=True,blank=True,upload_to="static/images/ngosignupimages")
    author = models.BooleanField()

    