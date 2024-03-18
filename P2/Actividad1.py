"""
        mates_iguales
        ESta funcion se encarga de buscar todo slo coeficientes iguales de los colores mate y los regresa 
        en una lista 
"""
def mates_iguales(lista):
    listas_mates = []
    lista_iguales = []
    for sublistas in lista:
        for elemento in sublistas:
            if "M" in elemento:
                listas_mates.append(int(elemento[:-1]))  
    for i in range(len(listas_mates)):
        for j in range(i + 1, len(listas_mates)): 
            if listas_mates[i] == listas_mates[j]:
                lista_iguales.append(listas_mates[i])
                break  
    return lista_iguales
"""
        num_mates
        Esta funcion se encarga de contar el numero de colores mate que hay en la lista de clientes
"""
def num_mates(lista):
    contador = 0    
    for sublista in lista:
        for elemento in sublista:
            if "M" in elemento:
                contador += 1        
    return contador 
"""
        filas_mates
        Esta funcion se encarga de determinar si existe almenos una fila con todos los colores mate 
"""
def fila_mates(lista):
    filas = 0
    for sublista in lista:
        contador = 0
        for elemento in sublista:
            if "M" in elemento:
                contador += 1
        if contador == len(sublista):
            filas += 1
    if filas == 1:
        return True
    else:
        return False
"""
        num_blancos
        Funcion que se encarga de contar el numero de colores blancos que hay en la lista de clientes
"""
def num_blancos(lista):
    contador = 0
    for sublista in lista:
        for elemento in sublista:
            if "B" in elemento:
                contador += 1
    return contador 
"""
        Nblancos
        Funcion que se encraga de contar el numero de colores blancos que hay en una sublista 
"""
def Nblancos(lista):
    contador = 0
    for elemento in lista:
        if "B" in elemento:
            contador += 1
    return contador 
"""
        minimo_mates
        Funcion se encargade encontrar el coeficiente minimo de los colores mate
"""
def minimo_mates(lista):
    indice = 0
    for sublista in lista:
        for elemento in sublista:
            if "M" in elemento:
                aux = int(elemento[0])
                if indice == 0:
                    minimo = aux
                elif aux < minimo:
                    minimo = aux
        indice += 1 
    return minimo
"""
        minimi_blanco
        Funcion que se encarga de encontrar el coeficiente minimo de los colores blanco
"""
def minimo_blanco(lista):
    min = 0
    if not lista:
        return None
    for sublista in lista:
        if "M" not in sublista:
            if min == 0:
                min = int(sublista[0])
            else:
                aux = int(sublista[0])
                if  aux < min:
                    min = aux
    return min    
"""
        mate_solo
        Funcion que se encarga de detrmina si existe un cliente que solo quiera un color mate 
"""   
def mate_solo(lista):
    respuesta = False
    for sublista in lista:
        contador = 0
        for elemento in sublista:
            if "M" in elemento:
                contador += 1
        if contador == 1 and Nblancos(sublista) == 0:
            respuesta = True
            return respuesta
    return respuesta
"""
        minimo
        Funcion que se encarga de encontrar el coeficiente minimo de un lista de entero
"""
def minimo(lista):
    if not lista:
        return None  
    minimo = int(lista[0][:-1])       
    for color in lista:        
        numero = int(color[:-1])
        if numero < minimo:
            minimo = numero
    return minimo
"""
        maximo
        Funcion que se encarga de encontrar el coeficiente maximo de un lista de enteros
"""
def maximo(lista):
    maximo = 0
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo
"""
        minimo
        Funcion que se encarga de contar el numero de colores blancos que hay en una lista
"""
def mates_unic(lista):
    contador = 0   
    for elemento in lista:
        if "B" in elemento:
            contador += 1        
    return contador 
"""
        fila_unic
        Funcion que se encarga de devolver el indice donde se encuentra un valor en una lista
"""
def fila_unic(valor, lista):
    fila = 0
    for sublista in lista:
        for elemento in sublista:
            if valor in elemento:
                return fila   
        fila += 1   
    return fila
"""
        existe_solucion
        Funcion que se encarga de determinar si existe una solucion para el problema
"""
def existe_solucion(lista):
    filas_allmate = 0
    for sublista in lista:
        contador = 0
        for elemento in sublista:
            if "M" in elemento:
                contador += 1
        if contador == len(sublista):
            filas_allmate += 1
    if filas_allmate >1 and len(mates_iguales(lista)) == 0:
        return False
    else:
        return True
"""
        existe_solucion
        Funcion que se encarga de determinar si existe una solucion para el problema
"""
def mate_indice(lista):    
    for sublista in lista:
        for elemento in sublista:
            if "M" in elemento and blancos(sublista) == 0:
                 return int(elemento[0])

