from django.db import models

# Create your models here.
class USERS(models.Model):
    req_name = models.CharField(max_length=256)
    req_email = models.EmailField(max_length=256)
    req_password = models.CharField(max_length=256)
    req_phone = models.DecimalField(max_digits=10,decimal_places=0)
    age = models.DecimalField(max_digits=5,decimal_places=0)
    domain = models.CharField(max_length=10)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="static/images/userspic")
    agree = models.BooleanField()
    




