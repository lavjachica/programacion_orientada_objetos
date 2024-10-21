class Vehiculo:
    def __init__(self, modelo, marca, año, disponible):
        self.modelo = modelo
        self.marca = marca 
        self.año = año
        self.__disponible = True

    def vender(self):
        if self.__disponible:
            self.__disponible = False
            print(f"el vehiculo {self.modelo} ha sido vendido, disponibilidad: {self.__disponible}")
    
    def __str__(self):
        return f"Vehiculo {self.modelo} de la marca {self.marca} con año {self.año} y disponibilidad {self.__disponible}"

class Consecionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []
    
    def agregarVehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
            print(f"el vehiculo {vehiculo.modelo} ha sido agregado con exito")
        else:
            print(f"el objeto ha agregar no pertenece a la clase Vehiculo.")
        
    def mostrarVehiculos(self):
        for lista in self.vehiculos:
            print(lista)
    
consecionaria = Consecionaria("Chiloe Motores")

camioneta= Vehiculo("Toyota Pickup", "toyota", 2023, True)
auto = Vehiculo("sedan", "hyundai", 2015, True)
auto2 = Vehiculo("i10", "hyundai", 2022, True)

consecionaria.agregarVehiculo(camioneta)
consecionaria.agregarVehiculo(auto)
consecionaria.agregarVehiculo(auto2)
## metodo para mostrar vehiculos 
consecionaria.mostrarVehiculos()
## metodo para vender vehiculo
auto.vender()
print(auto)