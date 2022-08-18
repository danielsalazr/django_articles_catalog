from django.urls import path
from .views import (
    lista_articulos, 
    creacion, 
    create, 
    buscar,
    busqueda)
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [
    path('articulos/',lista_articulos, name='articulos' ),
    path('articulos/crear/',creacion, name='creacion' ),
    path('articulos/create/',create, name='create' ),
    path('articulos/buscar/',buscar, name='buscar' ),
    path('articulos/busqueda/',busqueda, name='busqueda' ),

    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
