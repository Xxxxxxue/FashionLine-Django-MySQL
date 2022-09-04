from django.shortcuts import render, redirect
from general import models, pagination
from django.utils import timezone
from django.contrib import auth
from gestion_user.upload import handle_uploaded_file
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

# variables globales para navigation y filtro

tipocad = models.Tipocategoria.objects.all()
categorias = models.Categorias.objects.all()
color = models.Colores.objects.all()
talla =  models.Tallas.objects.all()
valoracion = models.Valoraciones.objects.all()
sexos = models.Sexos.objects.all()


#img
def getImg(request, id):
    img = models.Imagenes.objects.get(id=id)
    return render(request,"paginas/img.html", {'img':img})

# PERFIL
def perfil(request, id):

    # datos a sacar: cliente,
    # categorias de cliente -- saca de funcion getCategoria
    # imagenes de cliente  -- saca de funcion
    cliente = models.Clientes.objects.filter(idusuario=request.user).first()
    direcciones = models.Direcciones.objects.filter(idcliente=cliente)
    localidad = direcciones.filter(elegido=1).first()
    grupo = request.user.groups.first()
    print(grupo.name)

    return render(request, "paginas/user_perfil.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                        'categorias': categorias, 'cliente': cliente,
                                                            'direcciones': direcciones,'localidad': localidad,'grupo':grupo.name})


def perfil_edit(request, id):

    # Icono
    icon = request.FILES.get('icon')
    if icon:
        user_cli = models.Clientes.objects.filter(idusuario=request.user).first()
        if(user_cli.icon != '/static/imagenes/user_icon.svg'):
            user_cli.delete()
        print(request.FILES)
        url_icon = 'static/imagenes/icon/'+icon.name
        handle_uploaded_file(icon, url_icon)
        models.Clientes.objects.filter(idusuario=request.user).update(icon='/' + url_icon)
    # Datos
    cli = models.Clientes
    cli.nombre = request.POST.get("nombre")
    cli.apellidos = request.POST.get("apellidos")
    cli.email = request.POST.get("email")
    cli.telefono = request.POST.get("telefono")
    cli.descripcion = request.POST.get("descripcion")
    cli.empresa = request.POST.get("empresa")
    cli.cif = request.POST.get("cif")
    cli.cuenta = request.POST.get("cuenta")

    id_dir =request.POST.get("dir-select")
    user_cli = models.Clientes.objects.filter(idusuario=request.user).first()
    print(cli.descripcion)
    #imagenes
    slider = request.FILES.getlist('slider')
    print(request.FILES)
    if slider:
        for s in slider:
            url_slider = 'static/imagenes/slider/'+s.name
            handle_uploaded_file(s, url_slider)
            models.Imagenes.objects.get_or_create(nombre=s.name,imagen='/'+url_slider)
            img = models.Imagenes.objects.last()
            models.Clienteimagen.objects.get_or_create(idcliente=user_cli, idimagen=img)

    # update
    models.Clientes.objects.filter(idusuario=request.user).update(
        nombre=cli.nombre, apellidos=cli.apellidos, email=cli.email, telefono=cli.telefono, empresa=cli.empresa,
        cuenta=cli.cuenta, cif=cli.cif, descripcion=cli.descripcion)
    models.Direcciones.objects.filter(elegido='True').update(elegido='False')
    models.Direcciones.objects.filter(id=id_dir).update(elegido='True')

    print("cambiado datos del perfil")
    ruta = '/user/profile/' + str(request.user.id)

    return redirect(ruta)

def perfil_dir(request, id):

    dir = models.Direcciones
    dir.calle = request.POST.get("calle")
    dir.localidad = request.POST.get("localidad")
    dir.provincia = request.POST.get("provincia")
    dir.pais = request.POST.get("pais")
    dir.cp = request.POST.get("cp")
    dir.elegido = request.POST.get("elegido")

    if(dir.elegido == 'True'):
        models.Direcciones.objects.filter(elegido='True').update(elegido='False')

    if (id == 0):
        cli = models.Clientes.objects.filter(idusuario=request.user).get()
        print(cli)
        models.Direcciones.objects.get_or_create(calle=dir.calle,localidad=dir.localidad,provincia=dir.provincia,pais=dir.pais,cp=dir.cp,elegido=dir.elegido,idcliente=cli)
    else:
        models.Direcciones.objects.filter(id=id).update(calle=dir.calle,localidad=dir.localidad,provincia=dir.provincia,pais=dir.pais,cp=dir.cp,elegido=dir.elegido)

    print("cambiado la direccion")

    ruta = '/user/profile/' + str(request.user.id)
    return redirect(ruta)

def perfil_dir_delete(request, id):

    models.Direcciones.objects.filter(id=id).delete()

    print("eliminado la direccion")

    ruta = '/user/profile/' + str(request.user.id)
    return redirect(ruta)

def img_delete(request, id):

    img = models.Imagenes.objects.get(id=id)
    img.delete()

    print("eliminado slider/imagen" + request.path)
    ruta = '/user/profile/' + str(request.user.id)
    return redirect(ruta)

