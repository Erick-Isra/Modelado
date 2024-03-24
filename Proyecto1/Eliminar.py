import csv

class Eliminar:
    def __init__(self,id):
        self.id = id
    
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
                