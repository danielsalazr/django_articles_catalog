from django.contrib import admin
from .models import  Articulos

# Register your models here.

@admin.register(Articulos)
class Articulos(admin.ModelAdmin):
    list_display = (
        'linea',
        'grupo',
        'elemento',
        'descripcion',
        'unidad',
        'imagen',
        'stock' ,
    )