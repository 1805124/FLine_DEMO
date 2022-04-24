from django.shortcuts import render,HttpResponse
from distributionteamsignup.models import USERS
from hotelsignup.models import hotelsignup
from ngosignup.models import ngosignup 
from django.contrib import messages
from dashboard.models import request_manage

# Create your views here.
def index(request):
    return render(request,'index.html') 
def sign_up(request):
    return render(request,'signUp.html')
def sign_up_ngo(request):
    return render(request,'ngoSignUp.html')
def about_us(request):
    return render(request,'aboutUs.html')
def dash_hotel(request):
    return render(request,"hotel.html")
def sign_up_hotel(request):
    return render(request,"hotelSignUp.html")
def distributionTeamSignUp(request):
    return render(request,"distributionTeamSignUp.html")

def login(request):
    if (request.method=='POST'):
        email= request.POST.get("login_email")
        password = request.POST.get("login_password")
        if ( len(request.POST.getlist("remember_me"))!=0):
            b_check = True
        print(email,"     ",password)
        data1 = USERS.objects.filter(req_email=email)
        data2 = hotelsignup.objects.filter(hotel_email=email)
        data3 = ngosignup.objects.filter(req_email=email)
        if(len(data1)>0):
            for a in data1:
                if (a.req_password == password):
                    print("validated .. Login Successfull as USER")
                    context={
                        "NAME":a.req_name,
                        "EMAIL":a.req_email,
                        "CONTACT":a.req_phone,
                        "AGE":a.age,
                        "DOMAIN":a.domain,
                        "IMAGE":a.profile_pic,
                        "TYPE":"USER"
                    }
                    return render(request,"dash.html",context) 
                else:
                    print("Password does Not Matching .. login failed")
                    context={ "alertval":"PASSWORD WAS INVALID BRO",}
                    return render(request,"index.html",context)
        elif(len(data2)>0):
            for a in data2:
                if (a.password == password):
                    print("validated .. Login Successfull as HOTEL")
                    requests = request_manage.objects.filter(receiever=email)
                    context={
                        "NAME":a.req_name,
                        "HOTEL_NAME":a.hotel_name,
                        "CONTACT":a.hotel_phone,
                        "EMAIL":a.hotel_email,
                        "ZONE":a.ZONE,
                        "CAPACITY":a.CAPACITY,
                        "IMAGE":a.hotel_image_upload,
                        "AUTH_DOC":a.auth_doc_upload,
                        "TYPE":"HOTEL",
                        "REQUESTS":requests

                    }
                    return render(request,"dash.html",context) 
                else:
                    print("Password does Not Matching .. login failed")
                    context={ "alertval":"PASSWORD WAS INVALID BRO",}
                    return render(request,"index.html",context)
        elif(len(data3)>0):
            for a in data3:
                if (a.passkey == password):
                    print("validated .. Login Successfull as NGO")
                    hotels = hotelsignup.objects.filter(ZONE=a.ZONE)
                    context={
                        "NAME":a.req_name,
                        "CONTACT":a.req_phone,
                        "EMAIL":a.req_email,
                        "ZONE":a.ZONE,
                        "AREA":a.AREA,
                        "CAPACITY":a.CAPACITY,
                        "IMAGE":a.image_upload,
                        "TYPE":"NGO",
                        "HOTELS":hotels,
                        "id":a.id
                    }
                    return render(request,"dash.html",context) 
                else:
                    print("Password does Not Matching .. login failed")
                    context={ "alertval":"PASSWORD WAS INVALID BRO",}
                    return render(request,"index.html",context)
        else:
            print("email id Not Registered...")
            messages.info(request,"EMAIL NOT REGISTERED YET")
            return render(request,"signUp.html")
           
            
            



    
