# Clase base para todos los vehículos
class Vehiculo:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def mover(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clases derivadas para tipos de vehículos
class Terrestre(Vehiculo):
    def mover(self):
        return f"{self.nombre} (terrestre) se mueve a {self.velocidad} km/h."

class Acuatico(Vehiculo):
    def mover(self):
        return f"{self.nombre} (acuático) navega a {self.velocidad} km/h."

class Aereo(Vehiculo):
    def mover(self):
        return f"{self.nombre} (aéreo) vuela a {self.velocidad} km/h."

# Clases híbridas que combinan características
class TerrestreAcuatico(Terrestre, Acuatico):
    def mover(self):
        return f"{self.nombre} (terrestre-acuático) se mueve a {self.velocidad} km/h."

class TerrestreAereo(Terrestre, Aereo):
    def mover(self):
        return f"{self.nombre} (terrestre-aéreo) se mueve a {self.velocidad} km/h."

# Función para simular el movimiento de los vehículos
def simular_movimiento(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo.mover())

# Código principal
if __name__ == "__main__":
    # Crear instancias de vehículos
    vehiculos = [
        Terrestre("Coche", 120),
        Acuatico("Barco", 80),
        Aereo("Avión", 600),
        TerrestreAcuatico("Amfibio", 100),
        TerrestreAereo("Coche Volador", 150)
    ]

    # Simular movimiento
    simular_movimiento(vehiculos)
