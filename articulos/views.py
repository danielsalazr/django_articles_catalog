#Django
from django.shortcuts import render
from django.http import HttpResponse

#Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Apps
from .models import Articulos

#Serializers
from .serializers import ArticleSerializers

#Python
from rich.console import Console
console = Console()

def creacion(request):
    return render(request, 'articulos/crearProducto.html')

def busqueda(request):
    return render(request, 'articulos/buscarProducto.html')

#obtener todo el llistado de articulos
@api_view(['GET'])
def lista_articulos(request):

    articulos = Articulos.objects.all()
    serializer = ArticleSerializers(articulos, many=True)
    print (articulos)
    console.log(serializer.data)
    print(serializer.data[0]['linea'])

    return render(request, 'articulos/listadoArticulos.html', {'items': serializer.data})
    #return Response(serializer.data)



@api_view(['POST'])
def create(request):
    serializer = ArticleSerializers( data = request.data)
    serializer.is_valid(raise_exception=True)
    #print(serializer.data)
    articulos =serializer.save()
    return Response(ArticleSerializers(articulos).data)


@api_view(['GET'])
def buscar(request):
    try:
        busqueda = str(request.query_params['descripcion'])
        #print(busqueda)
        articulo = Articulos.objects.get(descripcion__icontains=busqueda,)
        print(articulo)
        return render(request, 'articulos/resultadoBusqueda.html', {'articulo':articulo})
    except:
        return render(request, '404.html')
    #return HttpResponse("OK")