# -------------------------------------------------------------------------------------------------------
    # Interfaz
lista_clientes = []
contador1 = 0
contador2 = 0
num_clien = int(input("¿Cuantos clientes son?\n"))
num_colores = int(input("Dame el numero de colores\n"))
while(contador1<num_clien):    
    salida = False
    cliente = []
    while(salida != True):
        print(f"Elige una de las opciones para el cliente {contador1+ 1}:")
        print("1.Agregar colores")
        print("2.Ya no agregar colores\Pasar al siguiente cliente")
        opcion = input()
        if opcion == "1":
            numero = int(input("Dame el numero de color\n"))
            if 1<= numero <= num_colores :
                print("Elige una de estas opciones:")
                print("1.Mate")
                print("2.Blanco")
                tono = input() 
                if tono == "1" and str(numero) + "M" not in cliente:
                    cliente.append(str(numero) + "M")
                elif tono == "2" and str(numero) + "B" not in cliente:
                    cliente.append(str(numero) + "B")
                else:
                    print("Opcion invalida, puede ser que este repitiendo colores")
            else:
                print("Opcion invalida")
        elif opcion == "2":
            lista_clientes.append(cliente)
            cliente = []
            salida = True
        else:             
             print("Opcion invalida") 
    contador1 += 1     
mates = num_mates(lista_clientes)
# -------------------------------------------------------------------------------------------------------
    # Caso donde no hay colores mate
if mates == 0:    
    blancos = []
    respuesta = []
    for sublista in lista_clientes:
        blancos.append(int(minimo(sublista)))
        
    for i in range(int(maximo(blancos))):
        respuesta.append("B")
    
    print(respuesta)  
# -------------------------------------------------------------------------------------------------------
    # Caso donde existe solo un color mate
elif mates == 1:
    respuesta = []
    i = fila_unic("M",lista_clientes)
    unic = mates_unic(lista_clientes[i])
    # -------------------------------------------------------------------------------------------------------
    # Caso donde el color mate esta solo
    if unic == 0:
        blancos = []
        indice = 1
        for sublista in lista_clientes[i]:
            if "M" in sublista:
                valor = int(sublista[0])
        for sublista in lista_clientes:
            blancos.append(int(minimo(sublista)))
        
        for i in range(int(maximo(blancos))):
            if indice == valor:
                respuesta.append("M")
            else:
                respuesta.append("B") 
            indice += 1    
        
        print(respuesta)  
    # -------------------------------------------------------------------------------------------------------
    # Cualquier otro caso         
    else:    
        blancos = []
        for sublista in lista_clientes:
            blancos.append(int(minimo_blanco(sublista)))

        for i in range(int(maximo(blancos))):
           respuesta.append("B")                            
        
        print(respuesta)  
else:
    # -------------------------------------------------------------------------------------------------------
    # Caso donde existe mas de un color mate
    respuesta_existe = existe_solucion(lista_clientes)
    # -------------------------------------------------------------------------------------------------------
    # Se checa que la respuesta exista
    if respuesta_existe == True:
        respuesta = []
        blancos = []
        indice = 1
        # -------------------------------------------------------------------------------------------------------
        # Caso donde exista un color mate solo
        if mate_solo(lista_clientes) == True: 
           for sublista in lista_clientes:
               for elemento in sublista:
                   if "M" in elemento and Nblancos(sublista) == 0: 
                       valor = int(elemento[0]) 
           for sublista in lista_clientes:                                    
                blancos.append(int(minimo_blanco(sublista))) 
           if maximo(blancos) > valor:
               aux = int(maximo(blancos))
           else:
               aux = valor
           for i in range(aux):
               if indice == valor:
                   respuesta.append("M")
               else:
                   respuesta.append("B")
               indice += 1  
           
           print(respuesta)           
                                          
        else:
           # -------------------------------------------------------------------------------------------------------
           # Caso  toda una lista es de colores mate es decir un clinete pidio todos sus colores mate
           if fila_mates(lista_clientes) == True:               
               respuesta = []
               aux = int(maximo(mates_iguales(lista_clientes)))
               for i in range(aux):
                  if i == (aux-1):  
                     respuesta.append("M")
                  else:
                      respuesta.append("B") 
               
               print(respuesta) 
           else:
                 # -------------------------------------------------------------------------------------------------------
                 # Cualquier otro caso
                 for sublista in lista_clientes:
                    blancos.append(int(minimo_blanco(sublista)))
                 for i in range(maximo(blancos)):
                    respuesta.append("B")               
                 print(respuesta)                                      
    # -------------------------------------------------------------------------------------------------------
    # Caso donde no exista solucion                                                                  
    else:
        print("Es imposible de resolver")


       
    


       
          
        

        
        

    
































