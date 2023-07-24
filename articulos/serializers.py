from rest_framework import serializers

#APP
from .models import Articulos

# Create your views here.

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulos
        #fields = '__all__'
        fields = [
            'linea',
            'grupo',
            'elemento',
            'descripcion',
            'unidad',
            # 'imagen',
            'stock',
        ]

# class ArticleSerializers(serializers.Serializer):
#     """Circle serializer"""
#     linea = serializers.IntegerField()
#     grupo = serializers.IntegerField()
#     elemento = serializers.IntegerField()
#     descripcion = serializers.CharField()
#     unidad = serializers.CharField()
#     imagen = serializers.ImageField(required=False)
#     stock = serializers.IntegerField()
    