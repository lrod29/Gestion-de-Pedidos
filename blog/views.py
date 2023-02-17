from django.shortcuts import render

from blog.models import Post, Categoria
# Create your views here.

def blog(req):
    posts = Post.objects.all()
    return render(req, "blog/blog.html", {"posts": posts})


def categoria(req, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(req, "blog/categorias.html", {"categoria": categoria, "posts": posts})