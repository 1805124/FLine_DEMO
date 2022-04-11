from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html') 
def sign_up(request):
    return render(request,'signUp.html')

def dash_hotel(request):
    return render(request,"hotel.html")
def dash_ngo(request):
    return render(request,"ngo.html")
def dash_user(request):
    return render(request,"User.html")