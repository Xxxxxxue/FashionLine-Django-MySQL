from django.db.models import Q
from django.shortcuts import render, redirect
from general import models, pagination, ObtenerValoracion
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# variables globales para navigation y filtro
tipocad = models.Tipocategoria.objects.all()
categorias = models.Categorias.objects.all()
color = models.Colores.objects.all()
talla =  models.Tallas.objects.all()
valoracion = models.Valoraciones.objects.all()
sexos = models.Sexos.objects.all()
ependiente= models.Estados.objects.filter(estado='pendiente').get()


# PAGINAS PRINCIPALES
########################################################################################################################

# HOME
def home(request):
    # PROBAR LAS FUNCIONES DE BASE DE DATO
    # Tipocategoria.objects.create(id=1,tipo = "ropa")
    # Tipocategoria.objects.create(tipo="pantalón")
    # tipocad = Tipocategoria.objects.get(tipo="ropa")
    # Categorias.objects.create(categoria="camiseta",idtipocad=tipocad)
    ####################################################################################

    text = ' <div class="carousel-caption d-none d-md-block"> \
            <h5>WELCOME TO FASHIONLINE!</h5>\
            <p>Get your fashion, choose you style!</p> \
            </div>'
    # slider de los imagenes promociones e imagenes subidos directamente en tabla imagen
    fecha = timezone.now()
    promo = models.Promociones.objects.filter(ffin__gte=fecha)
    imagenes = models.Imagenes.objects.filter(nombre='slider')

    slider = imagenes

    if(promo):
        for p in promo:
            slider=[]
            slider.append(p.imagen)
            print(p.imagen)
        if(len(slider) < 2):
            slider.extend(imagenes)

    print(slider)
    slider.reverse()
    # print(promo[0].ffin, fecha)
    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name


    return render(request, "paginas/home.html", {'slider': slider, 'tipo': tipocad, 'categorias':categorias, 'text': text, 'idcesta': idcesta,'grupo':grupo })



########################################################################################################################

# LOGIN
def login(request):
    # get
    if request.method == "GET":
        return render(request, "paginas/login.html", {'tipo': tipocad, 'categorias':categorias})

    # post
    username = request.POST.get('usuario')
    password = request.POST.get('password')
    # u = auth.authenticate(username=username, password=password)
    # proteger password
    # md5 = hashlib.md5()
    # md5.update(password.encode())
    # pass_md5 = md5.hexdigest()
    # u = models.Usuarios.objects.filter(usuario=username, contrasena=pass_md5).get()
    user = auth.authenticate(username=username, password=password)
    if user:
        # num = str(u.id)
        # no funciona session debido a que necesita la tabla session en bbdd
        # request.session['user'] = u
        # return redirect('/user/profile/'+num)
        auth.login(request, user)
        return redirect("/")


    error_msg = 'Usuario o Contraseña está incorrecto.'
    return render(request, "paginas/login.html", {'tipo': tipocad, 'categorias':categorias, 'error_msg': error_msg})

# REGISTRAR
def registro(request):
    # get
    if request.method == "GET":
        return render(request, "paginas/registro.html", {'tipo': tipocad, 'categorias':categorias})

    # post
    username = request.POST.get('usuario')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    u = User.objects.filter(username=username)
    # si esta ya registrado?
    if u:
        msg = 'Usuario ya está registrado.'
        return render(request, "paginas/registro.html", {'tipo': tipocad, 'categorias':categorias, 'msg':msg})

    # proteger password
    # md5 = hashlib.md5()
    # md5.update(password.encode())
    # pass_md5 = md5.hexdigest()
    # user = models.Usuarios.objects.create(usuario=username, contrasena=pass_md5)
    # cliente = models.Clientes.objects.create(nombre=nombre, apellidos=apellido, email=username)
    # models.Usuarios.objects.filter(usuario=username).update(idclientes=cliente)

    # crear usuario
    user = User.objects.create_user(username=username, password=password)
    cliente = models.Clientes.objects.create(nombre=nombre, apellidos=apellido, email=username,idusuario=user)
    print(user.id)
    # registrado, inicia sesion
    if user:
        g = Group.objects.get(name='none')
        user.groups.add(g)
        models.Cestas.objects.create(idusuario=user,idestado=ependiente,fcreacion=timezone.now())
        id = str(user.id)
        auth.login(request, user)
        return HttpResponseRedirect('/user/profile/'+id)

    return redirect(registro)

