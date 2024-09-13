#Ejercicio 4

class Pedido:
    def __init__(self, numero_mesa):
        # Inicializar el número de mesa y los detalles del pedido
        self.numero_mesa = numero_mesa  # Número de mesa
        self.platos = []  # Lista de platos (nombre, precio)
        self.total = 0.0  # Total del pedido
    
    def añadir_plato(self, nombre_plato, precio):
       
     # Agregar el plato a la lista y actualiza el total
        self.platos.append((nombre_plato, precio))
        self.total += precio                         # Actualizar el total del pedido
    
    def calcular_total(self):
        
        return self.total  # Devuelve el total del pedido
    
    def __len__(self):
         
        # Retornar el número de platos
        return len(self.platos)      # retornamos el numero de platos con len que cuenta la cantidad de cadenas
    
    def __add__(self, otro_pedido):    #Método mágico para combinar dos pedidos de la misma mesa
        
        # Comprobar si ambos pedidos son de la misma mesa
        if self.numero_mesa == otro_pedido.numero_mesa:
            nuevo_pedido = Pedido(self.numero_mesa)  # Crear un nuevo pedido 
            # Combinar los platos y actualizar el total
            nuevo_pedido.platos = self.platos + otro_pedido.platos
            nuevo_pedido.total = self.total + otro_pedido.total
            return nuevo_pedido  # Devolver el pedido combinado
        else:
            raise ValueError("Los pedidos son de mesas diferentes, no se pueden combinar.") # aqui se utiliza raise y value error para que lanze una excepcion porque no se pueden combinar 
    
    def __del__(self): #Método finalizador que se llama al eliminar el pedido
       
        # Mostrar un mensaje cuando se elimina el pedido
        print(f"El pedido de la mesa {self.numero_mesa} ha sido completado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un pedido para la mesa 1
    pedido1 = Pedido(numero_mesa=1)
    
    # Añadir platos al pedido
    pedido1.añadir_plato("completo italiano", 10.0)
    pedido1.añadir_plato("bebida limon soda", 2.5)
    
    # Ver el total del pedido
    print(f"Total del pedido: ${pedido1.calcular_total():.2f}")
    
    # Contar el número de platos en el pedido
    print(f"Número de platos en el pedido: {len(pedido1)}")
    
    # Crear otro pedido para la misma mesa
    pedido2 = Pedido(numero_mesa=1)
    pedido2.añadir_plato("pollo con papas fritas", 3.0)
    
    # Combinar los pedidos de las mesas
    pedido_combined = pedido1 + pedido2  # Combina ambos pedidos de la mesa 1
    print(f"Total del pedido combinado: ${pedido_combined.calcular_total():.2f}")
    
    # Contar el número de platos en el pedido combinado
    print(f"Número de platos en el pedido combinado: {len(pedido_combined)}")
    
    # Eliminar el pedido combinado (pongo el método __del__)
    del pedido_combined
