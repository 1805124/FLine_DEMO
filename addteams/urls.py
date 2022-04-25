from django.contrib import admin
from django.urls import path
from addteams import views

urlpatterns = [
    path('addteams.html',views.addteams,name='TEAM_PAGE'),
]