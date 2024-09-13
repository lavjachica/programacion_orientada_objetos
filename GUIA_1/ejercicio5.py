#ejercicio 5

class Libro:
    def __init__(self, titulo, autor, año_publicacion, cantidad_disponible):
        """Inicializa un libro con el título, autor, año de publicación y cantidad disponible."""
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, cantidad):    ### metodo para administar la cantidad de libros disponibles
        if cantidad < 0:                               
            print("Error: La cantidad no puede ser negativa.")
            return
        self.cantidad_disponible = cantidad

    def __str__(self): ## metodo magico para mostrar la informacion de los libros
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Año de publicación: {self.año_publicacion}\n"
                f"Cantidad disponible: {self.cantidad_disponible}")

class Biblioteca:
    def __init__(self):
        
        self.libros = {} ## inicializamos un diccionario vacio para almacenar los libros 

    def agregar_libro(self, libro):
        
        if libro.titulo in self.libros:
            libro_existente = self.libros[libro.titulo]
            nueva_cantidad = libro_existente.cantidad_disponible + libro.cantidad_disponible
            libro_existente.actualizar_cantidad(nueva_cantidad)
        else:
            self.libros[libro.titulo] = libro

    def buscar_libro_por_titulo(self, titulo):
        
        libro = self.libros.get(titulo)
        if libro:
            return libro
        else:
            return "Libro no encontrado."

    def actualizar_libro(self, titulo, cantidad_disponible):
        
        libro = self.libros.get(titulo)
        if libro:
            libro.actualizar_cantidad(cantidad_disponible)
        else:
            return "Libro no encontrado."

    def __str__(self):
        if not self.libros:
            return "La biblioteca está vacía."
        return '\n\n'.join(str(libro) for libro in self.libros.values())


libro1 = Libro("El hobbit", " J.R.R. Tolkien", 1937, 5)
libro2 = Libro("Percy Jackson", "Rick Riordan", 2006, 3)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print("Biblioteca después de agregar libros:")
print(biblioteca)

print("\nBuscar libro 'El hobbit':")
print(biblioteca.buscar_libro_por_titulo("El hobbit"))

print("\nActualizar la cantidad disponible de 'Percy Jackson' a 10:")
biblioteca.actualizar_libro("Percy Jackson", 10)
print(biblioteca)

print("\nBuscar libro 'Don Juan Tenorio':")
print(biblioteca.buscar_libro_por_titulo("Don Juan Tenorio"))