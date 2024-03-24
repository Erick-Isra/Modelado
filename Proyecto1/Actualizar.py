import csv
import Alta as alt
import Eliminar as elim

class Actualizar:
    def __init__(self,id):
        self.id = id

    def comprobarId(id):    
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if row:
                  if(id == row[0]):
                     return True           
        return False

    def actualizar(self,id):       
        salida = False              
        while(salida != True):
            filas_actualizadas = []
            producto_actualizado = []             
            print("Escoge una de las siguientes opciones")
            print("1. Actualizae codigo de barras")
            print("2. Actualizar nombre del producto")
            print("3. Actualizar cantidad del producto")
            print("4. Actualizar precio del prodcuto")
            print("5. Actualizar fecha de caducidad")
            print("6. Salir")
            opcion = input()            
            if opcion == "1":
                id = input("Ingresa el nuevo codigo de barras\n")
                if Actualizar.comprobarId(id) == False:                    
                    with open('Tienda.csv') as csvfile:
                        reader=csv.reader(csvfile)
                        for row in reader:
                            if row:
                                if(self.id == row[0]):
                                    indice = 0
                                    for subrow in row:
                                        if indice == 0:
                                            producto_actualizado.append(id)
                                        else:
                                            producto_actualizado.append(subrow)
                                        indice += 1
                                    filas_actualizadas.append(producto_actualizado)
                                else:
                                    filas_actualizadas.append(row)
                        eliminado = elim.Eliminar(self.id)
                        eliminado.elimina(self.id)
                        with open('Tienda.csv', 'w', newline='') as file:
                            writer = csv.writer(file)
                            for row in filas_actualizadas:
                                writer.writerow(row)                    
                    print("El codigo de barras ha sido actualizado")
                else:
                    print("El codigo de barras ingresado ya existe vuelva a intentarlo.")
            elif opcion == "2":                
                producto = str(input("Ingresa el nuevo nombre del producto\n"))
                with open('Tienda.csv') as csvfile:
                    reader=csv.reader(csvfile)
                    for row in reader:
                        if row:
                            if(self.id == row[0]):
                                indice = 0
                                for subrow in row:
                                    if indice == 1:
                                        producto_actualizado.append(producto)
                                    else:
                                        producto_actualizado.append(subrow)
                                    indice += 1
                                filas_actualizadas.append(producto_actualizado)
                            else:
                                filas_actualizadas.append(row)
                    eliminado = elim.Eliminar(self.id)
                    eliminado.elimina(self.id)
                    with open('Tienda.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in filas_actualizadas:
                            writer.writerow(row)                    
                print("El nombre del producto ha sido actualizado")
            elif opcion == "3":
                num = int(input("Ingresa la nueva cantidad del producto\n"))
                cantidad = "(" + str(num) + " unidades" + ")"
                with open('Tienda.csv') as csvfile:
                    reader=csv.reader(csvfile)
                    for row in reader:
                        if row:
                            if(self.id == row[0]):
                                indice = 0
                                for subrow in row:
                                    if indice == 3:
                                        producto_actualizado.append(cantidad)
                                    else:
                                        producto_actualizado.append(subrow)
                                    indice += 1
                                filas_actualizadas.append(producto_actualizado)
                            else:
                                filas_actualizadas.append(row)
                    eliminado = elim.Eliminar(self.id)
                    eliminado.elimina(self.id)
                    with open('Tienda.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in filas_actualizadas:
                            writer.writerow(row)
                print("La cantidad del producto ha sido actualizada")
            elif opcion == "4":
                precio = float(input("Ingresa el nuevo precio del producto\n"))
                with open('Tienda.csv') as csvfile:
                    reader=csv.reader(csvfile)
                    for row in reader:
                        if row:
                            if(self.id == row[0]):
                                indice = 0
                                for subrow in row:
                                    if indice == 2:
                                        producto_actualizado.append(precio)
                                    else:
                                        producto_actualizado.append(subrow)
                                    indice += 1
                                filas_actualizadas.append(producto_actualizado)
                            else:
                                filas_actualizadas.append(row)
                    eliminado = elim.Eliminar(self.id)
                    eliminado.elimina(self.id)
                    with open('Tienda.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        for row in filas_actualizadas:
                            writer.writerow(row)
                print("El precio del producto ha sido actualizado")
            elif opcion == "5":
                print("Ingresa la nueva fecha de caducidad")
                dia = int(input("Ingresa el dia de caducidad\n"))                
                if dia >= 1 and dia <= 31:
                    mes = int(input("Ingresa el mes de caducidad\n"))
                    if mes >= 1 and mes <= 12:
                        año = int(input("Ingresa el año de caducidad\n")) 
                        if año >= 2025 and año <= 2027:  
                            with open('Tienda.csv') as csvfile:
                                reader=csv.reader(csvfile)
                                for row in reader:
                                    if row:
                                        if(self.id == row[0]):
                                            indice = 0
                                            for subrow in row:
                                                if indice == 4:
                                                    producto_actualizado.append(dia)
                                                elif indice == 5:
                                                    producto_actualizado.append(mes)
                                                elif indice == 6:
                                                    producto_actualizado.append(año)
                                                else:
                                                    producto_actualizado.append(subrow)
                                                indice += 1
                                            filas_actualizadas.append(producto_actualizado)
                                        else:
                                            filas_actualizadas.append(row)
                                eliminado = elim.Eliminar(self.id)
                                eliminado.elimina(self.id)
                                with open('Tienda.csv', 'w', newline='') as file:
                                    writer = csv.writer(file)
                                    for row in filas_actualizadas:
                                        writer.writerow(row)    
                            print("La fecha de caducidad ha sido actualizada")     
                            
                        else:
                               print("El año ingresado no es valido.")
                    else:
                              print("El mes ingresado no es valido")
                else:
                        print("El dia ingresado no es valido.") 
            elif opcion == "6":
                salida = True
            else:
                print("Opcion no valida")
            

        

                