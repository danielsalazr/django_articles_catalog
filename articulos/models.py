
from django.db import models

# Create your models here.
class Articulos(models.Model):
    linea = models.IntegerField(default=0)
    grupo = models.IntegerField(default=0)
    elemento = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=50)
    unidad = models.CharField(max_length=7)
    imagen = models.ImageField(upload_to='articulos/pictures')
    stock = models.PositiveIntegerField(
        default=0,
    )
