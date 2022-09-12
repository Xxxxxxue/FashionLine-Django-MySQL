
from django.urls import path, re_path
from . import views


urlpatterns = [

    # general page
    path('home', views.home.as_view()),
    path('productos', views.productos.as_view()),
    path('disign', views.disenos.as_view()),
    path('agendas', views.agendas.as_view()),


]
