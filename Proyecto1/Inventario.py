import csv 

class Inventario:

    def __init__(self):
        pass

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
              