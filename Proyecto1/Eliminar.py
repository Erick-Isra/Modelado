import csv
"""
Clase Eliminar que nos ayuda a eliminar un producto en especifico
"""

class Eliminar:
    """
    Metodo contstructor
    Recibe un id
    Devuelve un obejeto de la clase Eliminar
    """
    def __init__(self,id):
        self.id = id
    
    """
    Metodo elimina, elimina un producto en espcifico guiandose por el id
    Recibe un id
    Devuelve un archivo csv con el producto eliminado
    """
    def elimina(self, id):         
        filas_actualizadas = []
        id_encontrado = False  
        with open('Tienda.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if (row[0] != id):
                    filas_actualizadas.append(row)
        with open('Tienda.csv', 'w', newline='') as csvfile:                          
                    writer = csv.writer(csvfile)
                    writer.writerows(filas_actualizadas)    
                