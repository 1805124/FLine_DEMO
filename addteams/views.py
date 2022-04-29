from django.shortcuts import render
from addteams import models
from django.http import JsonResponse
from distributionteamsignup.models import USERS
from addteams.models import Newteam
from addteams.models import Newteammember

# Create your views here.

def addteams(request):
    if(request.method=="POST"):
        ngo_mail_id = request.POST.get("ngo_email")
        print(ngo_mail_id)
        context={"mail_ngo":ngo_mail_id}
        return render(request,"addteams.html",context)

    return render(request,"addteams.html")

def addteammember(request):
    if(request.method=="POST"):
        ngo_email= request.POST.get('ngo_email')
        Team_Name = request.POST.get('TName')
        team_image = request.FILES.get('Timage')
        Cdata = Newteam.objects.filter(Team_name=Team_Name)
        if(len(Cdata)>0):
           dir={"email_present":"SAME TEAM NAME [Alredy Existed] SUSPECTION DETECTED...LOGGING OUT "}
           return render(request,"index.html",dir) 
        ins = models.Newteam(Team_name=Team_Name,Ngo_name=ngo_email,Profile_pic=team_image)
        ins.save()
        print(ngo_email)
        print(Team_Name)
        context ={"ngos" : ngo_email}
        all_users = USERS.objects.all()
        all_teams = Newteam.objects.all()
        context = {"user_vals": all_users,"team_vals":all_teams,"ngo_mail":ngo_email}
        return render(request,"addteammember.html",context)

def submitteammember(request):
    if(request.method=="POST"):
        Team_Name = request.POST.get("team")
        volun_email = request.POST.get("volunteer")
        ngo_mail = request.POST.get("ngo")
    ins = models.Newteammember(Team_name=Team_Name,Ngo_email=ngo_mail,User_email=volun_email)
    ins.save()
    all_users = USERS.objects.all()
    all_teams = Newteam.objects.all()
    context = {"user_vals": all_users,"team_vals":all_teams,"ngo_mail":ngo_mail}
    return render(request,"addteammember.html",context)
