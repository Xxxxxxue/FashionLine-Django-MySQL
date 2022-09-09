from django.core.paginator import Paginator
import math

def pagination(productos, page):
    # Paginacion  datos, num:cuantos quiere poner en una pagina
    pager = Paginator(productos, 8)
    # print(pager)
    # num es pagina actual, recogido informacion de parametros
    num = int(page)
    page_productos = pager.page(num)
    # print(page_productos)
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

    #indices de las paginas
    pageList = range(begin, end + 1)
    print(pageList)
    # valores a exportar en views.py
    datos_pagination = {
        'page_productos': page_productos,
        'num': num,
        'pageList': pageList
    }
    return datos_pagination