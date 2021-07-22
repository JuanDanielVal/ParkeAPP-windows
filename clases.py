class Vehiculo:
    
    def __init__(self, placa, marca, color, tipo):
        self.__placa = placa
        self.__marca = marca
        self.__color = color
        self.__tipo = tipo

            
    def getPlaca(self):
        return self.__placa 
    
    def getMarca(self):
        return self.__marca
    
    def getColor(self):
        return self.__color
    
    def getTipo(self):
        return self.__tipo
    
     
        
class Camioneta(Vehiculo):
    
    pass

class Deportivo(Vehiculo):
    
    pass

class Clasico(Vehiculo):
    
    pass

class Moto(Vehiculo):
    
    def __init__(self, placa, marca, color, tipo):
        Vehiculo.__init__(self, placa, marca, color, tipo)
        

class Moto_AltoCC(Moto):
    
    pass

class Moto_BajoCC(Moto):
    
    pass

class Usuarios():
    
    def __init__(self, usuario, password):
        self.__nombre_usuario = usuario
        self.__contrasena = password
        
    def getUser(self):
        return self.__nombre_usuario
    
    def getPass(self):
        return self.__contrasena

    




