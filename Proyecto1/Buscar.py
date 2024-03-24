import csv
class Buscar:
    """
    Metodo constructor
    Recibe un id
    Devuelve un objeto de la clase Buscar
    """
    def __init__(self,id):
        self.id = id
    
    """
    Metodo busqueda,busca un producto en especifico guiandose por el id
    Recibe un id
    Devuelve los datos del producto si este existe
    """
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
        
    