from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from ngosignup.models import ngosignup
from hotelsignup.models import hotelsignup
from dashboard.models import request_manage
from dashboard import models 

# Create your views here.

def req_sent(request):
    if(request.method == "POST"):
        sender = request.POST.get('sender_mail')
        receiever = request.POST.get('hotel_email')
        head_count = request.POST.get('head_count')
        s_Type="NGO"
        r_Type="HOTEL"
        ins = models.request_manage(sender=sender,s_type=s_Type,head_count=head_count,receiever=receiever,r_type=r_Type)
        ins.save()
        dat = ngosignup.objects.get(req_email=sender)
        hotels = hotelsignup.objects.filter(ZONE=dat.ZONE)
        context={
                "NAME":dat.req_name,
                "CONTACT":dat.req_phone,
                "EMAIL":dat.req_email,
                "ZONE":dat.ZONE,
                "AREA":dat.AREA,
                "CAPACITY":dat.CAPACITY,
                "IMAGE":dat.image_upload,
                "TYPE":"NGO",
                "HOTELS":hotels
            }
        return render(request,"dash.html",context)


