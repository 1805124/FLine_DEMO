from django.shortcuts import render
from ngosignup import models
from ngosignup.models import ngosignup as ngomodel
from distributionteamsignup.models import USERS
from hotelsignup.models import hotelsignup 

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
        prevdat = ngomodel.objects.filter(req_email=email)
        prevdat2 = USERS.objects.filter(req_email=email)
        prevdat3 = hotelsignup.objects.filter(hotel_email=email)
        if(len(prevdat)+len(prevdat2)+len(prevdat3)>0):
           dir = {"email_present":"Email id Alredy Existed Try to LOGIN "}
           return render(request,"index.html",dir) 
        ins = models.ngosignup(req_name=req_name,req_phone=contact_no,req_email=email,passkey=passkey,ZONE=zone,AREA=area,CAPACITY=capacity,image_upload=image_upload,author=b_auth)
        ins.save()
        loc= ngomodel.objects.get(req_email=email)
        print("The DATA HAS BEEN ADDED TO THE DB")
        context={
            "NAME" :req_name,
            "IMAGE":loc.image_upload,
            "CONTACT":contact_no,
            "EMAIL":email,
            "ZONE":zone,
            "AREA":area,
            "CAPACITY":capacity,
            "AUTH":b_auth,
            "TYPE":"NGO",
            "id":loc.id
        }
        return render(request,"dash.html",context)
        





