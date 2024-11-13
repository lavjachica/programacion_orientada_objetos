class GestorTicketsEventos:
    # Descuento por compras en grupo (20%)
    DESCUENTO_GRUPO = 0.20
    
    def __init__(self):
        # Diccionario para almacenar los tipos de tickets y sus precios
        self._tipos_tickets = {}
        # Lista para registrar las ventas realizadas
        self._ventas_registradas = []

    def agregar_tipo_ticket(self, nombre_ticket, precio):
        """ Agrega un nuevo tipo de ticket al sistema. """
        assert precio > 0, "El precio debe ser positivo."
        self._tipos_tickets[nombre_ticket] = precio
        print(f"Tipo de ticket '{nombre_ticket}' agregado con precio {precio}.")

    def registrar_venta(self, nombre_ticket, cantidad):
        """ Registra la venta de tickets. """
        assert nombre_ticket in self._tipos_tickets, "El tipo de ticket no existe."
        assert cantidad > 0, "La cantidad debe ser positiva."
        
        precio_unitario = self._tipos_tickets[nombre_ticket]
        total_venta = self.calcular_total_venta(precio_unitario, cantidad)
        
        # Registrar la venta en la lista
        self._ventas_registradas.append({
            'nombre_ticket': nombre_ticket,
            'cantidad': cantidad,
            'total': total_venta
        })
        
        print(f"Venta registrada: {cantidad} tickets de '{nombre_ticket}' por un total de {total_venta}.")

    @staticmethod
    def calcular_total_venta(precio_unitario, cantidad):
        """ Calcula el total de la venta considerando el descuento por grupo. """
        total = precio_unitario * cantidad
        if cantidad >= 5:  # Aplicar descuento si se compran 5 o más tickets
            total -= total * GestorTicketsEventos.DESCUENTO_GRUPO
        return total

# Ejemplo de uso
gestor = GestorTicketsEventos()
gestor.agregar_tipo_ticket("General", 50)
gestor.agregar_tipo_ticket("VIP", 100)

gestor.registrar_venta("General", 3)  # Sin descuento
gestor.registrar_venta("VIP", 5)       # Con descuento por grupo 


