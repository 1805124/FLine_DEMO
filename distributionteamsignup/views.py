from django.shortcuts import render
from distributionteamsignup import models
from distributionteamsignup.models import USERS
# Create your views here.
def distributionteamsignup(request):
    if request.method == "POST":
      req_name = request.POST.get('req_name')
      req_email = request.POST.get('req_email')
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
      ins = models.USERS(req_name=req_name,req_email=req_email,req_password=password,req_phone=req_phone,age=age,domain=domain,profile_pic=profile_picture,agree=b_authentic)
      ins.save()
      print("THE DATA ADDED SUCCESSFULLY IN STUDENT DB")
      data1 = USERS.objects.filter(req_email=req_email)
      if(len(data1)>0):
          for a in data1:
              context={
                  "IMAGE":a.profile_pic,
                  "NAME":req_name,
                  "EMAIL":req_email,
                  "CONTACT":req_phone,
                  "AGE":age,
                  "DOMAIN":domain
              }

      return render(request,"dash.html",context)







