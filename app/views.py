from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def Insert_Topic(request):
    ETFO=TopicForm
    d={'ETFO':ETFO}

    if request.method=="POST":
        ETDO=TopicForm(request.POST)
        if ETDO.is_valid():
            ETDO.save()
            return HttpResponse(' Data inserted into Topics')
    return render(request,'Insert_Topic.html',d)


def Insert_Webpage(request):
    EWFO=WebpageForms
    d={'EWFO':EWFO}

    if request.method=='POST':
        EWDO=WebpageForms(request.POST)
        if EWDO.is_valid():
            EWDO.save()
            return HttpResponse(' Data inserted into Webpage')

    return render(request,'Insert_Webpage.html',d) 


def Insert_AccessRecord(request):
    EAFO=AccessRecordForms
    d={'EAFO':EAFO}
    if request.method=='POST':
        EADO=AccessRecordForms(request.POST)
        if EADO.is_valid():
            EADO.save()
            return HttpResponse(' Data inserted into Accessrecords')

    return render(request,'Insert_AccessRecord.html',d)