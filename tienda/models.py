from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria_producto'
        verbose_name_plural='categorias_productos'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen=models.ImageField( upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.nombre