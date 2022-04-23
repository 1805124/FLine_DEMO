from django.db import models

# Create your models here.

class request_manage(models.Model):
    sender = models.CharField(max_length=255)
    s_type = models.CharField(max_length=255)
    head_count = models.CharField(max_length=255)
    receiever = models.CharField(max_length=255)
    r_type = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

