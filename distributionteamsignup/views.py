from django.shortcuts import render
from distributionteamsignup import models
from distributionteamsignup.models import USERS
from ngosignup.models import ngosignup as ngomodel
# Create your views here.
def distributionteamsignup(request):
    if request.method == "POST":
      req_name = request.POST.get('req_name')
      req_Email = request.POST.get('req_email')
      password = request.POST.get('password')
      req_phone = request.POST.get('req_phone')
      age = request.POST.get('age')
      domain = request.POST.get('domain')
      profile_picture = request.FILES.get('UploadedImage')
      authentic = request.POST.getlist('auth')
      if(len(authentic)!=0):
          b_authentic = True
      else:
          b_authentic = False 
      prevdat = ngomodel.objects.filter(req_email=req_Email)
      prevdat2 = USERS.objects.filter(req_email=req_Email)
      prevdat3 = hotelsignup.objects.filter(hotel_email=req_Email)
      if(len(prevdat)+len(prevdat2)+(prevdat3)<=0):
           dir = {"email_present":"Email id Alredy Existed Try to LOGIN "}
           return render(request,"index.html",dir) 
      ins = models.USERS(req_name=req_name,req_email=req_Email,req_password=password,req_phone=req_phone,age=age,domain=domain,profile_pic=profile_picture,agree=b_authentic)
      ins.save()
      print("THE DATA ADDED SUCCESSFULLY IN USERS DATA BASE")
      data1 = USERS.objects.get(req_email=req_Email)
      context={
                  "IMAGE":data1.profile_pic,
                  "NAME":req_name,
                  "EMAIL":req_Email,
                  "CONTACT":req_phone,
                  "AGE":age,
                  "DOMAIN":domain,
                  "TYPE":"USER"
              }

      return render(request,"dash.html",context)







