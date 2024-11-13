class Sistema:
    def __init__(self):
        self.tickets = {}
        self.ventas = []
        
    descuento_grupal = 0.20
    
    def agregar_ticket(self, tipo, precio):
        assert precio > 0, "Su boleto debe costar mas que Cero."
        self.tickets[tipo] = precio
        
    def vender_tickets(self, ticket_vender, cantidad):
        assert ticket_vender in self.tickets, "Su ticket no existe"
        assert cantidad > 0, "La cantidad no puede ser menor que Cero."
        precio_de_ticket = self.tickets[ticket_vender]
        precio_venta = precio_de_ticket * cantidad 
        self.ventas.append(ticket_vender)
        print(f"La venta ha sido realizada con exito, han escogio los Tickets {ticket_vender} con precio { precio_de_ticket} y una cantidad de {cantidad} con un valor total de {precio_venta}")
        return precio_venta
    @staticmethod
    def descuento_grupal(precio_venta, cantidad):
        if cantidad >= 3:
             descuento_grupal = precio_venta - (precio_venta * Sistema.descuento_grupal)
             print(f"Felicidades han obtenido un descuento por una compra grupal de un 20% su nuevo valor es de: ${descuento_grupal}")
        return descuento_grupal
    

sistema = Sistema()

sistema.agregar_ticket("Vip", 15000)
sistema.agregar_ticket("Diamante", 30000)
sistema.vender_tickets("Vip", 3)
sistema.vender_tickets("Diamante", 2)