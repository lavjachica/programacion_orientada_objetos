import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        """Simplifica la fracción dividiendo numerador y denominador por su máximo común divisor."""
        divisor_comun = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor_comun
        self.denominador //= divisor_comun

    def __str__(self):
        """Devuelve la representación en cadena de la fracción."""
        if self.denominador == 1:
            return f"{self.numerador}"
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra):
        """Suma dos fracciones y devuelve el resultado como una nueva fracción."""
        nuevo_numerador = (self.numerador * otra.denominador) + (otra.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __mul__(self, otra):
        """Multiplica dos fracciones y devuelve el resultado como una nueva fracción."""
        nuevo_numerador = self.numerador * otra.numerador
        nuevo_denominador = self.denominador * otra.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otra):
        """Compara dos fracciones para determinar si son equivalentes."""
        return (self.numerador * otra.denominador) == (self.denominador * otra.numerador)

# Ejemplo de uso
f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

# Mostrar las fracciones
print(f"Fracción 1: {f1}")  # Salida: 1/2
print(f"Fracción 2: {f2}")  # Salida: 3/4

# Sumar fracciones
f3 = f1 + f2
print(f"Suma: {f3}")  # Salida: 5/4

# Multiplicar fracciones
f4 = f1 * f2
print(f"Producto: {f4}")  # Salida: 3/8

# Comparar fracciones
f5 = Fraccion(2, 4)
print(f"Fracción 1 es igual a Fracción 5: {f1 == f5}")  # Salida: True
