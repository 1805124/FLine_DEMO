from django.shortcuts import render
from ngosignup import models
from ngosignup.models import ngosignup,USERS

# Create your views here.
def ngosignup(request):
    if request.method =="POST":
        print("this is post")
        req_name = request.POST['req_name']
        print(req_name)
        contact_no = request.POST['req_phone']
        print(contact_no)
        email = request.POST['req_email']
        print(email)
        passkey = request.POST['passkey']
        print(passkey)
        zone = request.POST['ZONE']
        print(zone)
        area = request.POST['AREA']
        print(area)
        capacity = request.POST['CAPACITY']
        print(capacity)
        image_upload = request.FILES['image_upload']
        author = request.POST.getlist('author')
        if(len(author)==0):
           b_auth = False
        else:
            b_auth = True    
        
        ins = models.ngosignup(req_name=req_name,req_phone=contact_no,req_email=email,passkey=passkey,ZONE=zone,AREA=area,CAPACITY=capacity,image_upload=image_upload,author=b_auth)
        ins2 = models.USERS(req_name=req_name,req_email=email,req_password=passkey,age=18,domain="RV",profile_pic= image_upload,agree=b_auth,req_phone=contact_no)
        ins.save()
        ins2.save()
        print("The DATA HAS BEEN ADDED TO THE DB")
        return render(request,"dash.html",context)
        




