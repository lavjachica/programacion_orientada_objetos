#Crea una clase llamada Rectangulo que tenga los siguientes atributos:

#base (float)
#altura (float)
#Implementa los siguientes métodos:

#area(): que calcule y devuelva el área del rectángulo.
#perimetro(): que calcule y devuelva el perímetro del rectángulo.
#Crea una instancia de Rectangulo y muestra el área y el perímetro.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    def Area (self):
        area_rectangulo = self.base * self.altura
        print(f"el area del rectangulo es de: {area_rectangulo}")
    def Perimetro (self):
        perimetro_rectangulo = ((self.base*2)+(self.altura*2))
        print(f"el perimetro del rectangulo es de: {perimetro_rectangulo}")

rectangulo1 = Rectangulo(2, 5)
rectangulo1.Area()
rectangulo1.Perimetro()