# LOGOUT
def salir(request):
    # forma llamando session
    # if 'user' in request.session:
    #     del request.session['user']
    #
    # return redirect(home)
    ppp = auth.logout(request)
    print(ppp)  # None
    return redirect("/")



########################################################################################################################

# PRODUCTO
def producto(request,sexo,page):
    # sacar database para el filto : variables grobales
    # color, talla, precio(no), valoracion, tipos y categorias para filtro
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    #sacando productos
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        productos.append(t.idproducto)

    # sacar una imagen para cada productos
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]
        # imagen = models.Imagenes.objects.filter(id=img)
        # print(imagenes.count(imagenes[index]))
        # print(imagenes[index].idimagen.imagen)

    # print(imagenes,imagenes[0].idproducto.id,imagenes[1].idproducto.id)
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product'
    tip = 'product'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo, 'idcesta': idcesta,'grupo':grupo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,'tip':tip,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_filtro_tipo(request,sexo,tipo,page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    # sacando productos de tipo x
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    # print("Tipo de producto: ",producto[1].getTipo())
    productos=[]
    for t in psexo:
        if(t.idproducto.getTipo()==tipo.replace('-',' ')):
            productos.append(t.idproducto)

    # sacar una imagen para cada producto
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]


    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo
    tip = 'product'
    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad, 'idcesta':idcesta,
                                                     'categorias': categorias,'imagenes': imagenes, 'sexos':sexos, 'sexo': sexo,'grupo':grupo,
                                                     'productos': datos_pagination['page_productos'], 'tip': tip,
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],'paginacion_url': url})

def producto_filtro_categoria(request,tipo,sexo,categoria,page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    # sacando productos de tipo x
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    # print("Tipo de producto: ",producto[1].getTipo())
    productos = []
    for t in psexo:
        if (t.idproducto.getCategoria() == categoria.replace('ñ','n')):
            productos.append(t.idproducto)

    # sacar una imagen para cada producto
    imagenes = []
    for p in productos:
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + categoria
    tip = 'product'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo, 'idcesta': idcesta,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,'grupo':grupo,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url,'tip': tip})

