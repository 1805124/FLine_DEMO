from django.shortcuts import render,HttpResponse

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
