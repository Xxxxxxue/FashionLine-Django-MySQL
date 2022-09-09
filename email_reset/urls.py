from django.urls import path

from email_reset.views import *

urlpatterns = [
    path('reset/password/', ResetPasswordView.as_view(), name='reset_password'),
    path('change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password')

]
