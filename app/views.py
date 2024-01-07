from django.shortcuts import render

# Create your views here.

from app.forms import*
from django.http import HttpResponse 

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is completed')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webform()
    d={'EWFO':EWFO}
    
    if request.method=='POST':
        WFDO=Webform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is completed')
        
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=Accessrecordform(request.POST)
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_accessrecord is completed')
    return render(request,'insert_accessrecord.html',d)    
