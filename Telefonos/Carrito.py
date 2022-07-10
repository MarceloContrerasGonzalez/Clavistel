from ast import Break


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
            
    
    def agregar(self, Movil):
        id = str(Movil.id_movil)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "imagen": Movil.img.url,
                "producto_id": Movil.id_movil,
                "nombre": Movil.nombre,
                "precio": Movil.costo,
                "acumulado": Movil.costo,
                "cantidad": 1,
            }
        elif self.carrito[id]["cantidad"] >= int(Movil.cant):
            self.carrito[id]["cantidad"] = self.carrito[id]["cantidad"]
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += Movil.costo
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
        
    def eliminar(self, Movil):
        id =str(Movil.id_movil)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
            
    def restar(self, Movil):
        id= str(Movil.id_movil)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["acumulado"] -= Movil.costo
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Movil)
            self.guardar_carrito()
            
    def limpiar(self):
        self.session["carrito"]= {}
        self.session.modified = True
        
    def comprar(self, Movil):
        id= str(Movil.id_movil)
        
    def restar(self, Movil):
        id= str(Movil.id_movil)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -=1
            self.carrito[id]["acumulado"] -= Movil.costo
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(Movil)
            self.guardar_carrito()
            
    def comprar(self, Movil):
        id= str(Movil.id_movil)
        if id in self.carrito.keys():
            Movil.cant = Movil.cant - self.carrito[id]["cantidad"]