def producto_detalle(request, id):

    # post
    if request.method == 'POST':
        # usuario que esta en acceso
        u = models.Usuarios.objects.get(id=5)
        p = models.Productos.objects.get(id=id)
        ruta = '/product_detail/' + str(id)
        # si ya has valorado
        u_valorado = models.Productovalora.objects.filter(Q(idproducto=p) & Q(idusuario=u))
        if (u_valorado):
            return redirect(ruta)

        # si no
        v = request.POST.get("estrellas")
        v_aux = models.Valoraciones.objects.get(valoracion=v)
        models.Productovalora.objects.get_or_create(idproducto=p, idusuario=u, idvaloracion=v_aux)
        return redirect(ruta)

    # saca producto -> id
    # sacar tabla productocontenido, para obtener tallas y colores
    # sacar imagenes
    # get
    productos = models.Productos.objects.filter(id=id).get()
    print(productos.getImagen())
    totalcolor = len(productos.getColor())
    total = len(productos.getTalla())
    cli = models.Clientes.objects.filter(idusuario=productos.idusuario).get()
    tip = "producto"


    # o sacamos talla y color por aqui, o por model.py que he creado unos metodos
    # contenido = models.Productocontenido.objects.filter(idproducto=productos)
    # imagenes = models.Productoimagen.objects.filter(idproducto=productos)
    # imagenes = productos.getImagen()
    # valoracion media
    valoraciones = models.Productovalora.objects.filter(idproducto=productos)
    listValora = {}
    media = 0
    if(valoraciones):
        listValora = ObtenerValoracion.SacarValoracion(valoraciones)
        media = listValora['media']
        del listValora['media']

    idcesta = []
    grupo = []
    # contactar
    misala = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

        try:
            misala = models.Salausuario.objects.filter(idusuario=productos.idusuario)
            for m in misala:
                n = models.Salausuario.objects.filter(idsala=m.idsala).filter(idusuario=request.user).get()
                if (n):
                    misala = n
            if not misala:
                models.Salas.objects.create(fecha=timezone.now())
                misala = models.Salas.objects.last()
                models.Salausuario.objects.create(idsala=misala, idusuario=productos.idusuario)
                models.Salausuario.objects.create(idsala=misala, idusuario=request.user)
        except models.Salausuario.DoesNotExist:
            None

    return render(request, "paginas/producto_detalle.html", {'color': color, 'talla': talla, 'idcesta': idcesta,'grupo': grupo,'cli':cli,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'total': total,'totalcolor':totalcolor,
                                                     'categorias': categorias, 'producto': productos, 'tip': tip, 'misala': misala,
                                                     'media': media, 'valorado': valoraciones.count(), 'listvalora': listValora
                                                     })


def producto_user(request,iduser,sexo,page):
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    cli = models.Clientes.objects.filter(id=iduser).get()
    productos = []
    for t in psexo:
        if(t.idproducto.idusuario.id==cli.idusuario.id):
            productos.append(t.idproducto)

    # sacar una imagen para cada productos
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]
        # imagen = models.Imagenes.objects.filter(id=img)
        # print(imagenes.count(imagenes[index]))
        # print(imagenes[index].idimagen.imagen)

    # print(imagenes,imagenes[0].idproducto.id,imagenes[1].idproducto.id)
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'productcli/' + str(iduser)
    tip = 'product'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo, 'grupo': grupo.name,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'idcesta': idcesta,
                                                     'categorias': categorias, 'tip': tip,
                                                     'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})


########################################################################################################################
# DISENO
def diseno(request, sexo, page):
    # database filtro
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)

    # sacando productos de sexo
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        productos.append(t.iddiseno)

    #imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # user name

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign'
    tip = 'diseno' \
          ''
    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,'grupo':grupo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'idcesta': idcesta,
                                                     'categorias': categorias,'imagenes': imagenes, 'tip': tip,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'], 'paginacion_url': url})

