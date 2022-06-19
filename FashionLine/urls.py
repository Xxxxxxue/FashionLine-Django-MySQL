"""FashionLine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from general import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # general page
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('login/', views.login, name='login'),
    path('register/', views.registro, name='registro'),
    path('logout/', views.home, name='logout'),

    path('product/<int:page>', views.producto, name='producto'),
    path('product/<slug:tipo>/<int:page>/', views.producto_filtro_tipo, name='producto-filtro-tipo'),
    path('product/<slug:tipo>/<slug:categoria>/<int:page>/', views.producto_filtro_categoria, name='producto-filtro-categoria'),
    path('product_detail/<int:id>', views.producto_detalle),

    path('disign/<int:page>', views.diseno),
    path('disign/<slug:tipo>/<int:page>/', views.diseno_filtro_tipo, name='diseno-filtro-tipo'),
    path('disign/<slug:tipo>/<slug:categoria>/<int:page>/', views.diseno_filtro_categoria, name='diseno-filtro-categoria'),
    path('disign_detail/<int:id>', views.diseno_detalle),

    path('contact/<int:page>', views.agenda),
    path('contact/<slug:categoria>/<int:page>', views.agenda_categoria),
    path('contact_detail/<int:id>', views.agenda_detalle),

    path('message/<int:page>', views.mensajeria),
    path('message_chat/<int:id>', views.mensajeria_detalle),

    path('search/<int:page>', views.search),
    path('cart/', views.cesta),

    # # user
    path('user/profile/<int:id>', views.perfil),
    path('user/changeKey', views.changeKey),
    path('user/orders', views.pedidos),
    path('user/orders_detail/<int:id>', views.pedidos_detalle),
    path('user/mydisign/<int:page>', views.misdisenos),
    path('user/myproduct/<int:page>', views.misproductos),
    path('user/favorites/<int:page>', views.favoritos),
=======
    path('producto/<int:page>', views.producto, name='producto'),
    path('producto/<slug:tipo>/<int:page>/', views.producto_filtro_tipo, name='producto-filtro-tipo'),
    path('producto/<slug:tipo>/<slug:categoria>/<int:page>/', views.producto_filtro_categoria, name='producto-filtro-categoria'),
    path('producto_detalle/<int:id>', views.producto_detalle),

    path('diseno/<int:page>', views.diseno),
    path('diseno/<slug:tipo>/<int:page>/', views.diseno_filtro_tipo, name='diseno-filtro-tipo'),
    path('diseno/<slug:tipo>/<slug:categoria>/<int:page>/', views.diseno_filtro_categoria, name='diseno-filtro-categoria'),
    path('diseno_detalle/<int:id>', views.diseno_detalle),

    path('agenda/<int:page>', views.agenda),
    path('agenda/<slug:categoria>/<int:page>', views.agenda_categoria),
    path('agenda_detalle/<int:id>', views.agenda_detalle),

    path('mensajeria/<int:page>', views.mensajeria),
    path('mensajeria_detalle/<int:id>', views.mensajeria_detalle),

    # path('search/', views.search),

    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('cesta/', views.cesta),
    #
    # # user
    path('user/perfil/<int:id>', views.perfil),
    path('user/changeKey', views.changeKey),
    path('user/pedidos', views.pedidos),
    path('user/pedidos_detalle/<int:id>', views.pedidos_detalle),
    path('user/misdisenos/<int:page>', views.misdisenos),
    path('user/misproductos/<int:page', views.misproductos),
    path('user/favoritos/<int:page>', views.favoritos),
>>>>>>> d26d397246fc07fcc07cfe01c1d5066d7d8b27fe

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)