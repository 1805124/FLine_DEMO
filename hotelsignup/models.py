from django.db import models
from distributionteamsignup.models import USERS

# Create your models here.

class hotelsignup(models.Model):
    req_name = models.CharField(max_length=255)
    hotel_name = models.CharField(max_length=255)
    hotel_phone = models.DecimalField(max_digits=10,decimal_places=0)
    hotel_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    ZONE = models.CharField(max_length=255)
    CAPACITY = models.CharField(max_length=255)
    hotel_image_upload = models.ImageField(null=True,blank=True,upload_to="static/images/hotelsignupimages/PROFILE_PICS")
    auth_doc_upload = models.ImageField(null=True,blank=True,upload_to="static/images/hotelsignupimages/AUTHENTICATION_DOCS")
    author = models.BooleanField()