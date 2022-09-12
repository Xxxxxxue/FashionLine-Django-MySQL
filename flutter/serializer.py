from rest_framework import serializers
from general import models
from django.contrib.auth.models import User, Group

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorias
        fields = [
            'id',
            'categoria',
            'idtipocad'
            ]


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sexos
        fields = [
            'id',
            'tipo'
            ]

class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tallas
        fields = [
            'id',
            'talla'
            ]


class CestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cestas
        fields = [
            'id',
            'fcreacion',
            'fultimo',
            'idusuario',
            'idestado'
            ]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = [
            'id',
            'nombre',
            'apellidos',
            'email',
            'telefono',
            'empresa',
            'cif',
            'cuenta',
            'descripcion',
            'icon',
            'idusuario',
            ]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagenes
        fields = [
            'id',
            'nombre',
            'color',
            ]
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direcciones
        fields = [
            'id',
            'calle',
            'localidad',
            'procincia',
            'pais',
            'elegido',
            'idcliente',

            ]

class DisenoColorSerializer(serializers.ModelSerializer):
    idcolor = ColorSerializer(required=True)
    class Meta:
        model = models.Disenocolor
        fields = [
            'idcolor',
            'iddiseno',
            ]

class DisenoTallaSerializer(serializers.ModelSerializer):
    idtalla = TallaSerializer(required=True)
    class Meta:
        model = models.Disenotalla
        fields = [
            'idtalla',
            'iddiseno',
            ]

class DisenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disenos
        fields = [
            #'id',
            'nombre',
            #'descripcion',
            'precio',
            #'fecha',
            #'idusuario',
            ]
    # def create(self,validated_data):
    #     c_data = validated_data.pop('colores')
    #     diseno = models.Disenos.objects.create(**validated_data)
    #     for c in c_data:
    #         models.Disenocolor.create(iddiseno=diseno, **c)
    #     return diseno


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estados
        fields = [
            'id',
            'estado'
            ]

class GustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gustodiseno
        fields = [
            'idusuario',
            'iddiseno',
            'gusta'

            ]

class IvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Iva
        fields = [
            'id',
            'iva'
            ]

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Imagenes
        fields = [
            'nombre',
            'imagen'
            ]

class LineaCestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lineacesta
        fields = [
            'id',
            'idproducto',
            'idcesta',
            'preciounitario',
            'cantidad',
            'total',
            'color',
            'talla',
            'idpromocion',
            'idestado',

            ]

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mensajes
        fields = [
            'id',
            'idusuario',
            'idsala',
            'mensaje',
            'fecha',
            'estadomensaje',
            'estadomensajeuser'

            ]

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Productos
        fields = [
            'id',
            'nombre',
            #'descripcion',
            #'referencia',
            'precio',
            #'coste',
            #'oferta',
            #'precioactual',
            #'fecha',
            #'cantidad',
            #'idiva',
            #'idestado',
            #'idusuario'
            ]

class ProductoImgSerializer(serializers.ModelSerializer):
    idimagen = ImagenSerializer(required=True)
    idproducto = ProductoSerializer()
    class Meta:
        model = models.Disenoimagen
        fields = [
            'idimagen',
            'idproducto',
            ]

class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promociones
        fields = [
            'id',
            'nombre',
            'descuento',
            'descripcion',
            'finicio',
            'ffin',
            'imagen'

            ]

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Salas
        fields = [
            'id',
            'fecha'
            ]

class SalaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Salausuario
        fields = [
            'idsala',
            'idusuario'
            ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            ]

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            ]

class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valoraciones
        fields = [
            'id',
            'valoracion',
            'nombre',
            ]

class DisenoImgSerializer(serializers.ModelSerializer):
    idimagen = ImagenSerializer(required=True)
    iddiseno = DisenoSerializer()
    class Meta:
        model = models.Disenoimagen
        fields = [
            'idimagen',
            'iddiseno',
            ]






