
from django.urls import path
from . import views


urlpatterns = [

    # general page
    path('home', views.home.as_view()),


]
