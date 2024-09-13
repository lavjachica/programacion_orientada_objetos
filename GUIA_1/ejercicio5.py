#ejercicio 5

class Libro:
    def __init__(self, titulo, autor, año_publicacion, cantidad_disponible):
         # Asignamos los valores a los atributos del libro.
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, cantidad):
       
        if cantidad < 0:                   # Si la cantidad es menor a 0, muestra un mensaje de error y no actualiza la cantidad.
            print("Error: La cantidad no puede ser negativa.")
            return
        self.cantidad_disponible = cantidad      # Actualiza la cantidad disponible del libro con el valor proporcionado.       

    def __str__(self):            # metodo magico de cadena de texto
        
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Año de publicación: {self.año_publicacion}\n"
                f"Cantidad disponible: {self.cantidad_disponible}")

class Biblioteca:      #creamos la clase biblioteca para poder manejar los libros 
    def __init__(self):
        
        self.libros = {} # El diccionario almacenará los libros con el título como clave

    def agregar_libro(self, libro):           #usamos este Método para actualizar la cantidad disponible de un libro por su título.
           # Si el libro ya existe (según el título), actualiza su cantidad.
        if libro.titulo in self.libros:
            #actualiza los libros
            libro_existente = self.libros[libro.titulo]
            nueva_cantidad = libro_existente.cantidad_disponible + libro.cantidad_disponible
            libro_existente.actualizar_cantidad(nueva_cantidad)
        else:
            self.libros[libro.titulo] = libro

    def buscar_libro_por_titulo(self, titulo):         #creamos metodo magico para poder buscar los libros
        
        libro = self.libros.get(titulo)
        if libro:
            return libro
        else:
            return "Libro no encontrado."      # si el libro buscado no existe arrojara el mensaje de "libro no encontrado"

    def actualizar_libro(self, titulo, cantidad_disponible):   # definimos metodo magico de actualizar los libros
        
        libro = self.libros.get(titulo)
        if libro:
            libro.actualizar_cantidad(cantidad_disponible)
        else:
            return "Libro no encontrado."

    def __str__(self):              # Método mágico para devolver una representación en cadena de la biblioteca.
        if not self.libros:
            return "La biblioteca está vacía."
        return '\n\n'.join(str(libro) for libro in self.libros.values()) # y lo que devuelve la cadena es que la biblioteca esta vacia 

# Ejemplo de uso:
libro1 = Libro("El hobbit", " J.R.R. Tolkien", 1937, 5)
libro2 = Libro("Percy Jackson", "Rick Riordan", 2006, 3)

#aca agregamos el libro 1 y 2 para el ejemplo
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)


print("Biblioteca después de agregar libros:")
print(biblioteca)

#buscamos el libro que queramos en la biblioteca y se imprime
print("\nBuscar libro 'El hobbit':")
print(biblioteca.buscar_libro_por_titulo("El hobbit"))

print("\nActualizar la cantidad disponible de 'Percy Jackson' a 10:")
biblioteca.actualizar_libro("Percy Jackson", 10)
print(biblioteca)

print("\nBuscar libro 'Don Juan Tenorio':")
print(biblioteca.buscar_libro_por_titulo("Don Juan Tenorio")) # al buscar un libro no existente arroja el mensaje de libro no encontrado