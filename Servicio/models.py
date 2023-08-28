from django.db import models

# Create your models here.
class Servicio (models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Imagen=models.ImageField(upload_to='Proyectoweb/media/servicio')
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
    def __str__(self) -> str:
        return self.Titulo