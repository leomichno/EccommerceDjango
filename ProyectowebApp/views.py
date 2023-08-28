from django.shortcuts import render, HttpResponse


# Create your views here.

def inicio(request):
    
    return render(request,"ProyectowebApp/home.html")

def tienda(request):
    
    return render(request,"ProyectowebApp/Tienda.html")

def contacto(request):
    
    return render(request,"ProyectowebApp/Contacto.html")