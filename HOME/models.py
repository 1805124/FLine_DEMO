from django.db import models

# Create your models here.
class notification_manage(models.Model):
    sender = models.CharField(max_length=255)
    f_type = models.CharField(max_length=255)
    receiever = models.CharField(max_length=255)
    r_type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    time = models.DateTimeField()

