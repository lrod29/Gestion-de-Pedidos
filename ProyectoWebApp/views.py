from django.shortcuts import render, HttpResponse

# Create your views here.

def home(req):
    return HttpResponse("Home")

def servicios(req):
    return HttpResponse("Servicios")

def tienda(req):
    return HttpResponse("Tienda")

def blog(req):
    return HttpResponse("Blog")

def contacto(req):
    return HttpResponse("Contacto")