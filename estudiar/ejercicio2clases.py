class Coche:
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometros_recorridos = 0
    
    def conducir(self, kilometros):
        # Calcular la cantidad de gasolina necesaria para recorrer los kilómetros
        gasolina_necesaria = kilometros / 10
        if gasolina_necesaria <= self.gasolina:
            # Si hay suficiente gasolina, recorremos toda la distancia
            self.kilometros_recorridos += kilometros
            self.gasolina -= gasolina_necesaria
            print(f"Has recorrido {kilometros} kilómetros. Te queda {self.gasolina:.2f} litros de gasolina.")
        else:
            # Si no hay suficiente gasolina, calculamos cuánto se puede recorrer
            kilometros_posibles = self.gasolina * 10
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"Te has quedado sin gasolina después de recorrer {kilometros_posibles:.2f} kilómetros.")
    
    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Has cargado {litros} litros de gasolina. Ahora tienes {self.gasolina:.2f} litros.")

# Ejemplo de uso
coche = Coche("Toyota", 5)
coche.conducir(30)  # Debería gastar 3 litros y quedar con 2 litros de gasolina.
coche.cargar_gasolina(10)  # Carga 10 litros más.
coche.conducir(100)  # Conducir 100 km, pero quedarse sin gasolina si no es suficiente.
