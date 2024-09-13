import matplotlib.pyplot as plt  ## importamos la biblioteca para poder crear el grafico 

class Cuerpo:
    def __init__(self, x0, v):
        self.x0 = x0  
        self.v = v  ## 𝑥 = 𝑥0 + 𝑣𝑡  


    def calcular_posicion(self, t):   ### SimuladorMovimiento simula el movimiento y grafica la posición del
        return self.x0 + self.v * t    ## objeto en función del tiempo utilizando la fórmula del MRU. 
## esta es la funcion del tiempo

class SimuladorMovimiento: ### creamos otra clase
    def __init__(self, cuerpo):   ## esto le permite al simulador de movimiento operar con nuestra instancia anterior
        self.cuerpo = cuerpo
    def simular(self, tiempoMax):
        tiempos = list(range(tiempoMax + 1))  # tiempo maximo para poder darle segundos de duracion c:, 
        posiciones = []  #### se crea una lista para almacenar los tiempos que el rango maximo entrega, ej max 10 seg
        
        for t in tiempos:
            P = self.cuerpo.calcular_posicion(t)  ## calcula la posicion con el metodo creado en la clase Cuerpo(t)
            posiciones.append(P) ## agregra las posiciones a la lista vacia c: 
        

        # Graficar las posiciones
        plt.figure(figsize=(10, 5)) ## tamaño del grafico
        plt.plot(tiempos, posiciones, marker='o', linestyle='-', color='b') 
        plt.title('MRU')
        plt.xlabel('Tiempo') ## eje x
        plt.ylabel('Posición')  ## eje y 
        plt.grid(True)  ## muestra una cuadricula
        plt.show() ## muestra el grafico

cuerpo = Cuerpo(v=5, x0=0)   ### entregamos la posicion inicial y la velocidad, 5 m/s 
simulador = SimuladorMovimiento(cuerpo) ## le pasamos el objeto recien creado de la clase cuerpo a simulador de movimiento

# este da el valor maximo para crear la lista de valores 
simulador.simular(tiempoMax=5)
 
