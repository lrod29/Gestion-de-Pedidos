from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


# Create your views here.

def contacto(req):
    formulario_contacto=FormularioContacto()
    if req.method=="POST":
        formulario_contacto=FormularioContacto(data=req.POST)
        if formulario_contacto.is_valid():
            nombre=req.POST.get("nombre")
            email=req.POST.get("email")
            contenido=req.POST.get("contenido")

            email=EmailMessage("Mensaje de App Django",
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n {}".format(nombre, email, contenido),
            "", ["luis29.rod@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(req, "contacto/contacto.html",{"miFormulario": formulario_contacto})