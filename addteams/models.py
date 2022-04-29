from django.db import models


# Create your models here.
class Newteam(models.Model):
    Team_name = models.CharField(max_length=256)
    Ngo_name = models.CharField(max_length=256)
    Profile_pic = models.ImageField(null=True,blank=True,upload_to="static/images/userspic")
    
class Newteammember(models.Model):
    Team_name = models.CharField(max_length=256)
    User_email = models.CharField(max_length=256)
    Ngo_email = models.CharField(max_length=256)

    