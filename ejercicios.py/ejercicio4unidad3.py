
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)  # Usamos 3.14 como aproximación de pi

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

class PentagonRegular:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        apotema = (self.lado * 1.720)  # el apotema se aproxima c:
        return (5 * self.lado * apotema) / 2

# Metodo compartido entre todas las clases
def mostrar_area(figura):
    area = figura.calcular_area()  # Llama al método calcular_area()
    print(f"El área de la figura es: {area:.2f}")

if __name__ == "__main__":
    # instancia
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(4, 3)
    cuadrado = Cuadrado(4)
    trapecio = Trapecio(5, 3, 4)
    pentagono = PentagonRegular(6)

    # implementar c:
    mostrar_area(circulo)
    mostrar_area(rectangulo)
    mostrar_area(triangulo)
    mostrar_area(cuadrado)
    mostrar_area(trapecio)
    mostrar_area(pentagono)
