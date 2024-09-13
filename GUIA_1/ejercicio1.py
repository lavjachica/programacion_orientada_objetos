#ejercicio 1

class ReservaHostal:
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, numero_habitacion):
        # Variables para guardar la info de la reserva
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_habitacion = numero_habitacion

    def calcular_duracion_estadia(self):
       
        fecha_entrada = list(map(int, self.fecha_entrada.split('-')))
        fecha_salida = list(map(int, self.fecha_salida.split('-')))
        
        # Calcular los días 
        dias_entrada = fecha_entrada[0] * 365 + fecha_entrada[1] * 30 + fecha_entrada[2]
        dias_salida = fecha_salida[0] * 365 + fecha_salida[1] * 30 + fecha_salida[2]
        
        # Ajustar por años bisiestos (simplifico)
        dias_entrada += fecha_entrada[0] // 4
        dias_salida += fecha_salida[0] // 4
        
        # Devolver la diferencia en días
        return dias_salida - dias_entrada

    def cambiar_fecha_salida(self, nueva_fecha_salida):
      
        self.fecha_salida = nueva_fecha_salida

    def __str__(self):
       
        return (f"Reserva de {self.nombre_cliente}\n"
                f"Habitación: {self.numero_habitacion}\n"
                f"Fecha de entrada: {self.fecha_entrada}\n"
                f"Fecha de salida: {self.fecha_salida}\n"
                f"Duración de la estadía: {self.calcular_duracion_estadia()} días")

    def cancelar_reserva(self):
        """Elimina la reserva e imprime un mensaje de cancelación."""
        print(f"Reserva de {self.nombre_cliente} en la habitación {self.numero_habitacion} ha sido cancelada.")
        del self


# Ejemplo:
reserva = ReservaHostal("Juan Pérez", "2024-09-07", "2024-09-10", 101)
print(reserva)
print("Duración de la estadía:", reserva.calcular_duracion_estadia(), "días")
reserva.cambiar_fecha_salida("2024-09-12")
print("\n Después de cambiar la fecha de salida:")
print(reserva)

# Cancelar la reserva
reserva.cancelar_reserva()