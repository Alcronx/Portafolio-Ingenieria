class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carritoReceta")
        if not carrito:
            self.session["carritoReceta"] = {}
            self.carrito = self.session["carritoReceta"]
        else:
            self.carrito = carrito

    def agregar (self, producto):
        id = str(producto.productid)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.productid,
                "nombre": producto.productname,
                "acumulado": producto.purchaseprice,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"]+= 1
            self.carrito[id]["acumulado"] += producto.purchaseprice
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carritoReceta"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id= str(producto.productid)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.productid)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.purchaseprice
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carritoReceta"] = {}
        self.session.modified = True



