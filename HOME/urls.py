from django.contrib import admin
from django.urls import path
from HOME import views

urlpatterns = [
    path('',views.index,name='HOME_PAGE'),
    path('signUp.html',views.sign_up,name='SIGNUP_PAGE'),
    path('sign-up',views.sign_up,name='SIGN_UP_PAGE'),
    path('dash_hotel',views.dash_hotel,name='HOTEL_DASHBOARD_PAGE'),
    path('dash_ngo',views.dash_ngo,name='NGO_DASHBOARD_PAGE'),
    path('dash_user',views.dash_user,name='USER_DASHBOARD_PAGE')
]
