from django.contrib import admin
from django.urls import path
from HOME import views

urlpatterns = [
    path('',views.index,name='HOME_PAGE'),
    path('index.html',views.index,name='HOME_PAGE'),
    path('signUp.html',views.sign_up,name='SIGNUP_PAGE_LANDING'),
     path('ngoSignUp.html',views.sign_up_ngo,name='SIGNUP_PAGE_NGO'),
    path('aboutUs.html',views.about_us,name='ABOUT_US_PAGE'),
    path('hotelSignUp.html',views.sign_up_hotel,name='SIGNUP_PAGE_HOTEL'),
    path('distributionTeamSignUp.html',views.distributionTeamSignUp,name='SIGNUP_PAGE_DISTRIBUTION_TEAM'),
    path('login',views.login,name='LOGIN')
    
]