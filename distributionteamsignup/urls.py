from django.contrib import admin
from django.urls import path
from distributionteamsignup import views

urlpatterns = [
    path('distributionteamsignup',views.distributionteamsignup,name='AFTER_SIGNUP'),
]


    
