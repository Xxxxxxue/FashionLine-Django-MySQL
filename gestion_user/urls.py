from django.contrib.staticfiles.urls import static
from django.urls import path
from gestion_user import views

urlpatterns = [

    path('img/<int:id>', views.getImg),

    path('profile/<int:id>', views.perfil, name="perfil"),
    path('profile/direccion/<int:id>', views.perfil_dir, name="direccion"),
    path('profile/direccion/delete/<int:id>', views.perfil_dir_delete),
    path('profile/edit/<int:id>', views.perfil_edit, name="perfil-edit"),

    path('slider/delete/<int:id>', views.img_delete),

    path('changeKey', views.changeKey),
    path('orders', views.pedidos),
    path('orders_detail/<int:id>', views.pedidos_detalle),

    path('mydisign/<slug:sexo>/<int:page>', views.misdisenos),
    path('mydisign/edit/<slug:sexo>/<int:page>/<int:id>', views.misdisenos_edit),
    path('mydisign/delete/<slug:sexo>/<int:page>/<int:id>', views.misdisenos_delete),

    path('myproduct/<slug:sexo>/<int:page>', views.misproductos),
    path('myproduct/edit/<slug:sexo>/<int:page>/<int:id>', views.misproductos_edit),
    path('myproduct/delete/<slug:sexo>/<int:page>/<int:id>', views.misproductos_delete),

    path('favorites/<slug:sexo>/<int:page>', views.favoritos),
    path('favorites/delete/<slug:sexo>/<int:id>', views.favoritos_delete),
    path('megusta/<int:id>', views.megusta),
]
from FashionLine import settings
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)