from django.shortcuts import render, HttpResponse
from blog.models import Post
# Create your views here.


def blog(request):
    pos1=Post.objects.all()
    return render(request,"blog/blog.html",{"Postbusqueda":pos1})
