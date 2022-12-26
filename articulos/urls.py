from django.urls import path
from .views import (
    lista_articulos, 
    creacion, 
    create, 
    buscar,
    busqueda
)



urlpatterns = [
    path('',lista_articulos, name='articulos' ),
    path('crear/',creacion, name='creacion' ),
    path('create/',create, name='create' ),
    path('buscar/',buscar, name='buscar' ),
    path('busqueda/',busqueda, name='busqueda' ),

    

] 
