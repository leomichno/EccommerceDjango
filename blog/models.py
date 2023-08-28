from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoriablog(models.Model):
    Nombre=models.CharField(max_length=50)
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'categoriablog'
        verbose_name_plural = 'categoriablogs'
        
    def __str__(self) -> str:
        return self.Nombre
    
class Post(models.Model):
    Titulo=models.CharField(max_length=50)
    Contenido=models.CharField(max_length=50)
    Imagen=models.ImageField(upload_to='Proyectoweb/media/blog',null=True,blank=True)
    auto=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoriablog)
    
    Created=models.DateTimeField(auto_now_add=True)
    Update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def __str__(self) -> str:
        return self.Titulo