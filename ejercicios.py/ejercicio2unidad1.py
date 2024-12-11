
class Coche():
    def __init__(self,marca,gasolina):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0.0

    # Metodo para conducir
    def conducir(self,kilometros):
        gasolina_necesaria = kilometros /10  #por 1 litro de bencina recorre 10 km
        if self.gasolina >= gasolina_necesaria:
            self.kilometros_recorridos += kilometros
            self.gasolina -= gasolina_necesaria
            print(f"Has conducido {kilometros} kilómetros. Gasolina restante {self.gasolina:.2f} Litros")
        
        else:
            kilometros_posibles = self.gasolina * 10 
            self.kilometros_recorridos += kilometros_posibles
            self.gasolina = 0
            print(f"Solo pudiste conducir {kilometros_posibles:.2f} kilómetros y te has quedado sin gasolina")
        
    #Metodo para cargar gasolina
    def cargar_gasolina(self,litros):
        self.gasolina += litros
        print(f"Has cargado {litros} Litros de gasolina, tu gasolina actual es de: {self.gasolina:.2f} Litros")

# instancias
coche1 = Coche("tucutucu", 10)
coche2= Coche("cars", 5)

coche1.conducir(50)
coche1.conducir(100)

coche2.conducir(60)
coche2.cargar_gasolina(1) 
coche2.conducir(10) 

