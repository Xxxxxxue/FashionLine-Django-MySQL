# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User
import os
from FashionLine import settings


class Categorias(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idtipocad = models.ForeignKey('Tipocategoria', db_column='idTipoCad', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    def getCat(self):
        cad = self.categoria.replace('ñ','n')
        return cad.replace(' ','-')

    class Meta:
        ordering = ['id']
        db_table = 'categorias'


class Cestas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fcreacion = models.DateTimeField(db_column='Fcreacion', blank=True, null=True)  # Field name made lowercase.
    fultimo = models.DateTimeField(db_column='Fultimo', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idestados = models.ForeignKey('Estados', db_column='idEstados', blank=True, null=True, on_delete=models.SET_NULL)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'cestas'


class Clientecategoria(models.Model):
    idcliente = models.ForeignKey('Clientes', db_column='idCliente',  on_delete=models.CASCADE)  # Field name made lowercase.
    idcategoria = models.OneToOneField(Categorias, db_column='idCategoria', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'clientecategoria'
        unique_together = (('idcliente', 'idcategoria'),)


class Clienteimagen(models.Model):
    idcliente = models.ForeignKey('Clientes', db_column='idCliente', on_delete=models.CASCADE)  # Field name made lowercase.
    idimagen = models.OneToOneField('Imagenes', db_column='idImagen',primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'clienteimagen'
        unique_together = (('idcliente', 'idimagen'),)


class Clientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='empresa', max_length=100, blank=True, null=True)  # Field name made lowercase
    cif = models.CharField(db_column='CIF', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=24, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='descripcion', blank=True, null=True)
    icon = models.ImageField(db_column='icon', upload_to='icon',  null=True)
    idusuario = models.ForeignKey(User, db_column='idUsuario', blank=True, null=True, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        try:
            dir = str(self.icon)
            dir = dir[1:]
            dir = dir.replace('/','\\')
            os.remove(os.path.join(settings.BASE_DIR, dir))

        except(FileNotFoundError):
            print("no existe archivo")

    def getImagen(self):
        imagenList = []
        for i in self.clienteimagen_set.all():
            img = i.idimagen
            if img not in imagenList:
                imagenList.append(img)
        return imagenList

    def getCategoria(self):
        cadList = []
        for i in self.clientecategoria_set.all():
            cad = i.idcategoria
            if cad not in cadList:
                cadList.append(cad)
        return cadList


    class Meta:
        ordering = ['id']
        db_table = 'clientes'


class Colores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    color = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'colores'


class Direcciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=145, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cp = models.IntegerField(db_column='CPorta', blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=45, blank=True, null=True)  # Field name made lowercase.
    elegido= models.BooleanField(db_column='elegido', default=False)  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, db_column='idCliente', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'direcciones'


class Disenocategoria(models.Model):
    idcategoria = models.OneToOneField(Categorias, db_column='idCategoria',primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    iddiseno = models.ForeignKey('Disenos', db_column='idDiseno', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenocategoria'
        unique_together = (('iddiseno', 'idcategoria'),)


class Disenocolor(models.Model):
    iddiseno = models.ForeignKey('Disenos', db_column='idDiseno',  on_delete=models.CASCADE)  # Field name made lowercase.
    idcolor = models.OneToOneField(Colores, db_column='idColor', primary_key=True,on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenocolor'
        unique_together = (('iddiseno', 'idcolor'),)


class Disenoimagen(models.Model):
    iddiseno = models.ForeignKey('Disenos', db_column='idDiseno', on_delete=models.CASCADE)  # Field name made lowercase.
    idimagen = models.OneToOneField('Imagenes', db_column='idImagen', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenoimagen'
        unique_together = (('iddiseno', 'idimagen'),)


class Disenos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idusuario = models.ForeignKey(User, db_column='idUsuario', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    def getTipo(self):
        tipo =self.disenocategoria_set.first().idcategoria.idtipocad.tipo
        return tipo.replace('ñ','n')

    def getCategoria(self):
        cad = self.disenocategoria_set.first().idcategoria.categoria
        return cad.replace('ñ','n')

    def getImagen(self):
        imagenList = []
        for i in self.disenoimagen_set.all():
            img = i.idimagen
            if img not in imagenList:
                imagenList.append(img)
        return imagenList

    def getColor(self):
        colorList = []
        for c in self.disenocolor_set.all():
            color = c.idcolor
            if color not in colorList:
                colorList.append(color)
        return colorList

    def getTalla(self):
        tallaList = []
        for t in self.disenotalla_set.all():
            talla = t.idtalla
            if talla not in tallaList:
                tallaList.append(talla)
        return tallaList

    def getGusto(self,u):
        gusto = self.gustodiseno_set.filter(idusuario=u).gusta
        print(gusto)
        return gusto

    class Meta:
        ordering = ['id']
        db_table = 'disenos'


class Disenosexo(models.Model):
    iddiseno = models.OneToOneField(Disenos, db_column='idDiseno', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idsexo = models.ForeignKey('Sexos', db_column='idSexo', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenosexo'
        unique_together = (('iddiseno', 'idsexo'),)


class Disenotalla(models.Model):
    iddiseno = models.ForeignKey(Disenos, db_column='idDiseno', on_delete=models.CASCADE)  # Field name made lowercase.
    idtalla = models.OneToOneField('Tallas', db_column='idTalla', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenotalla'
        unique_together = (('iddiseno', 'idtalla'),)


class Disenovalora(models.Model):
    iddiseno = models.OneToOneField(Disenos, db_column='idDiseno', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', on_delete=models.CASCADE)  # Field name made lowercase.
    idvaloracion = models.ForeignKey('Valoraciones', db_column='idValoracion', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'disenovalora'
        unique_together = (('iddiseno', 'idusuario'),)


class Estados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'estados'


class Gustodiseno(models.Model):
    iddiseno = models.OneToOneField(Disenos, db_column='idDiseno',  primary_key=True,on_delete=models.CASCADE)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', on_delete=models.CASCADE)  # Field name made lowercase.
    gusta = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'gustodiseno'
        unique_together = (('iddiseno', 'idusuario'),)


class Imagenes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    def delete(self, *args, **kwargs):
        try:
            dir = str(self.imagen)
            dir = dir[1:]
            dir = dir.replace('/','\\')
            os.remove(os.path.join(settings.BASE_DIR, dir))
            super().delete(*args, **kwargs)

        except(FileNotFoundError):
            print("no existe archivo")

    class Meta:
        ordering = ['id']
        db_table = 'imagenes'


class Iva(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'iva'


class Lineacesta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', db_column='idProducto', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idcesta = models.ForeignKey(Cestas, db_column='idCesta', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idpromocion = models.ForeignKey('Promociones', db_column='idPromocion', blank=True, null=True, on_delete=models.SET_NULL)  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, db_column='idEstado', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'lineacesta'


class Mensajes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idsala = models.ForeignKey('Salas', db_column='idSala', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    mensaje = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idtipomensaje = models.ForeignKey('Tipomensaje', db_column='idTipoMensaje', blank=True, null=True, on_delete=models.SET_NULL)  # Field name made lowercase.
    url = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'mensajes'


class Productocategoria(models.Model):
    idcategoria = models.OneToOneField(Categorias, db_column='idCategoria', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', db_column='idProducto', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productocategoria'
        unique_together = (('idcategoria', 'idproducto'),)


class Productoimagen(models.Model):
    idproducto = models.ForeignKey('Productos', db_column='idProducto',  on_delete=models.CASCADE)  # Field name made lowercase.
    idimagen = models.OneToOneField(Imagenes, db_column='idImagen', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productoimagen'
        unique_together = (('idproducto', 'idimagen'),)


class Productos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='nombre',max_length=45, blank=True, null=True)
    descripcion = models.TextField(db_column='descripcion',blank=True, null=True)
    referencia = models.CharField(db_column='referencia',max_length=45, blank=True, null=True)
    precio = models.DecimalField(db_column='precio',max_digits=10, decimal_places=2, blank=True, null=True)
    coste = models.DecimalField(db_column='coste',max_digits=10, decimal_places=2, blank=True, null=True)
    oferta = models.DecimalField(db_column='oferta',max_digits=10, decimal_places=2, blank=True, null=True)
    precioactual = models.DecimalField(db_column='precioactual',max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(db_column='fecha',blank=True, null=True)
    cantidad = models.IntegerField(db_column='cantidad',blank=True, null=True)
    idiva = models.ForeignKey(Iva, db_column='idIVA', blank=True, null=True, on_delete=models.SET_NULL)  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, db_column='idEstado', blank=True, null=True, on_delete=models.SET_NULL)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    def getTipo(self):
        tipo = self.productocategoria_set.first().idcategoria.idtipocad.tipo
        return tipo.replace('ñ','n')

    def getCategoria(self):
        cad = self.productocategoria_set.first().idcategoria.categoria
        return cad.replace('ñ','n')

    def getImagen(self):
        imagenList = []
        for i in self.productoimagen_set.all():
            img = i.idimagen
            if img not in imagenList:
                imagenList.append(img)
        return imagenList

    def getColor(self):
        colorList = []
        for c in self.productocolor_set.all():
            color = c.idcolor
            if color not in colorList:
                colorList.append(color)
        return colorList

    def getTalla(self):
        tallaList = []
        for t in self.productotalla_set.all():
            talla = t.idtalla
            if talla not in tallaList:
                tallaList.append(talla)
        return tallaList

    class Meta:
        ordering = ['id']
        db_table = 'productos'

class Productotalla(models.Model):
    idproducto = models.ForeignKey(Productos, db_column='idProducto', on_delete=models.CASCADE)  # Field name made lowercase.
    idtalla = models.OneToOneField('Tallas', db_column='idTalla', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productotalla'
        unique_together = (('idproducto', 'idtalla'),)

class Productocolor(models.Model):
    idproducto = models.ForeignKey('Productos', db_column='idProducto',  on_delete=models.CASCADE)  # Field name made lowercase.
    idcolor = models.OneToOneField(Colores, db_column='idColor', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productocolor'
        unique_together = (('idproducto', 'idcolor'),)


class Productosexo(models.Model):
    idproducto = models.OneToOneField(Productos, db_column='idProducto', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idsexo = models.ForeignKey('Sexos', db_column='idSexo', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productosexo'
        unique_together = (('idproducto', 'idsexo'),)


class Productovalora(models.Model):
    idproducto = models.OneToOneField(Productos, db_column='idProducto', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', on_delete=models.CASCADE)  # Field name made lowercase.
    idvaloracion = models.ForeignKey('Valoraciones', db_column='idValoracion', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'productovalora'
        unique_together = (('idproducto', 'idusuario'),)


class Promociones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    finicio = models.DateTimeField(db_column='Finicio', blank=True, null=True)  # Field name made lowercase.
    ffin = models.DateTimeField(db_column='Ffin', blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(db_column='imagen', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['id']
        db_table = 'promociones'


class Salas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'salas'


class Salausuario(models.Model):
    idsala = models.OneToOneField(Salas, db_column='idSala', primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idUsuario', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'salausuario'
        unique_together = (('idsala', 'idusuario'),)


class Sexos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'sexos'


class Tallas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    talla = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tallas'


class Tipocategoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tipocategoria'


class Tipomensaje(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tipomensaje'


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=50)
    tipousuario = models.IntegerField(db_column='tipoUsuario', default=0 )  # Field name made lowercase.
    idclientes = models.ForeignKey(Clientes, db_column='idClientes', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return "( " + str(self.id) + " ) - " + self.usuario

    class Meta:
        ordering = ['id']
        db_table = 'usuarios'



class Valoraciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    valoracion = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']
        db_table = 'valoraciones'
