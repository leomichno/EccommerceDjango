from django.contrib import admin
from .models import Categoriablog,Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("Created","Update")
    

class PostAdming(admin.ModelAdmin):
    readonly_fields=("Created","Update")
    
    
admin.site.register(Categoriablog, CategoriaAdmin)

admin.site.register(Post, PostAdming)