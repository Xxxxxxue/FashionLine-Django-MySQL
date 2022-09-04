from django.db.models import Q
from django.shortcuts import render, redirect
from general import models, pagination, ObtenerValoracion
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect

# variables globales para navigation y filtro
tipocad = models.Tipocategoria.objects.all()
categorias = models.Categorias.objects.all()
color = models.Colores.objects.all()
talla =  models.Tallas.objects.all()
valoracion = models.Valoraciones.objects.all()
sexos = models.Sexos.objects.all()


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

    slider = []
    slider += imagenes
    slider += promo

    print(slider)
    # print(promo[0].ffin, fecha)

    return render(request, "paginas/home.html", {'slider': slider, 'tipo': tipocad, 'categorias':categorias, 'text': text })



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

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
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

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes, 'sexos':sexos, 'sexo': sexo,
                                                     'productos': datos_pagination['page_productos'],
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

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

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
    return render(request, "paginas/producto_detalle.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias, 'producto': productos,
                                                     'media': media, 'valorado': valoraciones.count(), 'listvalora': listValora
                                                     })


def producto_user(request,sexo,iduser,page):
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo[2] = 'ñ'
    print(sexo)
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if(t.idproducto.idusuario.idclientes.id==iduser):
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
    url = 'product/' + str(iduser)

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
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

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
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

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
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

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes,
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

    valoraciones = models.Disenovalora.objects.filter(iddiseno=productos)
    listValora = {}
    media = 0
    if (valoraciones):
        listValora = ObtenerValoracion.SacarValoracion(valoraciones)
        media = listValora['media']
        del listValora['media']
    return render(request, "paginas/diseno_detalle.html", {'color': color, 'talla': talla,
                                                             'valoracion': valoracion, 'tipo': tipocad,
                                                             'categorias': categorias, 'producto': productos,
                                                             'media': media, 'valorado': valoraciones.count(),
                                                             'listvalora': listValora
                                                             })


def diseno_user(request, sexo, iduser, page):
    # database filtro
    if (sexo == 'ninos' or sexo == 'ninas'):
        sexo[2] = 'ñ'
    print(sexo)
    # sacando productos de sexo
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if( t.iddiseno.idusuario.idclientes.id==iduser ):
            productos.append(t.iddiseno)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # user name

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + str(iduser)

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias, 'imagenes': imagenes,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'], 'paginacion_url': url})

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

    return render(request, "paginas/agenda.html", { 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes,
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

    return render(request, "paginas/agenda.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})

def agenda_detalle(request, id):
    # database
    # sacar informacion de este cliente id
    pcliente = models.Clientes.objects.get(id=id)
    print(pcliente)
    usuario = pcliente.getUser()
    print(usuario)
    direccion = models.Direcciones.objects.filter(idcliente=pcliente)[:1]
    cad = models.Clientecategoria.objects.get(idcliente=pcliente)
    # sacar los productos y disenos relacionados
    productos = models.Productos.objects.filter(idusuario=usuario) [:4]
    disenos = models.Disenos.objects.filter(idusuario=usuario)[:4]

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

    return render(request, "paginas/agenda_detalle.html", {'tipo': tipocad, 'categorias': categorias,
                                                            'slider': slider,'productos': productos,
                                                           'disenos': disenos, 'cliente': pcliente, 'categoria': cad,
                                                           'imgp':imgp, 'imgd': imgd, 'direccion': direccion})


# MENSAJERIA
def mensajeria(request, page):
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
    url = 'message'

    return render(request, "paginas/mensajeria.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,
                                                   'imagenes': imagenes,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})


def mensajeria_detalle(request, id):
    return render(request, "paginas/mensajeria_detalle.html")

########################################################################################################################

# CESTA
def cesta(request):
    return render(request, "paginas/cesta.html")

def search(request, page):
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'search'

    return render(request, "paginas/search.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,
                                                   'imagenes': imagenes,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})

#########################################################################################################################
