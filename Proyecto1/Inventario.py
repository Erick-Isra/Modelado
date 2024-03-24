import csv 

class Inventario:
    """
    Metodo constructor
    No recibe parametros
    No devuelve nada
    """
    def __init__(self):
        pass

    """
    Metodo mostrarTodo, muestra todos los productos en Tienda.csv en orden alfabetico
    No recibe parametros
    Devuelve los datos de todos los productos
    """
    def mostrarTodo(self):
        inventario = []
        valor = ["Id", "Producto", "Precio", "Cantidad", "Dia", "Mes", "Año"] 
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if row:
                    inventario.append(row)
        ordenada = sorted(inventario, key=lambda x: x[1])
        for product in ordenada:
            i = 0
            for sub in product:
                print(f"{valor[i]}: {sub}") 
                i += 1  
            print("\n")                   
              