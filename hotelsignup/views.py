from django.shortcuts import render
from hotelsignup import models
from hotelsignup.models import hotelsignup,USERS
# Create your views here.
def hotelsignup(request):
    print("HELLO")
    if ( request.method == "POST"):
        print("POST DETECTED")
        req_name = request.POST.get('req_name')
        hotel_name = request.POST.get('HOTEL')
        hotel_Email = request.POST.get('HOTEL_EMAIL')
        password1 = request.POST.get('password1')
        hotel_Phone = request.POST.get('hotel_phone')
        hotel_sub = request.POST.get('capacity')
        hotel_zone = request.POST.get('ZONE')
        profile_pic = request.FILES['UploadedImage']
        auth_pic = request.FILES['auth_image']
        print(request.FILES)
        author = request.POST.getlist('author')
        if(len(author)==0):
            b_auth = False
        else:
            b_auth = True
        ins = models.hotelsignup(req_name=req_name,hotel_name=hotel_name,hotel_phone = hotel_Phone,hotel_email= hotel_Email,password=password1,ZONE=hotel_zone,CAPACITY=hotel_sub,hotel_image_upload=profile_pic,auth_doc_upload=auth_pic,author=b_auth)
        ins2 = models.USERS(req_name=req_name,req_email=hotel_Email,req_password=password1,req_phone=hotel_Phone,age=18,domain="RV",profile_pic=profile_pic,agree=b_auth)
        ins.save()
        ins2.save()
        print("THE DATA ADDED FROM HOTELSIGNUP")
    else:
        print("NOT A POST")
    return render(request,"index.html")





