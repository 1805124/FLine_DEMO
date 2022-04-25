from django.db import models

# Create your models here.

class teams(models.Model):
    TEAM_name = models.CharField(max_length=255)
    member1=models.CharField(max_length=255)
    member2=models.CharField(max_length=255)
    member3=models.CharField(max_length=255)
    member4=models.CharField(max_length=255)
    member5=models.CharField(max_length=255)
    hotel_image_upload = models.ImageField(null=True,blank=True,upload_to="static/images/TEAMPIC")