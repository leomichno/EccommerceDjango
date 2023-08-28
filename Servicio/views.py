from django.shortcuts import render, HttpResponse
from Servicio.models import Servicio
# Create your views here.

def servicio(request):
    servicios=Servicio.objects.all()
    return render(request,"servicio/servicio.html",{"servicios":servicios})