from django.conf.urls.static import static
from django.urls import path, include
from general import views
from django.conf import settings

urlpatterns = [

    #flutter
    path('api/', include('flutter.urls')),

    # user
    path('user/', include('gestion_user.urls')),
    path('email/', include('email_reset.urls')),

    # general page
    path('', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('register/', views.registro, name='registro'),
    path('logout/', views.salir, name='logout'),

    path('product/<slug:sexo>/<int:page>', views.producto, name='producto'),
    path('product/<slug:tipo>/<slug:sexo>/<int:page>/', views.producto_filtro_tipo, name='producto-filtro-tipo'),
    path('product/<slug:tipo>/<slug:categoria>/<slug:sexo>/<int:page>/', views.producto_filtro_categoria,
         name='producto-filtro-categoria'),
    path('product_detail/<int:id>', views.producto_detalle),
    path('productcli/<int:iduser>/<slug:sexo>/<int:page>', views.producto_user),

    path('disign/<slug:sexo>/<int:page>', views.diseno),
    path('disign/<slug:tipo>/<slug:sexo>/<int:page>/', views.diseno_filtro_tipo, name='diseno-filtro-tipo'),
    path('disign/<slug:tipo>/<slug:categoria>/<slug:sexo>/<int:page>/', views.diseno_filtro_categoria,
         name='diseno-filtro-categoria'),
    path('disign_detail/<int:id>', views.diseno_detalle),
    path('disigncli/<int:iduser>/<slug:sexo>/<int:page>', views.diseno_user),

    path('contact/<int:page>', views.agenda),
    path('contact/<slug:categoria>/<int:page>', views.agenda_categoria),
    path('contact_detail/<int:id>', views.agenda_detalle),

    path('message/<int:page>', views.mensajeria),
    path('message_chat/<int:iduser>/<int:id>', views.mensajeria_detalle),
    path('message_submit/<int:id>', views.mensajeria_submit),

    path('search/<slug:valor>/<slug:sexo>/<int:page>', views.search),
    path('filtro/<slug:tip>/<slug:fc>/<slug:ft>/<slug:fv>/<slug:fcad>/<slug:fp>/<slug:sexo>/<int:page>', views.filtro),

    path('cart/<int:id>', views.cesta),
    path('cart/compra/<int:id>', views.lineacesta),
    path('pagado/<int:id>', views.pagado),



]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)