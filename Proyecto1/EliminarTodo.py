import csv
class EliminarTodo:
    def __init__(self):
        pass

    def elimina_todo(self):
        with open('Tienda.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Producto", "Precio", "Cantidad", "Dia", "Mes", "Año"]) 
        print("Se ha eliminado todo el inventario.") 
        
       