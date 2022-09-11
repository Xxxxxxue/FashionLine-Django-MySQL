from rest_framework import serializers
from general import models


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagenes
        fields = [
              'nombre',
              'imagen'
            ]