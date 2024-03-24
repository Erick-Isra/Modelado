import csv
"""
Clase Alta nos ayua a agregar un producto nuevo a Tienda.csv
"""
class Alta:
    """
    Metodo constructor
    Recibe un id, producto, precio, cantidad, dia, mes, año
    Devuelve un objeto de la clase Alta
    """
    def __init__(self, id, producto, precio, cantidad, dia, mes, año):
        self.id = id
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad 
        self.dia = dia
        self.mes = mes
        self.año = año   
    
    """
    Metodo agregar_producto, agrega un producto nuevo a la Tienda.csv
    """
    def agregar_producto(self, id, producto, precio, cantidad, dia, mes, año):
         with open('Tienda.csv', 'a', newline='') as file:
              writer = csv.writer(file)
              writer.writerow([
                id,
                producto,
                precio,
                cantidad,
                dia,
                mes,
                año          
              ])
         print("Se ha agregado el producto.")

