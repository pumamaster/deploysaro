from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail

from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'index.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class BlogView(TemplateView):
    template_name = 'blog.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'

def enviar_correo(nombre, correo, titulo, descripcion):
    asunto = f'{nombre}: {titulo}'
    mensaje = descripcion
    email_from = correo
    email_to = ['alejandrogongis03@thecreativefusion.com',]
    send_mail(asunto, mensaje, email_from, email_to)

def contact_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        enviar_correo(nombre, correo, titulo, descripcion)
        messages.success(request, '¡Gracias por contactarnos!')
        # Redirige a la URL 'contact' después de enviar el correo
        return redirect('contact')


    return render(request, 'contacto.html')