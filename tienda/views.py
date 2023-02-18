from django.shortcuts import render

from .models import Producto

# Create your views here.

def tienda(req):
    productos=Producto.objects.all()
    return render(req, "tienda/tienda.html", {"productos": productos})