def diseno_filtro_tipo(request, sexo, page, tipo):
    # database filtro
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    # sacando productos de sexo
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if(t.iddiseno.getTipo() == tipo.replace('-',' ')):
            productos.append(t.iddiseno)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo
    tip = 'diseno'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name
    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,'grupo':grupo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'tip':diseno,
                                                     'categorias': categorias, 'idcesta': idcesta,
                                                     'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def diseno_filtro_categoria(request, sexo, page, tipo, categoria):
    # database
    # color, talla, precio(no), valoracion, tipos y categorias
    # sacando productos de sexo
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        # porque categoria esta cambiada
        if (t.iddiseno.getCategoria() == categoria.replace('-',' ')):
            # print(t.iddiseno.getCategoria(), categoria)
            productos.append(t.iddiseno)
    # print(productos)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo + '/' + categoria
    tip = 'diseno'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'grupo':grupo,
                                                     'categorias': categorias, 'idcesta': idcesta,
                                                     'imagenes': imagenes, 'tip':tip,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def diseno_detalle(request, id):
    # post
    if request.method == 'POST':
        # usuario que esta en acceso
        u = models.Usuarios.objects.get(id=5)
        p = models.Disenos.objects.get(id=id)
        ruta = '/disign_detail/' + str(id)
        # si ya has valorado
        u_valorado = models.Disenovalora.objects.filter(Q(iddiseno=p) & Q(idusuario=u))
        if (u_valorado):
            return redirect(ruta)

        # si no
        v = request.POST.get("estrellas")
        v_aux = models.Valoraciones.objects.get(valoracion=v)
        models.Disenovalora.objects.get_or_create(iddiseno=p, idusuario=u, idvaloracion=v_aux)
        return redirect(ruta)

    # saca producto -> id
    # sacar tabla productocontenido, para obtener tallas y colores
    # sacar imagenes
    # get
    productos = models.Disenos.objects.filter(id=id).get()
    print(productos.getImagen())
    cli = models.Clientes.objects.filter(idusuario=productos.idusuario).get()
    tip ="diseno"


    valoraciones = models.Disenovalora.objects.filter(iddiseno=productos)
    listValora = {}
    media = 0
    if (valoraciones):
        listValora = ObtenerValoracion.SacarValoracion(valoraciones)
        media = listValora['media']
        del listValora['media']

    idcesta = []
    grupo = []
    # contactar
    misala = []
    # me gusta
    g = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

        try:
            misala = models.Salausuario.objects.filter(idusuario=productos.idusuario)
            for m in misala:
                n = models.Salausuario.objects.filter(idsala=m.idsala).filter(idusuario=request.user).get()
                if (n):
                    misala = n
            if not misala:
                models.Salas.objects.create(fecha=timezone.now())
                misala = models.Salas.objects.last()
                models.Salausuario.objects.create(idsala=misala, idusuario=productos.idusuario)
                models.Salausuario.objects.create(idsala=misala, idusuario=request.user)
        except models.Salausuario.DoesNotExist:
            None

        try:
            g = models.Gustodiseno.objects.filter(iddiseno=productos).filter(idusuario=request.user).get()
        except models.Gustodiseno.DoesNotExist:
            print('none')
    return render(request, "paginas/diseno_detalle.html", {'color': color, 'talla': talla, 'idcesta': idcesta, 'grupo':grupo,
                                                             'valoracion': valoracion, 'tipo': tipocad,'g':g, 'cli':cli, 'tip': tip,
                                                             'categorias': categorias, 'producto': productos, 'misala': misala,
                                                             'media': media, 'valorado': valoraciones.count(),
                                                             'listvalora': listValora
                                                             })


def diseno_user(request, iduser, sexo, page):
    # database filtro
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    print(sexo)
    # sacando productos de sexo
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)

    cli = models.Clientes.objects.filter(id=iduser).get()
    productos = []
    for t in psexo:
        if( t.iddiseno.idusuario.id==cli.idusuario.id ):
            productos.append(t.iddiseno)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # user name

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disigncli/' + str(iduser)
    tip = 'diseno'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name
    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo, 'grupo':grupo,
                                                   'valoracion': valoracion, 'tipo': tipocad, 'idcesta': idcesta,
                                                   'categorias': categorias, 'imagenes': imagenes, 'tip':tip,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'], 'paginacion_url': url})


########################################################################################################################
# AGENDA
def agenda(request, page):
    # database
    pcliente = models.Clientecategoria.objects.all()
    productos = []
    for p in pcliente:
        productos.append(p.idcliente)

    imagenes = []
    for p in productos:
        imagenes += models.Clienteimagen.objects.filter(idcliente=p)
    print(imagenes)

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'contact'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/agenda.html", { 'tipo': tipocad, 'categorias': categorias, 'grupo':grupo,
                                                     'imagenes': imagenes, 'idcesta':idcesta,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def agenda_categoria(request, page, categoria):
    # database
    #sacar objeto categoria que ha pasado por parametro
    cat = []
    for c in categorias:
        if c.getCat() == categoria:
            cat = c
    #cliente relacionado
    pcliente = models.Clientecategoria.objects.filter(idcategoria=cat)
    productos = []
    for p in pcliente:
        productos.append(p.idcliente)

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'contact/' + categoria
    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name
    return render(request, "paginas/agenda.html", {'color': color, 'talla': talla, 'grupo':grupo,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias, 'idcesta': idcesta,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})

