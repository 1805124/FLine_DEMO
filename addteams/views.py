from django.shortcuts import render
from distributionteamsignup.models import USERS
from django.http import JsonResponse

# Create your views here.
qs = USERS.objects.all()

def addteams(request):
    context = {'userlist':full }
    return render(request,"addteams.html",context)


