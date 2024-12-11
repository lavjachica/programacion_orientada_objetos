### Un gimnasio en la ciudad de Castro ofrece diferentes membresías con
### descuentos para sus clientes. Las categorías de membresía son las
### siguientes: (50 Puntos)
### ● Estudiante: 20% de descuento.
### ● Empleado de Empresa: 10% de descuento.
### ● General: Sin descuento.

class Cliente:
    def __init__(self, nombre, tipo_cliente):
        self.__precio = 40000 ## lo protejo encasuplando, para que no sea facil de modificar sin un metodo correspondiente 
        self.nombre = nombre ### no es importante en terminos de encapsulacion o proteccion de datos
        self.__tipo_cliente = tipo_cliente ## encapsular porque esta informaicon me guarda el tipo de cliente que es y por ende si obtendra o no un descuento 
    #### Inicializo los descuentos en Variables de clase, no es necesario colocar el sin descuento.
    ### los dejo como variables de clase porque no varian, Son descuentos fijos 
    descuento_estudiante = 0.20
    descuento_empleado = 0.10 
    ### organizo los descuentos como variable de clase ya que me permite operar de mejor manera que un diccionario
    @property
    def tipo_cliente(self):
        return self.__tipo_cliente
    @property
    def precio(self):
        return self.__precio   ### estos me permiten acceder al setter y utilizarlo
        
    @precio.setter
    def precio(self, valor):
        assert valor >= 0, "El precio no puede ser negativo."
        self.__precio = valor
    ### Accesores y mutadores, con un setter logro modificar los valores de la membresia, usamos variables de clase para no modificar la logica de los descuentos
    ### este setter me calcula el precio final de todas mis funciones
class Gym:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = {}
        
    def agregar_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.clientes[cliente.nombre] = cliente
            print(f"El cliente se ha agregado con exito")
        else:
            print(f"El cliente que deseas agregar no pertenece a la clase Clientes")
        
    def set_precio(self, Membresia):
        assert Membresia.precio > 0, "El valor de la membresia no puede ser cero" ## asertos necesarios
        if Membresia.tipo_cliente.lower() == "estudiante":
            nuevo_precio_estudiante = Membresia.precio - (Membresia.precio * Cliente.descuento_estudiante)
            print(f"Buenos días {Membresia.nombre} el valor normal de venta de Membresía es de {Membresia.precio} y por ser un cliente de tipo {Membresia.tipo_cliente} se le ha generado un descuento.")
            print(f"El nuevo valor de su Membresia en el gimnasio es de: ${nuevo_precio_estudiante}")
        elif Membresia.tipo_cliente.lower() == "empleado":
            nuevo_precio_empleado = Membresia.precio - (Membresia.precio * Cliente.descuento_empleado)
            print(f"Buenos días {Membresia.nombre} el valor normal de venta de Membresía es de {Membresia.precio} y por ser un cliente de tipo {Membresia.tipo_cliente} se le ha generado un descuento.")
            print(f"El nuevo valor de su Membresia en el gimnasio es de: ${nuevo_precio_empleado}")
        else:
            precio_normal = Membresia.precio
            print(f"Buenos días {Membresia.nombre} no cumples con los requisitos patra obtener un descuento")
            print(f"El nuevo valor de su Membresia en el gimnasio es de: ${precio_normal}")
            
            
cliente1 = Cliente("Fernanda", "estudiante")
cliente2 = Cliente("Hector", "empleado")
cliente3 = Cliente("Maria", "visitante")

Gimnasio = Gym("Pacific")

Gimnasio.agregar_cliente(cliente1)
Gimnasio.agregar_cliente(cliente2)
Gimnasio.agregar_cliente(cliente3)

Gimnasio.set_precio(cliente1)
Gimnasio.set_precio(cliente2)
Gimnasio.set_precio(cliente3)