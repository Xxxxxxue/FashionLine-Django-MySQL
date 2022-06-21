from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
from general import models
from general import pagination
from django.utils import timezone
from django.contrib.auth import logout

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

# LOGOUT
def salir(request):
    logout(request)
    redirect(home)

########################################################################################################################

# PRODUCTO
def producto(request,sexo,page):
    # sacar database para el filto : variables grobales
    # color, talla, precio(no), valoracion, tipos y categorias para filtro

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
    url = 'product/' + sexo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_filtro_tipo(request,sexo,tipo,page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando productos de tipo x
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    # print("Tipo de producto: ",producto[1].getTipo())
    productos=[]
    for t in psexo:
        if(t.idproducto.getTipo()==tipo):
            productos.append(t.idproducto)

    # sacar una imagen para cada producto
    imagenes = []
    for index, p in enumerate(productos):
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]


    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + sexo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla,'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes, 'sexos':sexos, 'sexo': sexo,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'],'paginacion_url': url})

def producto_filtro_categoria(request,tipo,sexo,categoria,page):
    # sacar database para el filto
    # color, talla, precio(no), valoracion, tipos y categorias

    # sacando productos de tipo x
    s = sexos.get(tipo=sexo)
    psexo = models.Productosexo.objects.filter(idsexo=s)
    # print("Tipo de producto: ",producto[1].getTipo())
    productos = []
    for t in psexo:
        if (t.idproducto.getCategoria() == categoria):
            productos.append(t.idproducto)

    # sacar una imagen para cada producto
    imagenes = []
    for p in productos:
        imagenes += models.Productoimagen.objects.filter(idproducto=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + categoria + '/' + sexo

    return render(request, "paginas/producto.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad, 'categorias': categorias,
                                                     'imagenes': imagenes, 'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'], 'num': datos_pagination['num'],
                                                     'paginacion_url': url})

def producto_detalle(request, id):
    # saca producto -> id
    producto = models.Productos.objects.filter(id=id)
    # saca todos imagenes
    imagenes = models.Productoimagen.objects.filter(idproducto=producto)


    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'product/' + tipo + '/' + categoria

    return render(request, "paginas/producto_detalle.html", {'color': color, 'talla': talla,
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
    url = 'disign/' + '/' + sexo

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
                                                     'valoracion': valoracion, 'tipo': tipocad,
                                                     'categorias': categorias,'imagenes': imagenes,
                                                     'productos': datos_pagination['page_productos'],
                                                     'pagelist': datos_pagination['pageList'],
                                                     'num': datos_pagination['num'], 'paginacion_url': url})

def diseno_filtro_tipo(request, sexo, page, tipo):
    # database filtro

    # sacando productos de sexo
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if(t.iddiseno.getTipo() == tipo):
            productos.append(t.iddiseno)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo + '/' + sexo

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
    s = sexos.get(tipo=sexo)
    psexo = models.Disenosexo.objects.filter(idsexo=s)
    productos = []
    for t in psexo:
        if (t.iddiseno.getCategoria() == categoria):
            productos.append(t.iddiseno)

    # imagenes
    imagenes = []
    for p in productos:
        imagenes += models.Disenoimagen.objects.filter(iddiseno=p)[:1]

    # Paginacion : llamar metodo pagination
    datos_pagination = pagination.pagination(productos, page)
    url = 'disign/' + tipo + '/' + categoria + '/' + sexo

    return render(request, "paginas/diseno.html", {'color': color, 'talla': talla, 'sexos': sexos, 'sexo': sexo,
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
    cat = categorias.get(categoria=categoria)
    pcliente = models.Clientecategoria.objects.filter(idcategoria=cat)
    productos = []
    for p in pcliente:
        productos.append(p.idcliente)

    imagenes = []
    for p in productos:
        imagenes += models.Clienteimagen.objects.filter(idcliente=p)
    print(imagenes)

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
