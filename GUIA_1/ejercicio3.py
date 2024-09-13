# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad, codigo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial_stock = []  #Lista que registra los cambios en el stock
        self.historial_stock.append(f"stock inicial: {cantidad}")
  
    #Crear método que actualice el stock del producto y añada el cambio al historial de stock.
    def actualizar_stock(self, cambio):
        self.cantidad += cambio
        self.historial_stock.append(f"Cambio de stock: {cambio}, Nueva cantidad: {self.cantidad}")
    
    #Implementar método que calcule el valor total de los productos disponibles
    def valor_total(self):
        return self.precio * self.cantidad
    
    #Crear METODO MAGICO, que muestra el estado del producto c: 
    def __str__(self):
        return (f"Producto: {self.nombre}, Precio: {self.precio}, "
                f"Cantidad: {self.cantidad}, Código: {self.codigo}")

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  #Diccionario 
    
    #Metodo para agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"El producto con código {producto.codigo} ya existe en el inventario.")
        else:
            self.productos[producto.codigo] = producto
            print(f"Producto {producto.nombre} agregado al inventario.")
    
    #Metodo para actualizar el stock de un producto en el inventario
    def actualizar_stock_producto(self, codigo, cambio):
        producto = self.productos.get(codigo, None)
        if producto:
            producto.actualizar_stock(cambio)
            print(f"Stock actualizado para el producto {producto.nombre}.")
        else:
            print(f"No se encontró un producto con el código {codigo} en el inventario.")
    
    #Metodo para mostrar todos los productos del inventario y sus detalles
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)
    
    # Método para obtener el valor total de los productos en el inventario
    def valor_total_inventario(self):
        total = sum(producto.valor_total() for producto in self.productos.values())
        return total
producto1 = Producto("Libro", 15000, 25, 1778) 
producto2 = Producto("Cuaderno", 2300, 50, 1777)
producto3 = Producto("libreta", 1300, 60, 1776)
producto4 = Producto("Caja de Lapices", 2500, 15, 1775)
producto5 = Producto("pegamento", 800, 50, 1774)

#### MOSTRANDO ESTADO DEL PRODUCTO
print(producto1)
print(producto2)
print(producto3)
print(producto4)
print(producto5)
