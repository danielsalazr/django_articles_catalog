from django.urls import path
from .views import (
    lista_articulos, 
    creacion, 
    create, 
    buscar,
    busqueda,
    TableArticulos,
)



urlpatterns = [
    # path('',lista_articulos, name='articulos' ),
    path('',TableArticulos.as_view(), name='articulos' ),
    path('lista_articulos/',lista_articulos, name='lista_articulos' ),
    path('crear/',creacion, name='creacion' ),
    path('create/',create, name='create' ),
    path('buscar/',buscar, name='buscar' ),
    path('busqueda/',busqueda, name='busqueda' ),

    

] 
