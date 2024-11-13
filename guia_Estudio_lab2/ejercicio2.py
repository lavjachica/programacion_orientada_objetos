class Cliente:
    def __init__(self, nombre, suscripcion, precio, tiempo):
        self.__nombre = nombre
        self.__suscripcion = suscripcion
        self.__precio = precio
        self.tiempo = tiempo
      
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def suscripcion(self):
        return self.__suscripcion

    @property
    def precio(self):
        return self.__precio



class Gym:
    
    descuento_especial = 0.30 ## se le aplicara un 30% de descuento al cliente 
    
    def __init__(self, nombre):
        self.informacion_cliente = {}
        self.nombreGym = nombre
        
        
    def agregar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
           self.informacion_cliente[cliente.nombre] = cliente  
           print(f"se ha agregado con exito el cliente al sistema del Gym.") 
        else:
           print("El cliente que deseas agregar no pertenece a la clase clientes.") 

    def set_precio(self, cliente):
        if cliente.suscripcion.lower() == "anual":
            nuevo_precio = cliente.precio - (cliente.precio * self.descuento_especial)
            print(f"El precio del Cliente {cliente.nombre} es de {nuevo_precio} debido a escoger suscripcion Anual")
            
            return nuevo_precio
        else: 
            print(f"La suscripcion no cumple con los requisitos como para obtener un descuento")
            return cliente.precio
             
    @staticmethod
    def descuento_inicial(suscricpcion):
        if suscricpcion.tiempo.lower() == "nuevo":
            precio_para_nuevos = suscricpcion.precio - (suscricpcion.precio * 0.10)
            print(f"Tu precio con descuento de Bienvenida es de ${precio_para_nuevos}")
            return precio_para_nuevos
        else:
            print(f"No cumples con los requisitos para un descuento de Bienvenida, pero existen otros descuentos disponibles!")
            return suscricpcion.precio
   
cliente1 = Cliente("Raul","anual", 130000, "Nuevo")
gym = Gym("Pacific")

gym.agregar_cliente(cliente1)
gym.set_precio(cliente1)
gym.descuento_inicial(cliente1)
gym.aplicar_descuentos(cliente1)