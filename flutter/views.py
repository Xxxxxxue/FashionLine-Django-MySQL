from django.utils import timezone
from rest_framework import generics
from flutter import serializer
from general import models

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

