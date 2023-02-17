from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contacto(req):
    formulario_contacto=FormularioContacto()
    return render(req, "contacto/contacto.html",{"miFormulario": formulario_contacto})