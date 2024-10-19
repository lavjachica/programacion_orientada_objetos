class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre 
        self.vida = vida 
        self.ataque = ataque 

    def atacar(self, otro_personaje): 
       otro_personaje.vida -= self.ataque
       print(f"{self.nombre} ha atacado a vida de {otro_personaje.vida}")

    def esta_vivo(self):
       return self.vida > 0
    def estado(self):
        print(f"{self.nombre}, vida {self.vida} y ataque {self.ataque}")

personaje1 = Personaje("Guerrero", 100, 15)
personaje2 = Personaje("Mago", 80, 20)

while personaje1.esta_vivo() and personaje2.esta_vivo():
    personaje1.atacar(personaje2)
    personaje1.estado()
    personaje2.estado()
    

    if not personaje2.esta_vivo():
        print(f"{personaje1.nombre} ha sido derrotado")
        break
    personaje2.atacar(personaje1)
    personaje1.estado()
    personaje2.estado()
    print()

    if not personaje1.esta_vivo():
        print(f"{personaje2.nombre} ha sido derrotado")
        break

    


