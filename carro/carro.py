class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro", {})
        self.carro=carro
    
    def agregar(self, producto):
        if (str(producto.id) not in self.carro):
            self.carro[str(producto.id)]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 0,
                "imagen": producto.imagen.url
            }
        self.carro[str(producto.id)]['cantidad'] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
        
    def restar_producto(self, producto):
        if self.carro[str(producto.id)]['cantidad'] <= 1:
            self.eliminar(producto)
        else:
            self.carro[str(producto.id)]['cantidad'] -= 1

        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.guardar_carro()
