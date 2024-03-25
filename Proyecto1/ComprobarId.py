import csv

class ComprobarId:
    """
    Metodo construtor de la clase ComprobarId
    Recibe un id
    Devuelve un objeto de la clase ComprobarId
    """
    def __init__(self, id):
        self.id = id
    
    """
    Metodo comprobarId, determina si un id ya existe dentro de Tienda.csv
    Recibe un id
    Regresa un booleano
    """
    def comprobarId(self, id):
        with open('Tienda.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row:
                   if (row[0] == id):
                      return True
        return False