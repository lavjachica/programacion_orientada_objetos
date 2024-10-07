import matplotlib.pyplot as plt 

class Funcion:
    def __init__(self, ejeX):
        self.ejeX = int(ejeX)

    def formula(self):
        y = self.ejeX**2 + 8
        print(f"funcion f(x)= {y}")
        return y
      

funcion1 = Funcion(ejeX=2)
funcion2 = Funcion(ejeX=1)
funcion3 = Funcion(ejeX=0)
funcion4 = Funcion(ejeX=3)
funcion1.formula()
posicion_x = [funcion1.ejeX, funcion2.ejeX, funcion3.ejeX, funcion4.ejeX]
posicion_y = [funcion1.formula(), funcion2.formula(), funcion3.formula(), funcion4.formula()]

     
plt.figure(figsize=(10, 5))
plt.plot(posicion_x, posicion_y, marker="o", linestyle="-", color="b")
plt.title("Función de x")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

