from django.contrib import admin
from django.urls import path
from ngosignup import views

urlpatterns = [
    path('ngosignup',views.ngosignup,name='AFTER_SIGNUP'),
]


    
