import csv

class InventarioAñoMes:
    def __init__(self):
        pass

    def mostrarTodo(self):        
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        valor = ["Id", "Producto", "Precio", "Cantidad", "Dia", "Mes", "Año"] 
        año1 = []
        año2 = []
        año3 = [] 
        mes = 1              
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                auxproducto = []
                if row:
                    if row[6] == "2025":                        
                        año1.append(row)
                    elif row[6] == "2026":                        
                        año2.append(row)
                    elif row[6] == "2027":                        
                        año3.append(row)

        ordenada1 = sorted(año1, key=lambda x: int(x[5])) 
        ordenada2 = sorted(año2, key=lambda x: int(x[5])) 
        ordenada3 = sorted(año3, key=lambda x: int(x[5]))   

        salida1 = False   
        print("2025")
        print("\n")
        indice1 = 0
        while(salida1 != True):            
            print(f"{meses[mes-1]} \n")
            for producto in ordenada1:
                i = 0                
                if int(producto[5]) == mes:
                    for sub in producto:
                        if indice1 != 6:
                          print(f"{valor[i]}: {sub}") 
                        i += 1
                        indice1 += 1
                print("\n")
            if mes == 12:
                salida1 = True
            mes += 1

        salida2 = False  
        mes = 1
        indice2 = 0
        print("2026")
        print("\n")
        while(salida2 != True):            
            print(f"{meses[mes-1]} \n")
            for producto in ordenada2:
                i = 0                
                if int(producto[5]) == mes:
                    for sub in producto:
                        if indice2 != 6:
                          print(f"{valor[i]}: {sub}") 
                        i += 1
                        indice2 += 1
                print("\n")
            if mes == 12:
                salida2 = True
            mes += 1   

        salida3 = False
        mes = 1  
        indice3 = 0
        print("2027") 
        print("\n")
        while(salida3 != True):            
            print(f"{meses[mes-1]} \n")
            for producto in ordenada1:
                i = 0                
                if int(producto[5]) == mes:
                    for sub in producto:
                        if indice3 != 6:
                          print(f"{valor[i]}: {sub}") 
                        i += 1
                        indice3 += 1
                print("\n")
            if mes == 12:
                salida3 = True
            mes += 1        



                
        
