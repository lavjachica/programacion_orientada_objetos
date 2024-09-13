import math
import matplotlib.pyplot as plt

class FuncionTrigonometrica:
    def __init__(self, tipo, amplitud, periodo):
        self.tipo = tipo
        self.amplitud = amplitud
        self.periodo = periodo

    def evaluar(self, x):
        if self.tipo == 'seno': ## si es del tipo seno, entonces utiliza math.sin 
            return self.amplitud * math.sin(x * 2 * math.pi / self.periodo) ## usamos las funciones que entrega la biblioteca ''math'', despues definimos amplitud y periodo
        elif self.tipo == 'coseno':
            return self.amplitud * math.cos(x * 2 * math.pi / self.periodo)
        elif self.tipo == 'tangente':
            return self.amplitud * math.tan(x * 2 * math.pi / self.periodo)
        else:
            raise ValueError("Ingrese una funcion valida")

    def graficar(self, x_min, x_max, num_puntos=1000): ## la cantidad de puntos elevada es para que se vea suave la grafica
        x = [x_min + (x_max - x_min) * i / (num_puntos - 1) for i in range(num_puntos)] ##x_min + (x_max- x_min) calcula el intervalo total, que se divide por el num de puntos, el cual da la distancia entre ellos, luego se multiplica por i, que i itera sobre el rango de num_puntos., osea la cantidad de puntos
        y = [self.evaluar(xi) for xi in x]                    ## osea genera los puntos, el espaciado y la cantidad, se utiliza el - 1 pq ejemplo, hay 4 letras, por lo tanto habra 3 espacios, sino calcula 1 extra             
        plt.plot(x, y) ## llama a evaluar, crea un  xi que itere sobre x, dependiendo de la funcion sera el resultado de x
        plt.title(f'Función {self.tipo.capitalize()}') ## muestra en mayusculas el tipo de funcion 
        plt.xlabel('x') ##eje x
        plt.ylabel('f(x)') ## en funcion de x
        plt.grid(True) ## muestra con una cuadricula
        plt.show() ## muestra el grafico

    def __str__(self):
        return f'Función {self.tipo.capitalize()} con amplitud {self.amplitud} y período {self.periodo}'
### metodo magico que muestra los detalles de cada funcion 
    def valor_critico(self):
        if self.tipo in ['seno', 'coseno']:
            return (self.amplitud, -self.amplitud)  # los valores maximos y minimos, solo en cos y sen 
        elif self.tipo == 'tangente':
            return 'Segun lo investigado, la tangente no alcanza valores maximos y minimos ya que puede crecer infinitamente'
        else:
            raise ValueError("Tipo de función no soportado")

# graficar funcion seno 
amplitud = 1           ### valores generales entregados a amplitud y periodo
periodo = math.pi
funcion = FuncionTrigonometrica('seno', amplitud, periodo) ## detallamos la funcion
print(funcion)
print("Valor crítico:", funcion.valor_critico()) ##llamamos metodo valor critico 
funcion.graficar(-2*math.pi, 2*math.pi)  ## entregamos los valores maximos y minimos a graficar 
# funcion tangente
amplitud = 1
periodo = math.pi
funcion = FuncionTrigonometrica('tangente', amplitud, periodo)
print(funcion)
print("Valor crítico:", funcion.valor_critico())
funcion.graficar(-2*math.pi, 2*math.pi)
# coseno 
amplitud = 1
periodo = math.pi
funcion = FuncionTrigonometrica('coseno', amplitud, periodo)
print(funcion)
print("Valor crítico:", funcion.valor_critico())
funcion.graficar(-2*math.pi, 2*math.pi)
