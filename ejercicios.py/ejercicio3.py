### Implementar una clase Fraccion que represente una fracción matemática con numerador y
### denominador. Además se debe crear varios métodos mágicos que permitan operar, comparar, y mostrar
### las fracciones de manera intuitiva. La clase debe poseer los siguientes métodos mágicos:
class Fraccion: 
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __str__(self): 
        return f"La fraccion tiene como numerador {self.numerador} y  denominador {self.denominador}"
    def __add__(self,frac):
        return Fraccion(
            self.numerador + frac.numerador,
            self.denominador + frac.denominador
        )

    
fraccion1= Fraccion(1,2)
fraccion2= Fraccion(4,8)


fraccion3 = fraccion1 + fraccion2
print(fraccion3)