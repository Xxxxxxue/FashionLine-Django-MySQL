import smtplib
import uuid
from general import models
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail
from FashionLine import settings
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView
from email_reset.forms import ResetPasswordForm, ChangePasswordForm

class ResetPasswordView(FormView):
    form_class = ResetPasswordForm
    template_name = 'resetpwd.html'
    success_url = reverse_lazy('/')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, user):
        data = {}
        try:
            URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
            print('send_user',user.username)
            token = uuid.uuid4()
            u = User.objects.get(username=user.username)
            print(u)
            models.Clientes.objects.filter(idusuario=u).update(token=token)
            print(u.username)

            # send_mail(
            #     'Reseteo de contraseña',
            #     'hola',
            #     'nievealas@gmail.com',
            #     [user.username],
            #     fail_silently=False,
            # )
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email_to = user.username
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = 'Reseteo de contraseña'

            content = render_to_string('send_email.html', {
                'user': user,
                'link_resetpwd': 'http://{}/email/change/password/{}/'.format(URL, str(token)),
                'link_home': 'http://{}'.format(URL)
            })
            mensaje.attach(MIMEText(content, 'html'))

            mailServer.sendmail(settings.EMAIL_HOST_USER,
                                email_to,
                                mensaje.as_string())

        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = ResetPasswordForm(request.POST)  # self.get_form()
            if form.is_valid():
                user = form.get_user()
                data = self.send_email_reset_pwd(user)
            else:
                data['error'] = form.errors
                print(form.errors)
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        return context


class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'changepwd.html'
    success_url = reverse_lazy('/')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        token = self.kwargs['token']

        if models.Clientes.objects.filter(token=token).exists():
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            print('change password')
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                user = models.Clientes.objects.filter(token=kwargs['token']).get()
                print('token:',kwargs['token'], user, 'pwd: ',request.POST['password'])
                user = user.idusuario
                print(user.username)
                u = User.objects.get(username=user.username)
                u.set_password(request.POST['password'])
                u.save()
                new = uuid.uuid4()
                models.Clientes.objects.filter(idusuario=user).update(token=new)
                print(new)

            else:
                data['error'] = form.errors

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        context['login_url'] = settings.LOGIN_URL
        return context
