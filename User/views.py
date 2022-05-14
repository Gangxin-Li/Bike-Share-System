from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from . import account_account_op
from User.models import account_account
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from Operator.models import Bike
from Operator.models import Station
from Operator.models import defectiveness_report
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist


def ulogin(request):
    context={}
    context['ulo1']='Sign in'
    return render(request,'ulogin.html',context)


def ulogin_post(request):
    ulogin_email=request.POST.get('email') 
    ulogin_password=request.POST.get('password')
    ue=str( account_account.objects.filter(email=ulogin_email)[0])
    
   

    if ue==ulogin_password:
        print("success")
        messages.success(request,"login successful")
        return render(request,'ume.html')
    else:
        print("in-success")
        messages.success(request,"login unsuccessful")
        return render(request,'ulogin.html')


def uregist_post(request):

    regist_name = request.POST.get('text')
    regist_email = request.POST.get('email')
    regist_pwd = request.POST.get('password')
    ADD = account_account(username = regist_name,password=regist_pwd,email=regist_email)
    ADD.save()
    return render(request,'ulogin.html')
        
def ume(request):
    context={}
    return render(request,'ume.html',context)

#Gangxin LI&Tianyi LI
def urecharge(request):
    ulogin_email=request.POST.get('email') 
    context={}
    context['uname']="sdafd"
    context['ubal']='33'
    cur_id = request.user.id
    pounds = request.POST.get('pounds')
    cur_pounds = account_account.objects.all()
    print(cur_pounds)
    account_account.objects.filter(id=cur_id).update(wallet_balance=pounds)


    return render(request,'urecharge.html',context)

@api_view(('GET',))
def viewDefectiveBikes(request):
    defectedBikes = Bike.objects.filter(is_faulty=True).all()
    y={}
    for i, c in enumerate(defectedBikes):
        sid = str(c.id)
        x=[]
        defectiveparts = defectiveness_report.objects.filter(bike_id=c.id).all()
        for l, m in enumerate(defectiveparts):
            x.append(m.defective_parts)
        y[c.id]=x
    return HttpResponse(json.dumps(y), content_type='application/json')

@api_view(('POST',))
def repairbikes(request):
    received_json_data=json.loads(request.body)
    bike_id=received_json_data['bike_id'] 
    defectiveness_report.objects.filter(bike_id=bike_id).update(is_fixed=True)
    Bike.objects.filter(id=bike_id).update(is_faulty=False)
    print (str(bike_id) + " HELLOOWW")
    return HttpResponse("repaired successfully", content_type='application/json')

@api_view(('GET',))
def trackBikes(request, station_id):
    freeBikes = Bike.objects.filter(in_use=False,station_id = station_id).all()
    x = []
    for i, c in enumerate(freeBikes):
        y={}
        y['bike_id'] = c.id
        y['is_faulty'] = c.is_faulty
        y['station_id'] = c.station_id
        if(y):
            x.append(y)
    return HttpResponse(json.dumps(x), content_type='application/json')

@api_view(('POST',))
def moveBikes(request):
    station_id=request.POST.get('station_id') 
    bike_id=request.POST.get('bike_id')
    try:
        Bike.objects.filter(id=bike_id).get()
        Bike.objects.filter(id=bike_id).update(station_id=station_id)  
        return HttpResponse("Bike moved successfully", content_type='application/json')
    except(ObjectDoesNotExist):
        return HttpResponse("Bike doesn't exist", content_type='application/json') 

def viewDefBikes(request):
    context={}
    return render(request,'listofRepairbikes.html',context)

def moveBikeshtml(request):
    context={}
    return render(request,'moveBikes.html',context)

def trackBikeshtml(request):
    context={}
    return render(request,'trackbikes.html',context)
    
@api_view(('GET',))
def getStations(request):
    Stations = Station.objects.all()
    x = []
    for i, c in enumerate(Stations):
        y={}
        y['id'] = c.id
        y['station_name'] = c.station_name
        y['latitude'] = c.station_latitude
        y['longitude'] = c.station_longitude
        if(y):
            x.append(y)
    return HttpResponse(json.dumps(x), content_type='application/json')

@api_view(('GET',))
def getCurrentStations(request,id):
    bike = Bike.objects.filter(id =id ).get()
    #station = Station.objects.filter(id = bike.station_id).get()
    y={}
    y['bike_id'] = bike.id
    y['station_id'] = bike.station_id
    return HttpResponse(json.dumps(y), content_type='application/json')

@api_view(('GET',))
def getDefectiveReports(request,operator_id):
    report = defectiveness_report.objects.filter(operator_id = operator_id ).all()
    x = []
    for i, c in enumerate(report):
        y={}
        y['id'] = c.id
        y['time'] = c.report_datetime.__str__()
        if(y):
            x.append(y)
    return HttpResponse(json.dumps(x), content_type='application/json')

def viewReports(request,operator_id):
    context={"operator_id":operator_id}
    return render(request,'operatorMe.html',context)
