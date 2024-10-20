class Personaje:
    def __init__(self, nombre, ataque, vida):
        self.nombre = nombre
        self.ataque = ataque 
        self.vida = vida 
    
    def Ataque(self, personaje):
        if personaje.vida >= self.ataque:
            personaje.vida -= self.ataque
            print(f"{personaje.nombre} ha quedado con vida de: {personaje.vida}")
        elif personaje.vida <= self.ataque:
            personaje.vida -= self.ataque
            print(f"el {personaje.nombre} no ha sobrevivido al ataque de {self.nombre}")
    def Sobrevivir(self):
        return self.vida > 0
    
    def __str__(self):
        return f"el personaje {self.nombre} con vida {self.vida} y ataque {self.ataque}"

personaje1 = Personaje("guerrero", 5, 15)
personaje2 = Personaje("Ninja", 8, 15)
## primer ataque
personaje1.Ataque(personaje2)
personaje2.Ataque(personaje1)
## resultados primer ataque
print(personaje1)
print(personaje2)
## segundo ataque 
personaje1.Ataque(personaje2)
personaje2.Ataque(personaje1)
