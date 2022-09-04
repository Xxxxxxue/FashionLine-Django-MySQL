from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from general import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('user/', include('gestion_user.urls')),

    # general page
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('register/', views.registro, name='registro'),
    path('logout/', views.salir, name='logout'),

    path('product/<slug:sexo>/<int:page>', views.producto, name='producto'),
    path('product/<slug:tipo>/<slug:sexo>/<int:page>/', views.producto_filtro_tipo, name='producto-filtro-tipo'),
    path('product/<slug:tipo>/<slug:categoria>/<slug:sexo>/<int:page>/', views.producto_filtro_categoria, name='producto-filtro-categoria'),
    path('product_detail/<int:id>', views.producto_detalle),

    path('disign/<slug:sexo>/<int:page>', views.diseno),
    path('disign/<slug:tipo>/<slug:sexo>/<int:page>/', views.diseno_filtro_tipo, name='diseno-filtro-tipo'),
    path('disign/<slug:tipo>/<slug:categoria>/<slug:sexo>/<int:page>/', views.diseno_filtro_categoria, name='diseno-filtro-categoria'),
    path('disign_detail/<int:id>', views.diseno_detalle),

    path('contact/<int:page>', views.agenda),
    path('contact/<slug:categoria>/<int:page>', views.agenda_categoria),
    path('contact_detail/<int:id>', views.agenda_detalle),

    path('message/<int:page>', views.mensajeria),
    path('message_chat/<int:id>', views.mensajeria_detalle),

    path('search/<int:page>', views.search),
    path('cart/', views.cesta),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)