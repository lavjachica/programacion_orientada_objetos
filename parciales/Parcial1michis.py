class Gato:
    def __init__(self, nombre, color, edad, energia, hambre):
        self.__nombre= nombre ## el nombre del Gato siempre sera el mismo 
        self.__color = color ## el color del gato no es modificable, siempre sera de ese color 
        self.__edad = edad ## la edad del gato no es modificable, al menos en este caso no. 
        self.energia = energia 
        self.hambre = hambre 
        ### funcion para que el gato Juegue 
    def jugar(self, juego):
        print(f"energia inicial del gato {self.__nombre} es de {self.energia}")
        if self.hambre >= 25: ## la comida debe de ser mayor a 25 para poder jugar, si es menor el gato no puede 
            self.energia -= juego.restar_energia 
            print(f"El gato {self.__nombre} está jugando, su energia ha disminuido a {self.energia} juega con {juego.tipo_producto}, que resta energia de {juego.restar_energia}")
        if self.energia <= 50:
            print(f"el gato tiene hambre, debes alimentarlo para que pueda tener energia")
        ### funcion para alimentar al Gato
    def alimentar(self, alimento):
        if self.hambre <=25:
            self.hambre += alimento.reponer_energia
            print(f"El gato {self.__nombre} siempre tiene hambre, sus niveles de comida estan bajos, han sido repuestos ha {self.hambre}  ")
        else:
            print(f"El gato {self.__nombre} esta lleno, prueba jugar con el!, sus niveles de comida estan en {self.hambre}")


    def __str__(self):
        return f"Gato {self.__nombre}, de color {self.__color}, con {self.__edad} años, tiene un nivel de energia {self.energia} con un nivel e hambre: {self.hambre}"
    
class Area:
    def __init__(self, nombre, cantidad_gatos, gatos):
        self.nombre = nombre 
        self.cantidad_gatos = cantidad_gatos
        self.gatos = [] 

            ### metodo para agregar a la lista de gatos
    def agregar(self, michi): ## utilice "michi" para no confundirme
        if isinstance(michi, Gato):
            self.gatos.append(michi)
            print(f"haz agregado el gato a la lista de gatos!")
        else:
            print(f"El animal que deseas agregar no pertenece a la Clase Gato ")
        ### no funciono pero es el intento de agregar la lista de gatos a las areas, por mientras la lista funciona
    def Agregar_michi(self, gato):
        if self.cantidad_gatos + gato <= self.cantidad_gatos:
            self.cantidad_gatos += gato 
            print(f"el gato ha sido agregado al area {self.nombre}")
        else:
            print(f"el Área al que deseas agregar el gato ya esta llena, busca otra Área")

class Productos:
    def __init__(self, tipo_producto, cantidad, restar_energia, reponer_energia):
        self.tipo_producto= tipo_producto
        self.cantidad = cantidad 
        self.restar_energia = restar_energia
        self.reponer_energia = reponer_energia
    def __str__(self):
        return f"Del producto {self.tipo_producto} hay {self.cantidad} cantidad."
class Inventario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.recursos = []

    def Agregar_Inventario(self, productos):
        if isinstance(productos, Productos):
            self.recursos.append(productos)
            print(f"el producto {productos} ha sido agregado con exito al inventario")
        else:
            print("El producto que quieres agregar no pertenece a la clase Productos")

    def mostrar(self):
        for inventario in self.recursos:
            print(inventario)
### creamos los gatos
gato1 = Gato("Raul", "gris", 5, 100, 25)
gato2 = Gato("Michihausen", "blanco", 2, 150, 50)
gato3 = Gato("Chirimoya", "naranja", 1, 200, 100)

### creamos las areas
Area1 = Area("terraza", 12, None)
Area2 = Area("niños", 10, None)
Area3 = Area("adultos", 20, None)

### Creamos los productos

comida1 = Productos("churu", 50, None, 50)
comida2 = Productos("whiskas", 30, None, 100)
comida3 = Productos("catnip", 12, None, 10)
juguete1 = Productos("raton", 40, 50, None)
juguete2 = Productos("pelota", 10, 100, None) ## no creamos objetos en el inventario porque el 
                                    ## inventario gestiona los objetos de productos
juguete3 = Productos("pajaro", 15, 25, None)

inventario1 = Inventario("Inventario Gatos")
## Funcion Jugar
gato1.jugar(juguete1)
gato2.jugar(juguete1)
## Funcion Alimentarse 
gato3.alimentar(comida1) ## probando con un gatito lleno
gato1.alimentar(comida1) ## un gatito con hambre

### Funciones de admin area
## agregar a la lista de gatos
Area1.agregar(gato1)
### agregar al area deseada un gato


## inventario 
inventario1.Agregar_Inventario(comida1)
inventario1.Agregar_Inventario(comida2)
inventario1.Agregar_Inventario(comida3)
inventario1.Agregar_Inventario(juguete1)


inventario1.mostrar()
            