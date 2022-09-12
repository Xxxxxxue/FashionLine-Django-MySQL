from rest_framework import generics
from flutter import serializer
from general import models
from django.utils import timezone
from rest_framework.schemas import AutoSchema
from rest_framework.compat import coreapi
from django.contrib import auth
from django.contrib.auth.models import User, Group


# variables globales para navigation y filtro
tipocad = models.Tipocategoria.objects.all()
categorias = models.Categorias.objects.all()
color = models.Colores.objects.all()
talla =  models.Tallas.objects.all()
valoracion = models.Valoraciones.objects.all()
sexos = models.Sexos.objects.all()


class home(generics.ListCreateAPIView):
    fecha = timezone.now()
    promo = models.Promociones.objects.filter(ffin__gte=fecha)
    imagenes = models.Imagenes.objects.filter(nombre='slider')

    slider = imagenes
    if (promo):
        for p in promo:
            slider = []
            slider.append(p.imagen)
            print(p.imagen)
        if (len(slider) < 2):
            slider.extend(imagenes)

    print(slider)
    slider.reverse()

    queryset = slider
    print(queryset)
    serializer_class = serializer.ImagenSerializer


class productos(generics.ListCreateAPIView):
    queryset = models.Productos.objects.all()
    serializer_class = serializer.ProductoSerializer

class disenos(generics.ListCreateAPIView):
    queryset = models.Disenos.objects.all()
    serializer_class = serializer.DisenoSerializer

class agendas(generics.ListCreateAPIView):
    s = ['diseñadores','talleres','importadores','empresas de venta mayor']
    cad = categorias.filter(categoria__in=s)
    clientes = models.Clientecategoria.objects.filter(idcategoria__in=cad)
    print(cad, clientes)
    cli = []
    for i in clientes:
        if i.idcliente not in cli:
            cli.append(i.idcliente)

    queryset = cli
    serializer_class = serializer.ClienteSerializer






