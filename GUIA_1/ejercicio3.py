class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial_stock = []
        self.historial_stock.append(f"Stock inicial: {cantidad} unidades")
    
    def actualizar_stock(self, cambio): ## metodo del cambio, se suma cambio a self.cantidad
        self.cantidad += cambio ## ej: 50 + (-5) = 45
        if cambio > 0:  ## si cambio es mayor que cero entonces muestra este print inicializado arriba
            self.historial_stock.append(f"Se agregaron {cambio} unidades. Total: {self.cantidad}")
        else:
            self.historial_stock.append(f"Se restaron {-cambio} unidades. Total: {self.cantidad}")
    
    def valor_total(self): ## metodo para sacar el valor total del inventario 
        return self.cantidad * self.precio
    
    def __str__(self): ### metodo magico para mostrar el estado del producto 
        return (f"Producto: {self.nombre}, Precio: {self.precio}, "
                f"Cantidad: {self.cantidad}, Código: {self.codigo}")
class Inventario:
    def __init__(self):
        self.productos = {}   ## diccionario de productos 
    
    def agregar_producto(self, producto): ## para agregar un producto al inventario 
            self.productos[producto.codigo] = producto
            print(f"El producto {producto.nombre} fue agregado al inventario.")
    
    def actualizar_stock_producto(self, codigo, cambio):   ## actualiza el stock del producto, 
        if codigo in self.productos:
            self.productos[codigo].actualizar_stock(cambio)
        else:
            print("Producto no encontrado.") ## sino encuentra el codigo del producto muestra el print 
    
    def mostrar_productos(self): ### imprime la informacion de todos los productos del diccionario 
        for producto in self.productos.values(): ## values para saber todos los valores del diccionario  
            print(producto) 
    
    def valor_total_inventario(self):  ## llamamos el metodo valor total, osea valor total de cada producto en el diccionario
        total = sum(producto.valor_total() for producto in self.productos.values()) ## sum toma todos los valores y los suma
        return total

producto1 = Producto("Libro", 15000, 25, "1778") 
producto2 = Producto("Cuaderno", 2300, 50, "1777")
producto3 = Producto("libreta", 1300, 60, "1776")
producto4 = Producto("Caja de Lapices", 2500, 15, "1775")
producto5 = Producto("pegamento", 800, 50, "1774")
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)
inventario.agregar_producto(producto4)
inventario.agregar_producto(producto5)
inventario.actualizar_stock_producto("1778", 5)
inventario.actualizar_stock_producto("1777", -3)
inventario.actualizar_stock_producto("1776", 15)
inventario.actualizar_stock_producto("1775", 60)
inventario.actualizar_stock_producto("1774", -40)
inventario.mostrar_productos()

print(f"Valor total del inventario: {inventario.valor_total_inventario()}")
print(f"Historial de stock del producto 1778: {producto1.historial_stock}")
print(f"Historial de stock del producto 1777: {producto2.historial_stock}")