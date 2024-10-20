class Planta:
    def __init__(self, tipo, crecimiento, agua, sol, color, fertilizante):
        self.__tipo = tipo ##privado porque el tipo de planta siempre sera el mismo
        self.__crecimiento = crecimiento  ### el crecimiento siempre sera el mismo
        self.agua = agua ## puede usar menos o mas agua dependiendo la exposicion al sol
        self.sol = sol ## no es constante
        self.color = color  ## no es constante 
        self.fertilizante = fertilizante
    ###creando metodo para necesidad de riego en funcion de la luz solar recibida 
   