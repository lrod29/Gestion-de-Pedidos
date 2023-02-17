from django.shortcuts import render, HttpResponse

from servicios.models import Servicio

# Create your views here.

def home(req):
    return render(req, "ProyectoWebApp/home.html")


def tienda(req):
    return render(req, "ProyectoWebApp/tienda.html")


