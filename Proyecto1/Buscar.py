import csv
class Buscar:
    def __init__(self,id):
        self.id = id
        
    def busqueda(self):   
        valor = ["Id", "Producto", "Precio", "Cantidad", "Dia", "Mes", "Año"] 
        i = 0   
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if(self.id == row[0]):
                    for subrow in row:
                        print(f"{valor[i]}: {subrow}") 
                        i += 1                       
                    return  
        return print("El id ingresado no existe")        
        
    