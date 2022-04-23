from django.db import models

# Create your models here.

class request_manage(models.Model):
    sender = models.CharField(max_length=255)
    s_type = models.CharField(max_length=255)
    day_count = models.CharField(max_length=255)
    receiever = models.CharField(max_length=255)
    r_type = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

class subscription(models.Model):
    hotel_sub = models.CharField(max_length=255)
    ngo_sub = models.CharField(max_length=255)
    sub_date = models.DateTimeField(auto_now_add=True)
    days = models.DecimalField(max_digits=3,decimal_places=0)
    
