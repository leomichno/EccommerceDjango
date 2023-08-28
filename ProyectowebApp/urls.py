from django.urls import path
from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.inicio,name="Ini"),
    path("tienda",views.tienda,name="Tie"),
    path("contacto",views.contacto,name="Con"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)