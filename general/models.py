# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idtipocad = models.ForeignKey('Tipocategoria', models.DO_NOTHING, db_column='idTipoCad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorias'


class Cestas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fcreacion = models.DateTimeField(db_column='Fcreacion', auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    fultimo = models.DateTimeField(db_column='Fultimo', blank=True, null=True, auto_now=True )  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idestados = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstados', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cestas'


class Clientecategoria(models.Model):
    idcliente = models.OneToOneField('Clientes', models.DO_NOTHING, db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='idCategoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientecategoria'
        unique_together = (('idcliente', 'idcategoria'),)


class Clienteimagen(models.Model):
    idcliente = models.OneToOneField('Clientes', models.DO_NOTHING, db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idimagen = models.ForeignKey('Imagenes', models.DO_NOTHING, db_column='idImagen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienteimagen'
        unique_together = (('idcliente', 'idimagen'),)


class Clientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nif = models.CharField(db_column='NIF', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=24, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    name_usuario = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        ordering = ['-id']
        db_table = 'clientes'


class Colores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colores'


class Direcciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=145, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cporta = models.IntegerField(db_column='CPorta', blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'direcciones'


class Disenocategoria(models.Model):
    iddiseno = models.OneToOneField('Disenos', models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='idCategoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenocategoria'
        unique_together = (('iddiseno', 'idcategoria'),)


class Disenocolor(models.Model):
    iddiseno = models.OneToOneField('Disenos', models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idcolor = models.ForeignKey(Colores, models.DO_NOTHING, db_column='idColor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenocolor'
        unique_together = (('iddiseno', 'idcolor'),)


class Disenoimagen(models.Model):
    iddiseno = models.OneToOneField('Disenos', models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idimagen = models.ForeignKey('Imagenes', models.DO_NOTHING, db_column='idImagen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenoimagen'
        unique_together = (('iddiseno', 'idimagen'),)


class Disenos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idestado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenos'


class Disenosexo(models.Model):
    iddiseno = models.OneToOneField(Disenos, models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idsexo = models.ForeignKey('Sexos', models.DO_NOTHING, db_column='idSexo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenosexo'
        unique_together = (('iddiseno', 'idsexo'),)


class Disenotalla(models.Model):
    iddiseno = models.OneToOneField(Disenos, models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idtalla = models.ForeignKey('Tallas', models.DO_NOTHING, db_column='idTalla')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenotalla'
        unique_together = (('iddiseno', 'idtalla'),)


class Disenovalora(models.Model):
    iddiseno = models.OneToOneField(Disenos, models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idvaloracion = models.ForeignKey('Valoraciones', models.DO_NOTHING, db_column='idValoracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disenovalora'
        unique_together = (('iddiseno', 'idusuario'),)


class Estados(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estados'


class Gustodiseno(models.Model):
    iddiseno = models.OneToOneField(Disenos, models.DO_NOTHING, db_column='idDiseno', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    gusta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gustodiseno'
        unique_together = (('iddiseno', 'idusuario'),)


class Imagenes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes'


class Iva(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iva'


class Lineacesta(models.Model):
    idproducto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idcesta = models.ForeignKey(Cestas, models.DO_NOTHING, db_column='idCesta')  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    idpromocion = models.ForeignKey('Promociones', models.DO_NOTHING, db_column='idPromocion', blank=True, null=True)  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lineacesta'
        unique_together = (('idproducto', 'idcesta'),)


class Mensajes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.
    idsala = models.ForeignKey('Salas', models.DO_NOTHING, db_column='idSala', blank=True, null=True)  # Field name made lowercase.
    mensaje = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    idtipomensaje = models.ForeignKey('Tipomensaje', models.DO_NOTHING, db_column='idTipoMensaje', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensajes'


class Productocategoria(models.Model):
    idcategoria = models.OneToOneField(Categorias, models.DO_NOTHING, db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productocategoria'
        unique_together = (('idcategoria', 'idproducto'),)


class Productocolor(models.Model):
    idproducto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idcolor = models.ForeignKey(Colores, models.DO_NOTHING, db_column='idColor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productocolor'
        unique_together = (('idproducto', 'idcolor'),)


class Productoimagen(models.Model):
    idproducto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idimagen = models.ForeignKey(Imagenes, models.DO_NOTHING, db_column='idImagen')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productoimagen'
        unique_together = (('idproducto', 'idimagen'),)


class Productos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    referencia = models.CharField(max_length=45, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    coste = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precioactual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idiva = models.ForeignKey(Iva, models.DO_NOTHING, db_column='idIVA', blank=True, null=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.

    def getOneImage(self):
        return self.productoimagen_set.first().idimagen.imagen

    class Meta:
        managed = False
        ordering = ['-id']
        db_table = 'productos'


class Productosexo(models.Model):
    idproducto = models.OneToOneField(Productos, models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idsexo = models.ForeignKey('Sexos', models.DO_NOTHING, db_column='idSexo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productosexo'
        unique_together = (('idproducto', 'idsexo'),)


class Productotalla(models.Model):
    idproducto = models.OneToOneField(Productos, models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idtalla = models.ForeignKey('Tallas', models.DO_NOTHING, db_column='idTalla')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productotalla'
        unique_together = (('idproducto', 'idtalla'),)


class Productovalora(models.Model):
    idproducto = models.OneToOneField(Productos, models.DO_NOTHING, db_column='idProducto', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.
    idvaloracion = models.ForeignKey('Valoraciones', models.DO_NOTHING, db_column='idValoracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productovalora'
        unique_together = (('idproducto', 'idusuario'),)


class Promociones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    finicio = models.DateTimeField(db_column='Finicio', blank=True, null=True)  # Field name made lowercase.
    ffin = models.DateTimeField(db_column='Ffin', blank=True, null=True)  # Field name made lowercase.
    url_imagen = models.CharField(db_column='URL_imagen', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promociones'


class Salas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salas'


class Salausuario(models.Model):
    idsala = models.OneToOneField(Salas, models.DO_NOTHING, db_column='idSala', primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salausuario'
        unique_together = (('idsala', 'idusuario'),)


class Sexos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sexos'


class Tallas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    talla = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tallas'


class Tipocategoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocategoria'


class Tipomensaje(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipomensaje'


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=50)
    tipousuario = models.IntegerField(db_column='tipoUsuario')  # Field name made lowercase.
    idclientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idClientes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        ordering = ['-id']
        db_table = 'usuarios'


class Valoraciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    valoracion = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valoraciones'
