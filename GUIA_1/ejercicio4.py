#la fonda menos cara de chile
class Pedido:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.platos = []
        self.total = 0.0
    def agregar_plato(self, nombre, precio):
        self.platos.append((nombre, precio))
        self.total += precio
    def calcular_total(self):
        return self.total
    def __len__(self):
        return len(self.platos)
    def __add__(self, otro_pedido):
        if self.numero_mesa != otro_pedido.numero_mesa:
            raise ValueError("Los pedidos deben ser de la misma mesa para combinar.")
        nuevo_pedido = Pedido(self.numero_mesa)
        nuevo_pedido.platos = self.platos + otro_pedido.platos
        nuevo_pedido.total = self.total + otro_pedido.total
        return nuevo_pedido
    def __del__(self):
        print(f"El pedido de la mesa {self.numero_mesa} ha sido completado.")
    def __repr__(self):
        platos_str = ', '.join([f'{nombre} (${precio:.2f})' for nombre, precio in self.platos])
        return (f'Pedido(mesa={self.numero_mesa}, '
                f'platos=[{platos_str}], '
                f'total=${self.total:.2f})')
if __name__ == "__main__":
    pedido1 = Pedido(5)
    pedido1.agregar_plato("Anticucho", 10000)
    pedido1.agregar_plato("Empanada de pino", 7000)
    print(pedido1)
    print(f"Total: ${pedido1.calcular_total():.2f}")
    print(f"Número de platos: {len(pedido1)}")
    pedido2 = Pedido(5)
    pedido2.agregar_plato("Choripan", 15000)
    pedido2.agregar_plato("Terremoto", 5000)
    print(pedido2)
    pedido_combinado = pedido1 + pedido2
    print(pedido_combinado)
    print("")
    del pedido1
    del pedido2
    del pedido_combinado