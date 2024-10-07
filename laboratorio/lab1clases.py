class Personaje:
    def __init__(self, nombre, vida, pts_ataque):
        self.nombre = nombre
        self.vida = vida 
        self.pts_ataque = pts_ataque
    def atacar(self, ataque):
        personaje1 = self.pts_ataque
        personaje2 = self.vida
        (self.vida - self.pts_ataque) * ataque
        print(f"Te han atacado {ataque} cantidad de veces")
        
        
    def vida_final(self): 
        if self.vida > 0:
            print(f"el personaje {self.nombre} ha sobrevivido al ataque, vida: {self.vida}")
        else:
            print(f"el personaje no ha sobrevivido al ataque")



personaje1= Personaje("Ninja", 50, 25)
personaje2= Personaje("Kong", 300, 50)

personaje1.atacar(2)
personaje1.vida_final()
personaje2.atacar(1)
personaje2.vida_final()