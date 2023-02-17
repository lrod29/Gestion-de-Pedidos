from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Create your views here.

def contacto(req):
    formulario_contacto=FormularioContacto()
    if req.method=="POST":
        formulario_contacto=FormularioContacto(data=req.POST)
        if formulario_contacto.is_valid():
            nombre=req.POST.get("nombre")
            email=req.POST.get("email")
            contenido=req.POST.get("contenido")
            return redirect("/contacto/?valido")

    return render(req, "contacto/contacto.html",{"miFormulario": formulario_contacto})