from django.contrib import admin
from django.urls import path
from addteams import views

urlpatterns = [
    path('addteam',views.addteams,name='TEAM_PAGE'),
    path('addteammember',views.addteammember,name='TEAM_MEM_PAGE'),
     path('submitteammember',views.submitteammember,name='TEAM_MEM_PAGE_2')
]

