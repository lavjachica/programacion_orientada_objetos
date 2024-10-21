class Planta:
    def __init__(self, tipo, crecimiento, agua, vida, necesidad):
        self.__tipo = tipo ##privado porque el tipo de self siempre sera el mismo
        self.__crecimiento = crecimiento  ### el crecimiento siempre sera el mismo
        self.agua = agua ## puede usar menos o mas agua dependiendo la exposicion al sol
        self.vida = vida #vida de la self
        self.necesidad = necesidad 

    def NecesidadRiego(self, dias):
        if self.agua >=0:
            self.agua -= dias 
            print(f"Necesitas regar pronto el/la {self.__tipo} el agua es de {self.agua}L")
        else:
            print(f"debes de regar tu self antes de la cantidad de dias {dias}, ya que consumen un litro diario, y solo tiene {self.agua}L")
        
    def Riego(self, regar):
        if self.necesidad == "humedo":
            if regar <= 3:
               self.agua += regar
               print(f"el agua ahora es de {self.agua}L")
            else:
                print(f"la cantidad de agua que deseas regar a la self {self.__tipo} es demasiada, prueba con menos de 2L")
        elif self.necesidad == "soleado":
            if regar <= 5:
               self.agua += regar 
               print(f"el agua ahora es de {self.agua}L")
            else:
                print(f"las plantas de tipo {self.__tipo} no necesitan mas de 5L")
         
        
        #### controla el estado de crecimiento de las plantas 
    def crecimiento(self):
        if self.__crecimiento == "semilla" and self.agua >= 1 :
            self.__crecimiento = "brote"
            print(f"tu planta {self.__tipo} ha crecido a {self.__crecimiento}")
        elif self.__crecimiento == "brote" and self.agua >= 2 :
            self.__crecimiento = "self adulta"
            print(f"tu planta {self.__tipo} ha crecido a {self.__crecimiento}")
        elif self.__crecimiento == "self adulta" and self.agua >= 3:
            self.__crecimiento = "self vieja"
            print(f"tu planta {self.__tipo} ha crecido a {self.__crecimiento}")
        else:
            print(f"probablemente a {self.__tipo} le falte agua, tiene {self.agua} litros")

class Jardin: 
    def __init__(self, *humedo, soleado):
        self.humedo = list(humedo)
        self.soleado = list(soleado) 
    
    def agregarPlantasHumedo(self, Nuevaplanta):
        if Nuevaplanta.necesidad == "humedo":
            self.humedo.append(Nuevaplanta)
        else:
            print(f"no se puede agregar {Nuevaplanta.nombre} porque no pertenece al clima humedo del area del jardin")
    
    def agregarPlantasSoleado(self, Plantanueva):
        if Plantanueva.necesidad == "soleado":
            self.soleado.append(Plantanueva)
        else:
            print(f"no se puede agregar {Plantanueva.nombre} porque no pertenece al clima soleado del area del jardin")

class Herramientas:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
    def __str__(self):
        return f"Herramienta: {self.tipo} - cantidad :{self.cantidad}"
Herramientas1= Herramientas("pala", 8)
Herramientas2= Herramientas("picota", 10)
Herramientas3= Herramientas("guantes", 25)
    

for herramientas in (Herramientas1, Herramientas2, Herramientas3):
    print(herramientas)

planta1 = Planta("Chilcon", "semilla", 2, 10, "humedo")
planta2 = Planta("Helecho", "brote", 1, 15, "humedo")
planta3 = Planta("Suculenta","self adulta", 2, 20, "soleado")
planta4 = Planta("Cactus", "self vieja", 1, 50, "soleado")

planta1.NecesidadRiego(2)
planta1.Riego(8)
planta1.Riego(2)
planta1.crecimiento()