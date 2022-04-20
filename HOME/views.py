from django.shortcuts import render,HttpResponse
from distributionteamsignup.models import USERS
from django.contrib import messages


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
        if(len(data1)>0):
            for a in data1:
                if (a.req_password == password):
                    print("validated .. Login Successfull")
                    context={
                        "NAME":a.req_name,
                        "AGE":a.age,
                        "DOMAIN":a.domain,
                        "IMAGE":a.profile_pic }
                    return render(request,"dash.html",context) 
                else:
                    print("Password does Not Matching .. login failed")
                    context={ "alertval":"PASSWORD WAS INVALID BRO",}
                    return render(request,"index.html",context)
        else:
            print("email id Not Registered...")
            messages.info(request,"EMAIL NOT REGISTERED YET")
            return render(request,"signUp.html")
            
            



    