def agenda_detalle(request, id):
    # database
    # sacar informacion de este cliente id
    pcliente = models.Clientes.objects.get(id=id)
    direccion= []
    try:
        direccion = models.Direcciones.objects.filter(idcliente=pcliente).filter(elegido=1).get()
    except models.Direcciones.DoesNotExist:
        None

    cad = models.Clientecategoria.objects.filter(idcliente=pcliente)
    # sacar los productos y disenos relacionados
    productos = models.Productos.objects.filter(idusuario=pcliente.idusuario) [:4]
    disenos = []
    for c in cad:
        if c.idcategoria.categoria == 'diseñadores':
            disenos = models.Disenos.objects.filter(idusuario=pcliente.idusuario)[:4]

    # sacar imagenes relacionados
    # imagen = pcliente.getImagen()
    fotos = models.Clienteimagen.objects.filter(idcliente=pcliente)
    slider = []
    for f in fotos:
        slider.append(f.idimagen)

    # imagenes productos
    imgp = []
    for p in productos:
        imgp += models.Productoimagen.objects.filter(idproducto=p)[:1]
    # imagenes disenos
    imgd = []
    for d in disenos:
        imgd += models.Disenoimagen.objects.filter(iddiseno=d)[:1]

        # contactar
    misala = []
    try:
        misala = models.Salausuario.objects.filter(idusuario=pcliente.idusuario)
        for m in misala:
            n = models.Salausuario.objects.filter(idsala=m.idsala).filter(idusuario=request.user).get()
            if (n):
                misala = n
        if not misala:
            models.Salas.objects.create(fecha=timezone.now())
            misala = models.Salas.objects.last()
            models.Salausuario.objects.create(idsala=misala, idusuario=pcliente.idusuario)
            models.Salausuario.objects.create(idsala=misala, idusuario=request.user)
    except models.Salausuario.DoesNotExist:
        None

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/agenda_detalle.html", {'tipo': tipocad, 'categorias': categorias, 'grupo':grupo, 'misala': misala,
                                                            'slider': slider,'productos': productos, 'idcesta': idcesta,
                                                           'disenos': disenos, 'cliente': pcliente, 'categoria': cad,
                                                           'imgp':imgp, 'imgd': imgd, 'direccion': direccion})


# MENSAJERIA
def mensajeria(request, page):
    # database
    # cli = models.Clientes.objects.get(idusuario=request.user)
    clis = []
    productos = models.Salausuario.objects.filter(idusuario=request.user)
    for s in productos:
        try:
            s_user = models.Salausuario.objects.filter(idsala=s.idsala).exclude(idusuario=s.idusuario).get()
            clis.append(s_user)
        except models.Salausuario.DoesNotExist:
            None

    print('msg:',clis)
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'message'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/mensajeria.html", {'color': color, 'talla': talla,'grupo':grupo,
                                                   'valoracion': valoracion, 'tipo': tipocad, 'idcesta': idcesta,
                                                   'categorias': categorias, 'clis': clis,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})


def mensajeria_detalle(request, iduser, id):

    misala = models.Salas.objects.filter(id=id).get()

    models.Mensajes.objects.filter(idsala=misala).exclude(idusuario=request.user).update(estadomensaje='leido')
    msgs = models.Mensajes.objects.filter(idsala=misala).order_by('fecha')

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/mensajeria_detalle.html", {'color': color, 'talla': talla, 'grupo': grupo,
                                                       'valoracion': valoracion, 'tipo': tipocad, 'idcesta': idcesta,
                                                       'categorias': categorias, 'msgs': msgs,'misala': misala})

