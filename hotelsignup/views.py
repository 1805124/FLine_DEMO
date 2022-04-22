from django.shortcuts import render
from hotelsignup import models
from hotelsignup.models import hotelsignup as hotelmodel
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
        ins.save()
        hoteldata= hotelmodel.objects.get(hotel_email=hotel_Email)
        print("THE DATA ADDED FROM HOTELSIGNUP")
    else:
        print("NOT A POST")
    context={
        "NAME": req_name,
        "IMAGE" : hoteldata.hotel_image_upload,
        "HOTEL_NAME":hotel_name,
        "HOTEL_EMAIL":hotel_Email,
        "CONTACT":hotel_Phone,
        "CAPACITY":hotel_sub,
        "ZONE":hotel_zone,
        "AUTH_DOC":auth_pic,
        "AUTH":author,
        "TYPE":"HOTEL"
    }
    return render(request,"dash.html",context)





