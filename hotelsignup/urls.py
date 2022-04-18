from django.contrib import admin
from django.urls import path
from hotelsignup import views

urlpatterns = [
    path('hotelsignup',views.hotelsignup,name='HOTEL_SIGNUP'),
]


    
