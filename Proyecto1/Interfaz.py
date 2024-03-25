import csv
import Alta as alt
import Buscar as bus
import EliminarTodo as Allelim
import Eliminar as elim
import Inventario as inv
import InventarioAñoMes as invAñoMes
import Actualizar as act
import ComprobarId as comprobarId
import Producto as prod

"""
Interfaz con la que interactua el usuario
"""
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
      #---------------------------------------------------------------------------------------------------------
            #Opcion 1 dar de alta un producto
      if opcion == "1":    
            id = input("Ingresa el id del producto\n").upper()
            comprobar = comprobarId.ComprobarId(id)    
            nuevo_producto = prod.Producto()            
            if comprobar.comprobarId(id) == False:
                  try:
                          nuevo_producto.setid(id)
                          producto = input("Ingresa el nombre producto\n")
                          nuevo_producto.setNombre(producto)                            
                          precio = input("Ingresa el precio del producto\n")
                          nuevo_producto.setPrecio(precio)
                          num = input("Ingresa la cantidad del producto\n")
                          nuevo_producto.setCantidad(num)
                          cantidad = nuevo_producto.getCantidad()
                          dia = input("Ingresa el dia de caducidad\n")
                          nuevo_producto.setDia(dia)
                          mes = input("Ingresa el mes de caducidad\n")
                          nuevo_producto.setMes(mes)
                          año = input("Ingresa el año de caducidad\n")
                          nuevo_producto.setAño(año)
                          nuevo_producto = alt.Alta(id, producto, precio,cantidad , dia, mes, año)
                          nuevo_producto.agregar_producto(id, producto, precio, cantidad, dia, mes, año)
                          
                  except ValueError as e:
                      print(f"Error: {e}")
                      print("Por favor, intenta de nuevo.") 
                    
            else:
                    print("El ID ingresado ya existe en el sistema. Por favor, intenta con otro.")
            
                  
            
                  
      #---------------------------------------------------------------------------------------------------------
           #Opcion 2 ver todo el inventario      
      elif opcion == "2":
           vertodoInventario = inv.Inventario()
           vertodoInventario.mostrarTodo()

      #---------------------------------------------------------------------------------------------------------
           #Opcion 3 ver inventario por año y mes
      elif opcion == "3":
           verinvAñoMes = invAñoMes.InventarioAñoMes()
           verinvAñoMes.mostrarTodo()


      #----------------------------------------------------------------------------------------------------------
           #Opcion 4 eliminar un producto            
      elif opcion == "4":
            id = input("Ingresa el id del producto, recuerda poner todo en mayusculas\n")
            comprobar = comprobarId.ComprobarId(id)  
            if comprobar.comprobarId(id) == True:
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


      #----------------------------------------------------------------------------------------------------------
         #Opcion 5 buscar un producto
      elif opcion == "5":
            id_producto = input("Ingresa el id del producto, recuerda poner todo en mayusculas\n")
            busqueda = bus.Buscar(id_producto)
            busqueda.busqueda()  

      #----------------------------------------------------------------------------------------------------------
            #Opcion 6 actualizar un producto
      elif opcion == "6":
            id = input("Ingresa el id del producto,  recuerda poner todo en mayusculas\n")
            comprobar = comprobarId.ComprobarId(id)  
            if comprobar.comprobarId(id) == True:
                 actualizar = act.Actualizar(id)
                 actualizar.actualizar(id)                 
            else:
                  print("El id ingresado no existe.")

      #----------------------------------------------------------------------------------------------------------
            #Opcion 7 borrar todos los productos
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
      
      #----------------------------------------------------------------------------------------------------------
            #Opcion 8 salir
      elif opcion == "8":
            print("Cerrando el programa...")
            salida = True

      #----------------------------------------------------------------------------------------------------------
            #Opcion invalida
      else:
            print("Opcion invalida, vuelve a intentarlo.")
    
    