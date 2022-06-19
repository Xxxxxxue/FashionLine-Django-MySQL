from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from general import models
from general import pagination


# variables globales para navigation y filtro
tipocad = models.Tipocategoria.objects.all()
categorias = models.Categorias.objects.all()
color = models.Colores.objects.all()
talla =  models.Tallas.objects.all()
valoracion = models.Valoraciones.objects.all()


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
    # ESTOS CODIGOS NO INCLUYE EL DE TIPO USUARIO
    # tipocad = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    # id_not = models.Tipocategoria.objects.get(tipo="usuarios")
    # categoria = models.Categorias.objects.filter(~Q(idtipocad=id_not))
    # print(slider)
    # print(tipocad,categoria)

    text = ' <div class="carousel-caption d-none d-md-block"> \
            <h5>WELCOME TO FASHIONLINE!</h5>\
            <p>Get your fashion, choose you style!</p> \
            </div>'
    slider = models.Imagenes.objects.filter(nombre='slider')
    return render(request, "paginas/home.html", {'slider': slider, 'tipo': tipocad, 'categorias':categorias, 'text': text })


# LOGIN
def login(request):
    # get
    if request.method == "GET":
        return render(request, "paginas/login.html", {'tipo': tipocad, 'categorias':categorias})

    # post
    username = request.POST.get('usuario')
    password = request.POST.get('password')

    if username == '111@gmail.com' and password == '1111':
        return redirect(home)
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
    return redirect(login)

########################################################################################################################

# PRODUCTO
def producto(request,page):
    # sacar database para el filto : variables grobales
    # color, talla, precio(no), valoracion, tipos y categorias para filtro

    #sacando productos
    productos = models.Productos.objects.all()
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]
        # imagen = models.Imagenes.objects.filter(id=img)
        # print(imagenes.count(imagenes[index]))
        # print(imagenes[index].idimagen.imagen)

    # print(img,img[0].idproducto.id,img[1].idproducto.id)
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product'

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_filtro_tipo(request,tipo, page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando productos
    # t = models.Tipocategoria.objects.filter(tipo=tipo)
    # c = models.Categorias.objects.filter(idtipocad=t)
    # pc = []
    # for c1 in c:
    #     pc.append(models.Productocategoria.objects.filter(idcategoria=c1))
    # # productos = []
    # # for i in pt:
    # #     productos.append(models.Productos.objects.filter(idproducto=i))
    # print(pc)
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))
    productos = models.Productos.objects.all()


    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],'paginacion_url': url})

def producto_filtro_categoria(request,tipo, categoria, page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando productos
    productos = models.Productos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + categoria

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_detalle(request, id):
    return render(request, "paginas/producto_detalle.html")


########################################################################################################################
# DISENO
def diseno(request, page):
    # database filtro

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign'

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'], 'paginacion_url': url})

def diseno_filtro_tipo(request, page, tipo):
    # database
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def diseno_filtro_categoria(request, page, tipo, categoria):
    # database
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo + '/' + categoria

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def diseno_detalle(request, id):
    return render(request, "paginas/diseno_detalle.html")

# AGENDA
def agenda(request, page):
    # database
    productos = models.Clientes.objects.all()
    # user=[]
    # for index, p in enumerate(productos):
    #     user += models.Usuarios.objects.filter(idclientes=p)
    #     print(user[index].idclientes.nombre)

    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

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
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'contact/' + categoria

    return render(request, "paginas/agenda.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,
                                                   'imagenes': imagenes,
                                                   'productos': datos_pagination['page_productos'],
                                                   'pagelist': datos_pagination['pageList'],
                                                   'num': datos_pagination['num'],
                                                   'paginacion_url': url})

def agenda_detalle(request, id):
    return render(request, "paginas/agenda_detalle.html")

# MENSAJERIA
def mensajeria(request, page):
    # database
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

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


########################################################################################################################
#PAGINAS USER

# PERFIL
def perfil(request, id):
    return render(request, "paginas/user_perfil.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

# PEDIDOS
def pedidos(request):
    return render(request, "paginas/user_pedidos.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

def pedidos_detalle(request, id):
    return render(request, "paginas/user_pedidos_detalle.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

# MIS DISENOS
def misdisenos(request, page):
    return render(request, "paginas/user_disenos.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

# MIS PRODUCTOS
def misproductos(request, page):
    return render(request, "paginas/user_productos.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

# MIS FAVORITOS
def favoritos(request, page):
    return render(request, "paginas/user_favoritos.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': tipocad,
                                                   'categorias': categorias,})

# CAMBIAR CONTRASEÑA
def changeKey(request):
    return render(request, "paginas/user_cambiarKey.html", {'tipo': tipocad, 'categorias': categorias,})
