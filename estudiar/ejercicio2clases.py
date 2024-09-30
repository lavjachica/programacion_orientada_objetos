##Crea la clase Coche que contenga las siguientes propiedades:
##marca (string): La marca del coche.
##gasolina (float): La cantidad de gasolina disponible en el coche.
##La clase tendrá un método llamado conducir() que recibirá como argumento el número de kilómetros a
##recorrer y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. Por cada 10
##kilómetros recorridos, se restará 1 litro de gasolina al valor de la propiedad gasolina. Si la gasolina no es
##suficiente para recorrer la distancia solicitada, el coche conducirá solo hasta donde alcance la gasolina y
##mostrará un mensaje indicando que se ha quedado sin gasolina.
##Además, la clase contendrá otro método llamado cargar_gasolina() que recibirá como argumento los
##litros de gasolina que se desean agregar al coche, sumando estos litros al valor de la propiedad gasolina.
class Coche:
    def __init__(self, marca, gasolina, kilometros_recorridos):
        self.marca = marca 
        self.gasolina = gasolina
        self.kilometros_Recorridos = kilometros_recorridos
    def conducir(self, kilometros):
        litros_gasolina = kilometros / 10 
        
        
        if litros_gasolina <= self.gasolina:
            self.kilometros_Recorridos += kilometros
            self.gasolina -= litros_gasolina
            print(f"tu coche ha recorrido {self.kilometros_Recorridos}km y tiene gasolina {self.gasolina}L")
        else:
            km_posibles = self.gasolina * 10
            self.kilometros_Recorridos += km_posibles
            self.gasolina = 0
            print(f"Tu coche ha quedado sin gasolina {self.gasolina}")

coche1 = Coche("toyota", 100,2)

coche1.conducir(100)



        
