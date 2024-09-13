import math ## biblioteca matematica para las funciones 

class FuncionTrigonometrica: 
    def __init__(self, tipo, amplitud, periodo):
        self.tipo = tipo
        self.amplitud = amplitud
        self.periodo = periodo

seno = FuncionTrigonometrica("seno",2, 4 * math.pi)
coseno = FuncionTrigonometrica("coseno", 1, 2 * math.pi)
tangente = FuncionTrigonometrica("tangente",1, math.pi)


