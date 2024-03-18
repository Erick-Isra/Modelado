def subcadena(cadena1, cadena2):
    comun_mas_larga = ""
    for i in range(len(cadena1)):
        for j in range(len(cadena2)):
            k = 0
            subcadena = ""
            while (i + k < len(cadena1) and j + k < len(cadena2) and
                   cadena1[i + k] == cadena2[j + k]):
                subcadena += cadena1[i + k]
                k += 1
            if len(subcadena) > len(comun_mas_larga):
                comun_mas_larga = subcadena
    return comun_mas_larga

#Se debe modificar el path para que lea el archivo
def maxsub():
    file = open("/home/erickisrael/Documentos/Practica1/P1/ejercicio2.txt", "r") 
    parejas = int(file.readline())  
    contador = 0
    while (contador < parejas):
        cadena1 = file.readline().strip()  
        cadena2 = file.readline().strip()  
        print(subcadena(cadena1, cadena2))
        contador += 1
    file.close()

maxsub()






    




