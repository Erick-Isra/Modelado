import csv
import Alta as alt
import Buscar as bus
import EliminarTodo as Allelim
import Eliminar as elim
import Inventario as inv
import InventarioAñoMes as invAñoMes
import Actualizar as act
"""
Funcion que nos ayuda a comprobar si un id ya existe en el arcihvo Tienda.csv
"""
def comprobarId(id):    
        with open('Tienda.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                if row:
                  if(id == row[0]):
                     return True           
        return False
#--------------------------------------------------------------------------------------------------
 #Interfaz
salida = False
while(salida == False):
      print("Escoge una de las siguientes opciones")
      print("1. Dar de alta un producto")
      print("2. Ver todo el inventario")
      print("3. Ver inventario por año y mes")
      print("4. Eliminar un prodcuto")
      print("5. Buscar un producto")
      print("6. Actualizar un producto")
      print("7. Borrar todos los productos")
      print("8. Salir")
      opcion = input()
      if opcion == "1":            
            id = input("Ingresa el id del producto\n")
            if comprobarId(id) == False:
                  producto = str(input("Ingresa el nombre producto\n"))
                  precio = float(input("Ingresa el precio del producto\n"))
                  num = int(input("Ingresa la cantidad del producto\n"))
                  cantidad = "(" + str(num) + " unidades" + ")"
                  dia = int(input("Ingresa el dia de caducidad\n"))
                  if dia >= 1 and dia <= 31:
                        mes = int(input("Ingresa el mes de caducidad\n"))
                        if mes >= 1 and mes <= 12:
                          año = int(input("Ingresa el año de caducidad\n")) 
                          if año >= 2025 and año <= 2027:                    
                            nuevo_producto = alt.Alta(id, producto, precio, cantidad, dia, mes, año)
                            nuevo_producto.agregar_producto(id, producto, precio, cantidad, dia, mes, año)
                          else:
                               print("El año ingresado no es valido.")
                        else:
                              print("El mes ingresado no es valido")
                  else:
                        print("El dia ingresado no es valido.")       
                  
            else:
                  print("El id ingresado ya existe vuelva a intentarlo.")
            
      elif opcion == "2":
           vertodoInventario = inv.Inventario()
           vertodoInventario.mostrarTodo()
      elif opcion == "3":
           verinvAñoMes = invAñoMes.InventarioAñoMes()
           verinvAñoMes.mostrarTodo()            
      elif opcion == "4":
            id = input("Ingresa el id del producto\n")
            if comprobarId(id) == True:
                 print("Estas seguro de eliminar este producto?")
                 print("1.Si")
                 print("2.No")
                 opcioneliminar = input()
                 if opcioneliminar == "1":
                      elimina = elim.Eliminar(id)
                      elimina.elimina(id)
                 else:
                      print("Operacion cancelada")
            else:
                  print("El id ingresado no existe.")
      elif opcion == "5":
            id_producto = input("Ingresa el id del producto\n")
            busqueda = bus.Buscar(id_producto)
            busqueda.busqueda()  
      elif opcion == "6":
            id = input("Ingresa el id del producto\n")
            if comprobarId(id) == True:
                 actualizar = act.Actualizar(id)
                 actualizar.actualizar(id)                 
            else:
                  print("El id ingresado no existe.")
      elif opcion == "7":
            print("Esta accion borrara todo su inventario ¿Desea continuar?")
            print("1.Si")
            print("2.No")
            opcion2 = input()
            if opcion2 == "1":
                  elimina_todo = Allelim.EliminarTodo()
                  elimina_todo.elimina_todo()
            else:
                  print("Operacion cancelada")            
      elif opcion == "8":
            print("Cerrando el programa...")
            salida = True
      else:
            print("Opcion invalida, vuelve a intentarlo.")
    
    