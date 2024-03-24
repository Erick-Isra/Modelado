import csv
class EliminarTodo:
    """
    Metodo constructor
    No recibe parametros
    No devuelve nada
    """
    def __init__(self):
        pass

    """
    Metodo elimina_todo elimina todos los productos de Tienda.csv
    No recibe parametros
    Devuelve un archivo csv con solo los encabezados, sin productos
    """
    def elimina_todo(self):
        with open('Tienda.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Producto", "Precio", "Cantidad", "Dia", "Mes", "Año"]) 
        print("Se ha eliminado todo el inventario.") 
        
       