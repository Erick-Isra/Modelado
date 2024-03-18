#Clase plato
class Plato:
    def __init__(self, lados, medidalados):
        self.lados = lados
        self.medidalados = medidalados
    
    def get_lados(self):
        return self.lados
    
    def get_medida_lados(self):
        return self.medidalados
    
#Clase hormiga
class Hormiga:
    def __init__(self, velocidad):
        self.velocidad = velocidad
    
    def getvelocidad(self):       
        return self.velocidad

hormiga_obj = Hormiga(6) 
plato_obj = Plato(8, 14) 
#Funcion que cuenta cuansta veces se detien la hormiga en un arista
def aristas(inicio, vueltas, arista):
    contador = 0
    cont_vueltas = 0
    while cont_vueltas < vueltas:
        inicio += hormiga_obj.getvelocidad()      
        if inicio % arista == 0:
            contador += 1                              
        cont_vueltas += 1        
    return contador

lista_aristas = [14, 28, 42, 56, 70, 84, 98, 112]
lista_nombres = ["B", "C", "D", "E", "F", "G", "H", "A"]

for i in range(len(lista_aristas)):
    print(f"La hormiga llega al arista {lista_nombres[i]} {aristas(106, 2000, lista_aristas[i])} veces.")
print("Notemos que en ninguna otra asrista la hormiga para 34 veces")