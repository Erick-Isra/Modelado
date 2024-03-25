import csv
import Alta as alt
import Eliminar as elim
import Producto as prod

class Actualizar:

    """
    Metodo constructor de la clase Actualizar
    Recibe un parametro id
    Devuelve un obejto de clase actualizar
    """
    def __init__(self,id):
        self.id = id

    """
        Metodo que se se encarga de verificar si un id existe.
        param:
            str id = El id del producto a buscar.
        returns:
            boolean 
    """
    def comprobarId(id):    
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if row:
                  if(id.upper() == row[0]):
                     return True           
        return False
    
    """
        Metodo que se se encarga de actualizar el id, nombre, precio, cantidad o fecha de un producto.
        param:
            str id = El id del producto a actualizar.
        returns:
            Tienda.csv = El archivo csv con los datos actualizados.
    """
    def actualizar(self,id):       
        salida = False                      
        while(salida != True):
            filas_actualizadas = []
            producto_actualizado = []  
            #------------------------------------------------------------------------------------------------
             #Menu de opciones           
            print("Escoge una de las siguientes opciones")
            print("1. Actualizar el  codigo de barras")
            print("2. Actualizar el nombre del producto")
            print("3. Actualizar la cantidad del producto")
            print("4. Actualizar el precio del prodcuto")
            print("5. Actualizar la fecha de caducidad")
            print("6. Salir")
            opcion = input()  
            #------------------------------------------------------------------------------------------------
             #Actualiza el id del producto          
            if opcion == "1":
                id = input("Ingresa el nuevo codigo de barras\n").upper()
                if Actualizar.comprobarId(id) == False:        
                    try:
                        nuevo_producto = prod.Producto()
                        nuevo_producto.setid(id)                        
                        with open('Tienda.csv') as csvfile:
                          reader=csv.reader(csvfile)
                          for row in reader:                            
                            if(row and self.id == row[0]):
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
                        self.id = id                   
                        print("El codigo de barras ha sido actualizado")
                    
                    except ValueError as e:
                        print(f"Error: {e}")
                        print("Por favor, intenta de nuevo.")                  
                else:
                    print("El codigo de barras ingresado ya existe vuelva a intentarlo.")
            #------------------------------------------------------------------------------------------------
             #Actualiza el nombre del producto
            elif opcion == "2":                 
                try:  
                    producto = str(input("Ingresa el nuevo nombre del producto\n"))
                    nuevo_producto = prod.Producto()
                    nuevo_producto.setNombre(producto)                 
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
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Por favor, intenta de nuevo.")              
            
            #------------------------------------------------------------------------------------------------
             #Actualiza la cantidad del producto
            elif opcion == "3":
                num = input("Ingresa la nueva cantidad del producto\n")
                try:
                    nuevo_producto = prod.Producto()
                    nuevo_producto.setCantidad(num) 
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
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Por favor, intenta de nuevo.")   

            #------------------------------------------------------------------------------------------------
             #Actualiza el precio del producto 
            elif opcion == "4":
                precio = input("Ingresa el nuevo precio del producto\n")
                try:
                    nuevo_producto = prod.Producto()
                    nuevo_producto.setPrecio(num)
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
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Por favor, intenta de nuevo.")

            #------------------------------------------------------------------------------------------------
             #Actualiza la fecha de caducidad del producto   
            elif opcion == "5":
                print("Ingresa la nueva fecha de caducidad")
                try:
                     nuevo_producto = prod.Producto()
                     dia = input("Ingresa el dia de caducidad\n")
                     nuevo_producto.setDia(dia)
                     mes = input("Ingresa el mes de caducidad\n")
                     nuevo_producto.setMes(mes)
                     año = input("Ingresa el año de caducidad\n")
                     nuevo_producto.setAño(año)
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
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Por favor, intenta de nuevo.")                       

            #------------------------------------------------------------------------------------------------
             #Salida del submenu                                    
            elif opcion == "6":
                salida = True

            #------------------------------------------------------------------------------------------------
             #Opcion invalida
            else:
                print("Opcion invalida, vuelve a intentarlo")
            

        

                