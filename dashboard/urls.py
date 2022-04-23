from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('req_sent',views.req_sent,name='REQUEST_SENDING'),
    path('accept',views.accept,name='REQUEST_ACCEPT'),
    path('reject',views.reject,name='REQUEST_Rejected'),
]