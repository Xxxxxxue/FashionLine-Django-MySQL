<<<<<<< HEAD
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

=======
import math

from django.shortcuts import render, HttpResponse, redirect
from general import models
from django.db.models import Q
from django.core.paginator import Paginator
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

# PAGINAS PRINCIPALES
#################################################################
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
<<<<<<< HEAD
    text = ' <div class="carousel-caption d-none d-md-block"> \
            <h5>WELCOME TO FASHIONLINE!</h5>\
            <p>Get your fashion, choose you style!</p> \
            </div>'
    slider = models.Imagenes.objects.filter(nombre='slider')
    return render(request, "paginas/home.html", {'slider': slider, 'tipo': tipocad, 'categorias':categorias, 'text': text })
=======
    tipocad = models.Tipocategoria.objects.all()
    categoria = models.Categorias.objects.all()
    slider = models.Imagenes.objects.filter(nombre='slider')
    return render(request, "paginas/home.html", {'slider': slider, 'tipo': tipocad, 'categoria':categoria })
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

# LOGIN
def login(request):
    # get
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, "paginas/login.html", {'tipo': tipocad, 'categorias':categorias})
=======
        return render(request, "paginas/login.html")
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
    # post
    username = request.POST.get('usuario')
    password = request.POST.get('password')

    if username == '111@gmail.com' and password == '1111':
        return redirect(home)
    error_msg = 'Usuario o Contraseña está incorrecto.'
<<<<<<< HEAD

    return render(request, "paginas/login.html", {'tipo': tipocad, 'categorias':categorias, 'error_msg': error_msg})
=======
    return render(request, "paginas/login.html", {'error_msg': error_msg})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

# REGISTRAR
def registro(request):
    # get
    if request.method == "GET":
<<<<<<< HEAD
        return render(request, "paginas/registro.html", {'tipo': tipocad, 'categorias':categorias})
=======
        return render(request, "paginas/registro.html")
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
    # post
    username = request.POST.get('usuario')
    password = request.POST.get('password')
    return redirect(login)

########################################################################################################################
# PRODUCTO
def producto(request,page):
<<<<<<< HEAD
    # sacar database para el filto : variables grobales
    # color, talla, precio(no), valoracion, tipos y categorias para filtro
=======
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla =  models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    categoria = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

    #sacando productos
    productos = models.Productos.objects.all()
    for p in productos:
        img = models.Productoimagen.objects.filter(idproducto=p)
        #imagen = models.Imagenes.objects.filter(id=img)
        print(img)
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product'

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_filtro_tipo(request,tipo, page):
=======
    #Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    #num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    #pagina inicial
    begin = (num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1
    #pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <=10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end+1)
    url = 'producto'

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': categoria, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': page_productos, 'pagelist':pageList,
                                                     'num': num,'paginacion_url': url})

def producto_filtro_tipo(request,tipo, page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla = models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    categoria = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()

>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
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
<<<<<<< HEAD

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],'paginacion_url': url})

def producto_filtro_categoria(request,tipo, categoria, page):
    # filto: color, talla, precio(no), valoracion, tipos y categorias
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'producto/'+tipo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': categoria,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': page_productos,
                                                     'pagelist': pageList, 'num': num,'paginacion_url': url})

def producto_filtro_categoria(request,tipo, categoria, page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla = models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    cat = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

    # sacando productos
    productos = models.Productos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + categoria

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'producto/' + tipo + categoria

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': cat,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': page_productos,
                                                     'pagelist': pageList, 'num': num, 'paginacion_url': url})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

def producto_detalle(request, id):
    return render(request, "paginas/producto_detalle.html")

########################################################################################################################
# DISENO
def diseno(request, page):
<<<<<<< HEAD
    # database filtro
=======
    # database
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla = models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    cat = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
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
    # database filtro
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'diseno'

    return render(request, "paginas/diseno.html",{'color': color, 'talla': talla,
                                                 'valoracion': valoracion, 'tipo': cat,
                                                 'categorias': categorias,
                                                 'imagenes': imagenes, 'productos': page_productos,
                                                  'paginacion_url': url,'num': num})

def diseno_filtro_tipo(request, page, tipo):
    # database
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla = models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    cat = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
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
    # database filtro
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'diseno/' + tipo

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': cat,
                                                   'categorias': categorias,
                                                   'imagenes': imagenes, 'productos': page_productos,
                                                   'paginacion_url': url, 'num': num})

def diseno_filtro_categoria(request, page, tipo, categoria):
    # database
    # color, talla, precio(no), valoracion, tipos y categorias
    color = models.Colores.objects.all()
    talla = models.Tallas.objects.all()
    valoracion = models.Valoraciones.objects.all()
    cat = models.Tipocategoria.objects.filter(~Q(tipo="usuarios"))
    categorias = models.Categorias.objects.all()
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

    # sacando disenos
    productos = models.Disenos.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
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
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'diseno' + tipo + categoria

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla,
                                                   'valoracion': valoracion, 'tipo': cat,
                                                   'categorias': categorias,
                                                   'imagenes': imagenes, 'productos': page_productos,
                                                   'paginacion_url': url, 'num': num})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

def diseno_detalle(request, id):
    return render(request, "paginas/diseno_detalle.html")

# AGENDA
def agenda(request, page):
    # database
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'contact'

    return render(request, "paginas/agenda.html", {'color': color, 'talla': talla,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,
                                                     'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],
                                                     'paginacion_url': url})
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'agenda'
    return render(request, "paginas/agenda.html", {'productos': page_productos, 'num': num})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

def agenda_categoria(request, page, categoria):
    # database
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
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
=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'agenda/' + categoria
    return render(request, "paginas/agenda.html", {'productos': page_productos, 'num': num})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

def agenda_detalle(request, id):
    return render(request, "paginas/agenda_detalle.html")

# MENSAJERIA
def mensajeria(request, page):
    # database
    productos = models.Clientes.objects.all()
    imagenes = models.Imagenes.objects.filter(~Q(nombre='slider'))

<<<<<<< HEAD
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

=======
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 1)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # pagina inicial
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # pagina final
    end = begin + 9
    if end > pager.num_pages:
        end = pager.num_pages
    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pageList = range(begin, end + 1)
    url = 'mensajeria'

    return render(request, "paginas/mensajeria.html", {'productos': page_productos, 'num': num})
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

def mensajeria_detalle(request, id):
    return render(request, "paginas/mensajeria_detalle.html")

<<<<<<< HEAD
########################################################################################################################

=======
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
# CESTA
def cesta(request):
    return render(request, "paginas/cesta.html")

<<<<<<< HEAD
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


=======
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
########################################################################################################################
#PAGINAS USER

# PERFIL
def perfil(request, id):
<<<<<<< HEAD

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
=======
    return render(request, "paginas/user_perfil.html")

# PEDIDOS
def pedidos(request):
    return render(request, "paginas/user_pedidos.html")

def pedidos_detalle(request, id):
    return render(request, "paginas/user_pedidos_detalle.html")

# MIS DISENOS
def misdisenos(request, page):
    return render(request, "paginas/user_disenos.html")

# MIS PRODUCTOS
def misproductos(request, page):
    return render(request, "paginas/user_productos.html")

# MIS FAVORITOS
def favoritos(request, page):
    return render(request, "paginas/user_favoritos.html")

# CAMBIAR CONTRASEÑA
def changeKey(request):
    return render(request, "paginas/user_cambiarKey.html")
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe
