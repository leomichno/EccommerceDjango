from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("Created","Update")

admin.site.register(Servicio,ServicioAdmin)