class Gato:
    def __init__(self, nombre, color, edad, energia, hambre):
        self.__nombre= nombre ## el nombre del Gato siempre sera el mismo 
        self.__color = color ## el color del gato no es modificable, siempre sera de ese color 
        self.__edad = edad ## la edad del gato no es modificable, al menos en este caso no. 
        self.energia = energia 
        self.hambre = hambre 
        ### funcion para que el gato Juegue 
    def jugar(self, juego):
        self.hambre = True
        self.energia -= juego 
        if self.energia == 0:
            self.hambre = False
        ### funcion para alimentar al Gato
    def alimentar(self, alimento):
        if self.hambre == False:
            self.hambre += alimento 
            self.hambre = True

    def __str__(self):
        return f"Gato {self.__nombre}, de color {self.__color}, con {self.__edad} años, 
                 tiene un nivel de energia {self.energia} con un nivel e hambre: {self.hambre}"
    
    class Area:
        def __init__(self, nombre, cantidad_gatos, gatos):
            self.nombre = nombre 
            self.cantidad_gatos = cantidad_gatos
            self.gatos = [] 

            ### metodo para agregar a la lista de gatos
        def agregar(self, michi): ## utilice "michi" para no confundirme
            if isinstance(michi, Gato):
                self.gatos.append(michi)
            else:
                print(f"El animal que deseas agregar no pertenece a la Clase Gato ")
            ### metodo para agregar Gatos a las áreas 
        def Agregar_michi(self, gato):
            if self.cantidad_gatos + gato > self.cantidad_gatos:
                self.cantidad_gatos += gato 
            else:
                print(f"el Área al que deseas agregar el gato ya esta llena, busca otra Área")

class Productos:
    def __init__(self, tipo_producto, cantidad):
        self.tipo_producto= tipo_producto
        self.cantidad = cantidad 
    def __str__(self):
        return f"Del producto {self.tipo_producto} hay {self.cantidad} cantidad."
class Inventario:
    def __init__(self):
        self.recursos = []

    def Agregar_Inventario(self, productos):
        if isinstance(productos, Productos):
            self.recursos.append(productos)
            print(f"el producto {productos} ha sido agregado con exito al inventario")
        else:
            print("El producto que quieres agregar no pertenece a la clase Productos")

    
            