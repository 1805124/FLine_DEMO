from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from ngosignup.models import ngosignup
from hotelsignup.models import hotelsignup
from dashboard.models import request_manage
from dashboard import models 
from dashboard.models import subscription
from datetime import datetime,timezone

# Create your views here.

def req_sent(request):
    if(request.method == "POST"):
        sender = request.POST.get('sender_mail')
        receiever = request.POST.get('hotel_email')
        head_count = request.POST.get('head_count')
        s_Type="NGO"
        r_Type="HOTEL"
        try:
            subdata = subscription.objects.get(ngo_sub=sender,hotel_sub=receiever)
        except subscription.DoesNotExist:
            subdata = None
        if (subdata == None) or (((subdata.sub_date-datetime.now(timezone.utc)).days+subdata.days)>=0):
            ins = models.request_manage(sender=sender,s_type=s_Type,day_count=head_count,receiever=receiever,r_type=r_Type)
            ins.save()
        dat = ngosignup.objects.get(req_email=sender)
        hotels = hotelsignup.objects.filter(ZONE=dat.ZONE)
        sub2datas = subscription.objects.filter(ngo_sub=sender).values("hotel_sub")
        subscriptdaTa = subscription.objects.filter(ngo_sub=sender)
        mango=[]
        for q in hotels:
            if q.hotel_email not in sub2datas:
                mango.append(q)
        context={
                "NAME":dat.req_name,
                "CONTACT":dat.req_phone,
                "EMAIL":dat.req_email,
                "ZONE":dat.ZONE,
                "AREA":dat.AREA,
                "CAPACITY":dat.CAPACITY,
                "IMAGE":dat.image_upload,
                "TYPE":"NGO",
                "HOTELS":mango,
                "SUBSCRIPTIONS":subscriptdaTa
            }
        return render(request,"dash.html",context)

def accept(request):
    if(request.method == "POST" ):
        iden = request.POST.get('identifier')
        hotel_Sub = request.POST.get('hotel_sub')
        ngo_Sub = request.POST.get('ngo_sub')
        day_count=request.POST.get('day_count')
        ins= models.subscription(hotel_sub=hotel_Sub,ngo_sub=ngo_Sub,days=day_count)
        ins.save()
        datax= hotelsignup.objects.get(hotel_email=hotel_Sub)
        request_manage.objects.filter(id=iden).delete()
        requests = request_manage.objects.filter(receiever=hotel_Sub)
        subs = subscription.objects.filter(hotel_sub=hotel_Sub)
        #requests = request_manage.exclude(receiever__in=subscription.objects.filter(hotel_sub=hotelSub))
        context={
            "NAME":datax.req_name,
            "HOTEL_NAME":datax.hotel_name,
            "CONTACT":datax.hotel_phone,
            "EMAIL":datax.hotel_email,
            "ZONE":datax.ZONE,
            "CAPACITY":datax.CAPACITY,
            "IMAGE":datax.hotel_image_upload,
            "AUTH_DOC":datax.auth_doc_upload,
            "TYPE":"HOTEL",
            "REQUESTS":requests,
            "SUBSCRIPTIONS":subs
        }
        return render(request,"dash.html",context)

def reject(request):
    if(request.method=="POST"):
        id=request.POST.get('identifier')
        request_manage.objects.filter(id=id).delete()
        hotel_Sub = request.POST.get('hotel_sub')
        datax = hotelsignup.objects.get(hotel_email=hotel_Sub)
        requests = request_manage.objects.filter(receiever=hotel_Sub)
        subs = subscription.objects.filter(hotel_sub=hotel_Sub)
        context={
            "NAME":datax.req_name,
            "HOTEL_NAME":datax.hotel_name,
            "CONTACT":datax.hotel_phone,
            "EMAIL":datax.hotel_email,
            "ZONE":datax.ZONE,
            "CAPACITY":datax.CAPACITY,
            "IMAGE":datax.hotel_image_upload,
            "AUTH_DOC":datax.auth_doc_upload,
            "TYPE":"HOTEL",
            "REQUESTS":requests,
            "SUBSCRIPTIONS":subs
        }
        return render(request,"dash.html",context)