#########################################################################################################################
# PEDIDOS
def pedidos(request):
    return render(request, "paginas/user_pedidos.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

def pedidos_detalle(request, id):
    return render(request, "paginas/user_pedidos_detalle.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})


#########################################################################################################################
# MIS DISENOS
def misdisenos(request, sexo,page):

    # sacando productos de sexo
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    gustos = []
    for t in psexo:
        try:
            x = models.Gustodiseno.objects.filter(idusuario=request.user).filter(iddiseno=t.iddiseno).get()
            gustos.append(x)
        except models.Gustodiseno.DoesNotExist:
            print('none')
        if (t.iddiseno.idusuario == request.user):
            productos.append(t.iddiseno)
    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    grupo = request.user.groups.first()
    if (grupo.name == 'diseñador' and len(productos) == 0 ):
        user_cli = models.Clientes.objects.filter(idusuario=request.user).get()
        filtercad = categorias.get(categoria='diseñadores')
        models.Clientecategoria.objects.filter(idcliente=user_cli).filter(idcategoria=filtercad).delete()
        g = Group.objects.get(name='diseñador')
        request.user.groups.remove(g)
        g = Group.objects.get(name='none')
        request.user.groups.add(g)

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'user/mydisign'

    return render(request, "paginas/user_disenos.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'], 'paginacion_url': url, 'grupo': grupo.name,'gustos':gustos})

def misdisenos_edit(request,sexo,id,page):
    # post  datos diseno
    p = models.Disenos
    p.nombre = request.POST.get('nombre')
    p.descripcion = request.POST.get('descripcion')
    p.precio = request.POST.get('precio')
    p.fecha = timezone.now()

    producto = []
    if (id == 0):
        models.Disenos.objects.get_or_create(nombre=p.nombre, descripcion=p.descripcion, precio=p.precio,fecha=p.fecha, idusuario=request.user)
        producto = models.Disenos.objects.last()
    else:
        models.Disenos.objects.filter(id=id).update(nombre=p.nombre, descripcion=p.descripcion, precio=p.precio,fecha=p.fecha)
        producto = models.Disenos.objects.get(id=id)

    idsexo = sexos.get(tipo=request.POST.get('sexo'))
    if(not models.Disenosexo.objects.filter(iddiseno=producto)):
        models.Disenosexo.objects.get_or_create(iddiseno=producto, idsexo=idsexo)
    else:
        models.Disenosexo.objects.filter(iddiseno=producto).update(idsexo=idsexo)

    # categorias
    idcad = request.POST.get('categoria')
    if idcad:
        pcad = models.Categorias.objects.get(categoria=idcad)
        models.Disenocategoria.objects.get_or_create(iddiseno=producto, idcategoria=pcad)
    # imagenes
    idimg = request.FILES.getlist('images')
    if idimg:
        for s in idimg:
            url_img = 'static/imagenes/disenos/' + s.name
            handle_uploaded_file(s, url_img)
            models.Imagenes.objects.get_or_create(nombre=s.name, imagen='/' + url_img)
            img = models.Imagenes.objects.last()
            models.Disenoimagen.objects.get_or_create(iddiseno=producto, idimagen=img)
    # color
    pcolor = request.POST.getlist('color')
    if(pcolor):
        for co in pcolor:
            pcol = models.Colores.objects.get(color=co)
            models.Disenocolor.objects.get_or_create(iddiseno=producto, idcolor=pcol)

    ptalla = request.POST.getlist('talla')
    if (ptalla):
        for t in ptalla:
            pt = models.Tallas.objects.get(talla=t)
            models.Disenotalla.objects.get_or_create(iddiseno=producto, idtalla=pt)


    print("edit diseño")
    ruta = '/user/mydisign/' + sexo + '/' + str(page)
    return redirect(ruta)

def misdisenos_delete(request,sexo,page,id):

    imgs = models.Disenos.objects.filter(id=id).get().getImagen()
    for img in imgs:
        img.delete()

    models.Disenos.objects.filter(id=id).delete()

    print("eliminado diseño -- " + str(page))
    ruta = '/user/mydisign/'+sexo+'/1'
    return redirect(ruta)


#########################################################################################################################
# MIS PRODUCTOS
def misproductos(request,sexo, page):

    # sacando productos
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if(t.idproducto.idusuario == request.user):
            productos.append(t.idproducto)

    # sacar una imagen para cada productos
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]

    datos_pagination = pagination.pagination(productos, page)
    url = 'user/myproduct'

    grupo = request.user.groups.first()

    return render(request, "paginas/user_productos.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url, 'grupo': grupo.name})

def misproductos_edit(request,sexo,id,page):

    #post  datos producto
    p = models.Productos
    p.nombre = request.POST.get('nombre')
    p.descripcion = request.POST.get('descripcion')
    p.referencia = request.POST.get('referencia')
    p.precio = request.POST.get('precio')
    p.coste  = request.POST.get('coste')
    p.oferta = request.POST.get('oferta')
    p.precioactual = request.POST.get('pactual')
    p.cantidad = request.POST.get('cantidad')
    i = request.POST.get('iva')
    idiva = models.Iva.objects.filter(iva=i).get()
    idestado = models.Estados.objects.filter(estado=request.POST.get('estado')).get()
    p.fecha = timezone.now()
    producto = []

    if (id == 0):
        models.Productos.objects.get_or_create(nombre=p.nombre,descripcion=p.descripcion,referencia=p.referencia,precio=p.precio,
                                               coste=p.coste,oferta=p.oferta,precioactual=p.precioactual,fecha=p.fecha,idiva=idiva,
                                               idusuario=request.user,cantidad=p.cantidad,idestado=idestado)
        producto = models.Productos.objects.last()
    else:
        models.Productos.objects.filter(id=id).update(nombre=p.nombre, descripcion=p.descripcion, referencia=p.referencia,
                                               precio=p.precio,cantidad=p.cantidad,idestado=p.idestado,
                                               coste=p.coste, oferta=p.oferta, precioactual=p.precioactual,
                                               fecha=p.fecha, idiva=p.idiva)
        producto = models.Productos.objects.get(id=id)

    sex = sexos.get(tipo=request.POST.get('sex'))
    if (not models.Productosexo.objects.filter(idproducto=producto)):
        models.Productosexo.objects.get_or_create(idproducto=producto, idsexo=sex)
    else:
        models.Productosexo.objects.filter(idproducto=producto).update(idsexo=sex)
    #categorias
    idcad = request.POST.get('categoriass')
    if idcad:
        pcad = models.Categorias.objects.get(categoria=idcad)
        models.Productocategoria.objects.get_or_create(idproducto=producto, idcategoria=pcad)
    # imagenes
    idimg = request.FILES.getlist('images')
    if idimg:
        for s in idimg:
            url_img = 'static/imagenes/productos/' + s.name
            handle_uploaded_file(s, url_img)
            models.Imagenes.objects.get_or_create(nombre=s.name, imagen='/' + url_img)
            img = models.Imagenes.objects.last()
            models.Productoimagen.objects.get_or_create(idproducto=producto, idimagen=img)
    #cotenido
    pcolor = request.POST.getlist('color')
    if(pcolor):
        for co in pcolor:
            pco = models.Colores.objects.get(color=co)
            models.Productocolor.objects.get_or_create(idproducto=producto, idcolor=pco)
    ptalla = request.POST.getlist('talla')
    if (ptalla):
        for t in ptalla:
            pt = models.Tallas.objects.get(talla=t)
            models.Productotalla.objects.get_or_create(idproducto=producto, idtalla=pt)


    print("edit productos")
    ruta = '/user/myproduct/' + sexo + '/'+str(page)
    return redirect(ruta)

def misproductos_delete(request,sexo,id,page):

    imgs = models.Productos.objects.filter(id=id).get().getImagen()
    for img in imgs:
        img.delete()

    models.Productos.objects.filter(id=id).delete()

    print("eliminado producto")
    ruta = '/user/myproduct/'+sexo+'/1'
    return redirect(ruta)


#########################################################################################################################
# MIS FAVORITOS
def favoritos(request, sexo, page):
    # sacando productos de sexo
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    gustos = []
    for t in psexo:
        try:
            x = models.Gustodiseno.objects.filter(idusuario=request.user).filter(iddiseno=t.iddiseno).get()
            if (x.gusta == 1):
                gustos.append(x)
                print(x.iddiseno,x.gusta)
                productos.append(t.iddiseno)
        except models.Gustodiseno.DoesNotExist:
            print('none')

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    grupo = request.user.groups.first()
    print(grupo.name)

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'user/favorites'

    return render(request, "paginas/user_favoritos.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                         'valoracion': valoracion, 'tipo': tipocad,
                                                         'categorias': categorias, 'imagenes': imagenes,
                                                         'productos': datos_pagination['page_productos'],
                                                         'pagelist': datos_pagination['pageList'],
                                                         'num': datos_pagination['num'], 'paginacion_url': url,
                                                         'grupo': grupo.name, 'gustos': gustos})

def favoritos_delete(request,sexo, id):

    iddiseno = models.Disenos.objects.filter(id=id).get()
    models.Gustodiseno.objects.filter(iddiseno=iddiseno).filter(idusuario=request.user).delete()

    print("eliminado favoritos")
    ruta = '/user/favorites/'+ sexo + '/1'
    return redirect(ruta)

def megusta(request,id):

    d = models.Disenos.objects.filter(id=id).get()
    models.Gustodiseno.objects.get_or_create(idusuario=request.user,iddiseno=d,gusta=True)

    print(request)
    return redirect('/user/favorites/mujer/1')

#########################################################################################################################
# CAMBIAR CONTRASEÑA
def changeKey(request):

    if request.method == 'GET':
        return render(request, "paginas/user_cambiarKey.html", {'tipo': tipocad, 'categorias': categorias,})

    print(request.user.password)
    password = request.POST.get('Password1')
    u = User.objects.filter(id=request.user.id).get()
    u.set_password(password)
    u.save()
    print(u.password)
    user = auth.authenticate(username=request.user.username, password=password)
    if user:
        auth.login(request, user)
    return redirect('/')
