## Se solicita crear una clase ReservaHostal que permita a los usuarios crear reservas de
## habitaciones en un hostal. Cada reserva tendrá atributos como el nombre del cliente, la fecha
## de entrada, la fecha de salida, y el número de habitación. Implementar los siguientes
## requerimientos:
## Métodos:
## ● Un método para calcular la duración de la estadía del cliente.
## ● Un método mágico para mostrar la información de la reserva.
## ● Un método para cambiar la fecha de salida.
## Se debe eliminar un objeto ReservaHostal, además de imprimir un mensaje indicando que la
## reserva ha sido cancelada.
class ReservaHotel:
    def __init__(self, NombreCliente, FechaEntrada, FechaSalida, habitacion):
        self.nombre = NombreCliente
        self.entrada = FechaEntrada
        self.salida = FechaSalida
        self.habitacion = habitacion
    def duracion(self):
        fecha1 = (self.salida[0] + self.salida[1]*30 + self.salida[2]*365)
        fecha2 = (self.entrada[0] + self.entrada[1]*30 + self.entrada[2]*365)
        cantidad_dias = fecha1 - fecha2 
        print(f"la cantidad de dias en el hotel es de {cantidad_dias} dias con entrada {self.entrada} y salida {self.salida}")
    def __str__(self):
        return f"SR/SRA {self.nombre}, con entrada {self.entrada} y salida {self.salida} su habitacion es la N°{self.habitacion}"
    
    def nuevaSalida(self, *nuevafecha):
        self.salida = list(nuevafecha)
    def eliminarHuesped(self, cliente):
        cliente = None
        print(f"el cliente ha sido eliminado de la base de datos del Hotel")

cliente1 = ReservaHotel("Raul", (3,6,24), (8,6,24), 7)
cliente1.duracion()
print(cliente1)
cliente1.nuevaSalida(15,6,24)
cliente1.duracion()
cliente1.eliminarHuesped(cliente1)