def mensajeria_submit(request,id):

    m = request.POST.get("mensaje")
    fecha = timezone.now()
    sala = models.Salas.objects.filter(id=id).get()
    models.Mensajes.objects.create(fecha=fecha,mensaje=m,estadomensajeuser='leido',estadomensaje='enviado',idusuario=request.user,idsala=sala)

    return redirect('/message_chat/' + str(request.user.id) + '/' + str(id))

########################################################################################################################

# CESTA
def cesta(request,id):
    cesta = models.Cestas.objects.get(id=id)
    count = cesta.getLinea().count()
    grupo = request.user.groups.first()
    return render(request, "paginas/cesta.html", {'color': color, 'talla': talla, 'grupo': grupo.name, 'idcesta':cesta,
                                                                 'valoracion': valoracion, 'tipo': tipocad,
                                                                 'categorias': categorias, 'cesta': cesta,
                                                                 'count': count})

def lineacesta(request,id):

    can = request.POST.get("cantidad")
    cl = request.POST.get("cl")
    tl = request.POST.get("tl")
    finicio = timezone.now()

    p = models.Productos.objects.get(id=id)
    t = int(can) * float(p.precioactual)
    micesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
    if not micesta:
        models.Cestas.objects.create(idusuario=request.user,idestado=ependiente,fcreacion=finicio)
        micesta = models.Cestas.objects.last()

    models.Lineacesta.objects.get_or_create(idproducto=p,idcesta=micesta,preciounitario=p.precioactual,cantidad=can,
                                            total=t,color=cl,talla=tl,idestado=ependiente)

    return redirect('/cart/'+ str(micesta.id))


def pagado(request,id):
    # estado a pagado
    cesta = models.Cestas.objects.get(id=id)
    idcesta = []
    if(len(cesta.getLinea())>0):
        es = models.Estados.objects.get(estado='pagado')
        cesta.update(idestado=es,fultimo=timezone.now())
        models.Cestas.objects.create(idusuario=request.user, idestado=ependiente, fcreacion=timezone.now())
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()

        grupo = request.user.groups.first()
        return render(request, "paginas/pagado.html", {'color': color, 'talla': talla, 'grupo': grupo.name,
                                                      'valoracion': valoracion, 'tipo': tipocad,
                                                      'categorias': categorias,'idcesta': idcesta})
    return redirect('/cart/'+str(id))


########################################################################################################################
def search(request,valor,sexo,page):
    # productos = models.Clientes.objects.all()
    # imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))
    # Paginacion : llamar metodo pagination

    txt = ''
    if request.method == 'POST':
        txt = request.POST.get("busqueda")

    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    # sacando productos de sexo
    s = sexos.get(tipo=sexo)

    txt = valor
    print(txt)
    productos = models.Productos.objects.filter(nombre__icontains=txt).order_by('-fecha')
    disenos = models.Disenos.objects.filter(nombre__icontains=txt).order_by('-fecha')

    # imagenes
    dimagenes = []
    ds = []
    pd = models.Productosexo.objects.filter(idsexo=s)
    pd1 = models.Disenosexo.objects.filter(idsexo=s)
    prod = []
    for t in pd:
        prod.append(t.idproducto)
    prod1 = []
    for t in pd1:
        prod1.append(t.iddiseno)

    for p in disenos:
        dimagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]
        if (p in prod):
            ds.append(p)
    disenos = ds
    # imagenes
    pimagenes = []
    ps = []
    for p in productos:
        pimagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]
        if (p in prod):
            ps.append(p)
    productos = ps


    p_pagination = {'page_productos': ''}
    d_pagination = {'page_productos': ''}
    num = 1
    pagelist = range(0)
    if(len(disenos) <= len(productos)):
        p_pagination = pagination.pagination(productos, page)
        pagelist = p_pagination['pageList']
        num = p_pagination['num']
    else:
        d_pagination = pagination.pagination(disenos, page)
        pagelist = d_pagination['pageList']
        num = d_pagination['num']
    print(len(p_pagination))


    url = 'search/' + valor
    tip = 'search'

    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, "paginas/search.html", {'color': color, 'talla': talla, 'grupo':grupo, 'tip': tip,
                                                   'valoracion': valoracion, 'tipo': tipocad,'idcesta': idcesta,
                                                   'categorias': categorias,'disenos': d_pagination['page_productos'],
                                                   'dimg':dimagenes, 'imagenes': pimagenes, 'sexo': sexo,
                                                   'productos': p_pagination['page_productos'],
                                                   'pagelist': pagelist,
                                                   'num': num,
                                                   'paginacion_url': url})



