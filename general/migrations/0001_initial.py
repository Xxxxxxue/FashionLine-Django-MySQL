# Generated by Django 4.0.5 on 2022-09-11 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cestas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fcreacion', models.DateTimeField(blank=True, db_column='Fcreacion', null=True)),
                ('fultimo', models.DateTimeField(blank=True, db_column='Fultimo', null=True)),
            ],
            options={
                'db_table': 'cestas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=45, null=True)),
                ('apellidos', models.CharField(blank=True, db_column='Apellidos', max_length=150, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=15, null=True)),
                ('empresa', models.CharField(blank=True, db_column='empresa', max_length=100, null=True)),
                ('cif', models.CharField(blank=True, db_column='CIF', max_length=9, null=True)),
                ('cuenta', models.CharField(blank=True, db_column='Cuenta', max_length=24, null=True)),
                ('descripcion', models.TextField(blank=True, db_column='descripcion', null=True)),
                ('icon', models.ImageField(db_column='icon', default='/static/imagenes/user_icon.svg', null=True, upload_to='icon')),
                ('token', models.UUIDField(blank=True, editable=False, null=True)),
                ('idusuario', models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'clientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'colores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Disenos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('idusuario', models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'disenos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, db_column='Estado', max_length=50, null=True)),
            ],
            options={
                'db_table': 'estados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('imagen', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'imagenes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('iva', models.DecimalField(blank=True, db_column='IVA', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'iva',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=45, null=True)),
                ('descripcion', models.TextField(blank=True, db_column='descripcion', null=True)),
                ('referencia', models.CharField(blank=True, db_column='referencia', max_length=45, null=True)),
                ('precio', models.DecimalField(blank=True, db_column='precio', decimal_places=2, max_digits=10, null=True)),
                ('coste', models.DecimalField(blank=True, db_column='coste', decimal_places=2, max_digits=10, null=True)),
                ('oferta', models.DecimalField(blank=True, db_column='oferta', decimal_places=2, max_digits=10, null=True)),
                ('precioactual', models.DecimalField(blank=True, db_column='precioactual', decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='fecha', null=True)),
                ('cantidad', models.IntegerField(blank=True, db_column='cantidad', null=True)),
                ('idestado', models.ForeignKey(blank=True, db_column='idEstado', null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.estados')),
                ('idiva', models.ForeignKey(blank=True, db_column='idIVA', null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.iva')),
                ('idusuario', models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Salas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'salas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sexos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'sexos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tallas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('talla', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tallas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipocategoria',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipocategoria',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Valoraciones',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('valoracion', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'valoraciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=50)),
                ('tipousuario', models.IntegerField(db_column='tipoUsuario', default=0)),
                ('idclientes', models.ForeignKey(blank=True, db_column='idClientes', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.clientes')),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('descuento', models.DecimalField(blank=True, db_column='Descuento', decimal_places=2, max_digits=10, null=True)),
                ('descripcion', models.TextField(blank=True, db_column='Descripcion', null=True)),
                ('finicio', models.DateTimeField(blank=True, db_column='Finicio', null=True)),
                ('ffin', models.DateTimeField(blank=True, db_column='Ffin', null=True)),
                ('imagen', models.ForeignKey(blank=True, db_column='imagen', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.imagenes')),
            ],
            options={
                'db_table': 'promociones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('estadomensaje', models.CharField(blank=True, db_column='EstadoMensaje', max_length=45, null=True)),
                ('estadomensajeuser', models.CharField(blank=True, db_column='EstadoMensajeUser', max_length=45, null=True)),
                ('idsala', models.ForeignKey(blank=True, db_column='idSala', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.salas')),
                ('idusuario', models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mensajes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lineacesta',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('preciounitario', models.DecimalField(blank=True, db_column='PrecioUnitario', decimal_places=2, max_digits=10, null=True)),
                ('cantidad', models.IntegerField(blank=True, db_column='Cantidad', null=True)),
                ('total', models.DecimalField(blank=True, db_column='Total', decimal_places=2, max_digits=10, null=True)),
                ('color', models.CharField(blank=True, db_column='color', max_length=45, null=True)),
                ('talla', models.CharField(blank=True, db_column='talla', max_length=45, null=True)),
                ('idcesta', models.ForeignKey(blank=True, db_column='idCesta', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.cestas')),
                ('idestado', models.ForeignKey(blank=True, db_column='idEstado', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.estados')),
                ('idproducto', models.ForeignKey(blank=True, db_column='idProducto', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
                ('idpromocion', models.ForeignKey(blank=True, db_column='idPromocion', null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.promociones')),
            ],
            options={
                'db_table': 'lineacesta',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('calle', models.CharField(blank=True, db_column='Calle', max_length=145, null=True)),
                ('localidad', models.CharField(blank=True, db_column='Localidad', max_length=45, null=True)),
                ('cp', models.IntegerField(blank=True, db_column='CPorta', null=True)),
                ('provincia', models.CharField(blank=True, db_column='Provincia', max_length=45, null=True)),
                ('pais', models.CharField(blank=True, db_column='Pais', max_length=45, null=True)),
                ('elegido', models.BooleanField(db_column='elegido', default=False)),
                ('idcliente', models.ForeignKey(blank=True, db_column='idCliente', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.clientes')),
            ],
            options={
                'db_table': 'direcciones',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='cestas',
            name='idestado',
            field=models.ForeignKey(blank=True, db_column='idEstados', null=True, on_delete=django.db.models.deletion.SET_NULL, to='general.estados'),
        ),
        migrations.AddField(
            model_name='cestas',
            name='idusuario',
            field=models.ForeignKey(blank=True, db_column='idUsuario', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('categoria', models.CharField(blank=True, db_column='Categoria', max_length=45, null=True)),
                ('idtipocad', models.ForeignKey(blank=True, db_column='idTipoCad', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.tipocategoria')),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Productovalora',
            fields=[
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('idproducto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
                ('idvaloracion', models.ForeignKey(blank=True, db_column='idValoracion', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.valoraciones')),
            ],
            options={
                'db_table': 'productovalora',
                'unique_together': {('idproducto', 'idusuario')},
            },
        ),
        migrations.CreateModel(
            name='Disenovalora',
            fields=[
                ('idusuario', models.OneToOneField(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('iddiseno', models.ForeignKey(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, to='general.disenos')),
                ('idvaloracion', models.ForeignKey(blank=True, db_column='idValoracion', null=True, on_delete=django.db.models.deletion.CASCADE, to='general.valoraciones')),
            ],
            options={
                'db_table': 'disenovalora',
                'unique_together': {('iddiseno', 'idusuario')},
            },
        ),
        migrations.CreateModel(
            name='Salausuario',
            fields=[
                ('idsala', models.OneToOneField(db_column='idSala', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.salas')),
                ('idusuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'salausuario',
                'unique_together': {('idsala', 'idusuario')},
            },
        ),
        migrations.CreateModel(
            name='Productotalla',
            fields=[
                ('idtalla', models.OneToOneField(db_column='idTalla', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.tallas')),
                ('idproducto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
            ],
            options={
                'db_table': 'productotalla',
                'unique_together': {('idproducto', 'idtalla')},
            },
        ),
        migrations.CreateModel(
            name='Productosexo',
            fields=[
                ('idproducto', models.OneToOneField(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.productos')),
                ('idsexo', models.ForeignKey(db_column='idSexo', on_delete=django.db.models.deletion.CASCADE, to='general.sexos')),
            ],
            options={
                'db_table': 'productosexo',
                'unique_together': {('idproducto', 'idsexo')},
            },
        ),
        migrations.CreateModel(
            name='Productoimagen',
            fields=[
                ('idimagen', models.OneToOneField(db_column='idImagen', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.imagenes')),
                ('idproducto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
            ],
            options={
                'db_table': 'productoimagen',
                'unique_together': {('idproducto', 'idimagen')},
            },
        ),
        migrations.CreateModel(
            name='Productocolor',
            fields=[
                ('idcolor', models.OneToOneField(db_column='idColor', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.colores')),
                ('idproducto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
            ],
            options={
                'db_table': 'productocolor',
                'unique_together': {('idproducto', 'idcolor')},
            },
        ),
        migrations.CreateModel(
            name='Productocategoria',
            fields=[
                ('idcategoria', models.OneToOneField(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.categorias')),
                ('idproducto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='general.productos')),
            ],
            options={
                'db_table': 'productocategoria',
                'unique_together': {('idcategoria', 'idproducto')},
            },
        ),
        migrations.CreateModel(
            name='Gustodiseno',
            fields=[
                ('iddiseno', models.OneToOneField(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.disenos')),
                ('gusta', models.IntegerField(blank=True, null=True)),
                ('idusuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gustodiseno',
                'unique_together': {('iddiseno', 'idusuario')},
            },
        ),
        migrations.CreateModel(
            name='Disenotalla',
            fields=[
                ('idtalla', models.OneToOneField(db_column='idTalla', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.tallas')),
                ('iddiseno', models.ForeignKey(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, to='general.disenos')),
            ],
            options={
                'db_table': 'disenotalla',
                'unique_together': {('iddiseno', 'idtalla')},
            },
        ),
        migrations.CreateModel(
            name='Disenosexo',
            fields=[
                ('iddiseno', models.OneToOneField(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.disenos')),
                ('idsexo', models.ForeignKey(db_column='idSexo', on_delete=django.db.models.deletion.CASCADE, to='general.sexos')),
            ],
            options={
                'db_table': 'disenosexo',
                'unique_together': {('iddiseno', 'idsexo')},
            },
        ),
        migrations.CreateModel(
            name='Disenoimagen',
            fields=[
                ('idimagen', models.OneToOneField(db_column='idImagen', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.imagenes')),
                ('iddiseno', models.ForeignKey(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, to='general.disenos')),
            ],
            options={
                'db_table': 'disenoimagen',
                'unique_together': {('iddiseno', 'idimagen')},
            },
        ),
        migrations.CreateModel(
            name='Disenocolor',
            fields=[
                ('idcolor', models.OneToOneField(db_column='idColor', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.colores')),
                ('iddiseno', models.ForeignKey(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, to='general.disenos')),
            ],
            options={
                'db_table': 'disenocolor',
                'unique_together': {('iddiseno', 'idcolor')},
            },
        ),
        migrations.CreateModel(
            name='Disenocategoria',
            fields=[
                ('idcategoria', models.OneToOneField(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.categorias')),
                ('iddiseno', models.ForeignKey(db_column='idDiseno', on_delete=django.db.models.deletion.CASCADE, to='general.disenos')),
            ],
            options={
                'db_table': 'disenocategoria',
                'unique_together': {('iddiseno', 'idcategoria')},
            },
        ),
        migrations.CreateModel(
            name='Clienteimagen',
            fields=[
                ('idimagen', models.OneToOneField(db_column='idImagen', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.imagenes')),
                ('idcliente', models.ForeignKey(db_column='idCliente', on_delete=django.db.models.deletion.CASCADE, to='general.clientes')),
            ],
            options={
                'db_table': 'clienteimagen',
                'unique_together': {('idcliente', 'idimagen')},
            },
        ),
        migrations.CreateModel(
            name='Clientecategoria',
            fields=[
                ('idcategoria', models.OneToOneField(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='general.categorias')),
                ('idcliente', models.ForeignKey(db_column='idCliente', on_delete=django.db.models.deletion.CASCADE, to='general.clientes')),
            ],
            options={
                'db_table': 'clientecategoria',
                'unique_together': {('idcliente', 'idcategoria')},
            },
        ),
    ]
