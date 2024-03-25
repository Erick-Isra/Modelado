
class Producto:
    """
    Metodo constructor de la clase Producto
    No necesita parametros
    Devuelve un objeto de la clase Producto
    """
    def __init__(self):
        self.id = None
        self.nombre = None
        self.precio = None
        self.cantidad = None
        self.dia = None
        self.mes = None
        self.año = None
    #-----------------------------------------------------------------------------------------------
        #Getters

    """    
        Devuelve el nombre del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo nombre del prodcuto.
        
    """
    def getNombre(self): 
        return self.nombre
    
    """    
        Devuelve el precio del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo precio del prodcuto.
        
    """
    def getPrecio(self):
        return self.precio
    
    """    
        Devuelve el id del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo id del prodcuto.        
    """
    def getId(self):
        return self.id
    
    """    
        Devuelve la cantidad del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo cantidad del prodcuto.        
    """
    def getCantidad(self):
        return self.cantidad
    
    """    
        Devuelve el dia de caducidad del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo dia del prodcuto.
        
    """
    def getDia(self):
        return self.dia
    
    """    
        Devuelve el mes de cadudcidad del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo mes del prodcuto.
        
    """
    def getMes(self):
        return self.mes
    
    """    
        Devuelve el año de caducidad del producto.
        param:
            No necesita parametros
        returns:
            El valor del atributo año del prodcuto.
        
    """
    def getAño(self):
        return self.año
    
    #------------------------------------------------------------------------------------------------
        #Setters
    
    """
        Designa un nuevo nombre para una instancia de la clase Producto.
        param:
            str nombre = El nuevo nombre a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setNombre(self, nombre):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacio")
        else:
            self.nombre = nombre

    """
        Designa un nuevo precio para una instancia de la clase Producto.
        param:
            float precio = El nuevo precio a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setPrecio(self, precio):
        try:
            self.precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser un numero")       
    
    """
        Designa un nuevo id para una instancia de la clase Producto.
        param:
            str id = El nuevo id a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setid(self, id):
        try:
           if id == "":
              raise ValueError("El id no puede estar vacio")
              return
           else:
              for char in id:
                if not char.isalpha():
                  raise ValueError("El id no puede contener numeros")    
                  return                      
           self.id = id
        except ValueError:
            raise ValueError("Id en formato incorrecto")
    

    """
        Designa una nueva cantidad para una instancia de la clase Producto.
        param:
            int cantidad = La nueva cantidad a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setCantidad(self, cantidad):
        try:
            num = int(cantidad)
            can = "(" + str(num) + " unidades" + ")"
            self.cantidad = can
        except ValueError:
            raise ValueError("La cantidad debe ser un numero entero")    
    
    """
        Designa un nuevo dia para una instancia de la clase Producto.
        param:
            int dia = El nuevo dia a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setDia(self, dia):
        try:
            dia = int(dia)
            if dia >=1 and dia <=31:
                self.dia = dia
            else:
                raise ValueError("El dia ingresado no es válido")
            
        except ValueError:
            raise ValueError("Dia invalido")
            
        
    """
        Designa un nuevo mes para una instancia de la clase Producto.
        param:
            int mes = El nuevo mes a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setMes(self, mes):
        try:
            mes = int(mes)
            if mes >= 1 and mes <= 12:
                self.mes = mes
            else:
                raise ValueError("El mes ingresado no es válido")
        except ValueError:
           raise ValueError("El mes ingresado no es válido")        
    
    """
        Designa un nuevo año para una instancia de la clase Producto.
        param:
            int año = El nuevo año a asignar a una instancia.
        returns:
            No devuelve nada
    """
    def setAño(self, año):
        try:
          año = int(año)
          if año >= 2025 and año <= 2027:
            self.año = año
          else:
              raise ValueError("El año ingresado no es válido")
        except ValueError:
           raise ValueError("El año ingresado no es válido")


    