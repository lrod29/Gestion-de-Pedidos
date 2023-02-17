from django.shortcuts import render

# Create your views here.

def tienda(req):
    return render(req, "tienda/tienda.html")