#########################################################################################################################
def filtro(request,tip,fc,ft,fv,fcad,fp,sexo,page):


    productos = []
    disenos = []
    card = []
    s = []
    prender = ""
    #filtrar todos
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo = sexo[:2] + "ñ" + sexo[3:]
    # sacando productos de sexo
    s = sexos.get(tipo=sexo)

    if (tip == 'product'):
        productos = models.Productos.objects.all().order_by("-fecha")
        prender = "paginas/producto.html"
    elif (tip == 'myproduct'):
        productos = models.Productos.objects.filter(idusuario=request.user).order_by("-fecha")
        prender = "paginas/user_prodctos.html"
    elif (tip == 'diseno'):
        productos = models.Disenos.objects.all().order_by("-fecha")
        prender = "paginas/diseno.html"
    elif (tip == 'mydiseno'):
        productos = models.Disenos.objects.filter(idusuario=request.user).order_by("-fecha")
        prender = "paginas/user_disenos.html"
    elif(tip == 'fav'):
        productos = models.Gustodiseno.objects.filter(idusuario=request.user)
        for i in productos:
            card.append(i.iddiseno)
        productos = card
        prender = "paginas/user_favoritos.html"

    else:
        productos = models.Productos.objects.all().order_by("-fecha")
        disenos = models.Disenos.objects.all().order_by("-fecha")
        prender = "paginas/search.html"

    if(fc == 'none' and ft == 'none' and fcad == 'none' and fv == 0 and fp == 'none'):
        None

    else:
        #color
        if(fc != 'none'):
            card = []
            fcolor = fc.split('-')
            fidcolor = color.filter(id__in=fcolor)
            print(fidcolor)
            for p in productos:
                if any(c in p.getColor() for c in fidcolor):
                    print(1)
                    card.append(p)
                    print(p.getColor())
            productos = card

            if(tip == 'search'):
                card = []
                for p in disenos:
                    if any(c in p.getColor() for c in fidcolor):
                        print(1)
                        card.append(p)
                        print(p.getColor())
                disenos = card

        # talla
        if (ft != 'none'):
            card = []
            ftalla = ft.split('-')
            fidtalla = talla.filter(talla__in=ftalla)
            print(fidtalla)
            for p in productos:
                if any(c in p.getTalla() for c in fidtalla):
                    print(1)
                    card.append(p)
                    print(p.getTalla())
            productos = card

            if (tip == 'search'):
                card = []
                for p in disenos:
                    if any(c in p.getTalla() for c in fidtalla):
                        print(1)
                        card.append(p)
                        print(p.getTalla())
                disenos = card

        # valoracion
        if (fv != '0'):
            card = []
            fval = fv.split('-')
            fidvalora = valoracion.filter(valoracion__in=fval)
            print(fidvalora)
            for p in productos:

                valoraciones = p.getValoracion()
                print('valoracion: ', len(valoraciones))
                listValora = {}
                media = 0
                if (valoraciones):
                    listValora = ObtenerValoracion.SacarValoracion(valoraciones)
                    media = listValora['media']
                    #despues de sacar media
                    m = valoracion.get(valoracion=media)
                    if ( m in fidvalora):
                        card.append(p)
                        print('media:',m,p)
            productos = card

            if (tip == 'search'):
                card = []
                for p in disenos:

                    valoraciones = p.getValoracion()
                    print('valoracion: ', len(valoraciones))
                    listValora = {}
                    media = 0
                    if (valoraciones):
                        listValora = ObtenerValoracion.SacarValoracion(valoraciones)
                        media = listValora['media']
                        # despues de sacar media
                        m = valoracion.get(valoracion=media)
                        if (m in fidvalora):
                            card.append(p)
                            print('media:', m, p)
                disenos = card

        # categoria
        if (fcad != 'none'):
            card = []
            fca = fcad.split('-')
            fidcad = categorias.filter(id__in=fca)
            print(fidcad)
            for p in productos:
                if any(c in p.getAllCategoria() for c in fidcad):
                    print(1)
                    card.append(p)
                    print(p.getAllCategoria())
            productos = card

            if (tip == 'search'):
                card = []
                for p in disenos:
                    if any(c in p.getAllCategoria() for c in fidcad):
                        print(1)
                        card.append(p)
                        print(p.getAllCategoria())
                disenos = card

        # precio
        if (fp != 'none'):
            card = []
            fprice = fp.split('-')
            print(fprice)
            for p in productos:
                if(p.precio >= float(fprice[0]) and p.precio <= float( fprice[1])):
                    card.append(p)
            print(card)
            productos = card

            if (tip == 'search'):
                card = []
                for p in disenos:
                    if (p.precio >= float(fprice[0]) and p.precio <= float(fprice[1])):
                        card.append(p)
                disenos = card


    # sacar una imagen para cada producto
    pimagenes = []
    dimagenes = []
    if (tip == 'product' or tip == 'myproduct'):
        pd = models.Productosexo.objects.filter(idsexo=s)
        prod = []
        for t in pd:
            prod.append(t.idproducto)

    if (tip == 'diseno' or tip == 'mydiseno' or tip == 'fav'):
        pd = models.Disenosexo.objects.filter(idsexo=s)
        prod = []
        for t in pd:
            prod.append(t.iddiseno)
    else:
        pd = models.Productosexo.objects.filter(idsexo=s)
        pd1 = models.Disenosexo.objects.filter(idsexo=s)
        prod = []
        for t in pd:
            prod.append(t.idproducto)
        prod1 = []
        for t in pd1:
            prod1.append(t.iddiseno)


    card=[]
    for p in productos:
        pimagenes.append(p.getImagenFirst())
        print(p)
        if (p in prod):
            print(0)
            print(prod)
            card.append(p)
    productos = card

    if( tip== 'search'):
        card = []
        for p in disenos:
            dimagenes.append(p.getImagenFirst())
            if (p in prod1):
                card.append(p)
        disenos = card

    p_pagination = {'page_productos': ''}
    d_pagination = {'page_productos': ''}
    num = 1
    pagelist = range(0)
    if (len(disenos) <= len(productos)):
        p_pagination = pagination.pagination(productos, page)
        pagelist = p_pagination['pageList']
        num = p_pagination['num']
    else:
        d_pagination = pagination.pagination(disenos, page)
        pagelist = d_pagination['pageList']
        num = d_pagination['num']
    print(len(p_pagination))

    url = 'filtro/'+tip+'/'+fc+'/'+ft+'/'+fv+'/'+fcad+'/'+fp


    idcesta = []
    grupo = []
    if request.user.username:
        idcesta = models.Cestas.objects.filter(idusuario=request.user).filter(idestado=ependiente).get()
        grupo = request.user.groups.first()
        grupo = grupo.name

    return render(request, prender, {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad, 'idcesta':idcesta,
                                                     'categorias': categorias,'imagenes': pimagenes, 'dimg':dimagenes,'sexos':sexos, 'sexo': sexo,'grupo':grupo,
                                                     'productos': p_pagination['page_productos'], 'tip': tip, 'fcad': fcad,'fp':fp,
                                                     'pagelist': pagelist, 'fc': fc, 'ft': ft, 'fv': fv,
                                                     'num': num,'paginacion_url': url,
                                                      'disenos': d_pagination['page_productos'],})

