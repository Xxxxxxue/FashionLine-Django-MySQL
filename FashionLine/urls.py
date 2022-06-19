from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from general import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # general page
    path('', views.home, name='home'),

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

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)