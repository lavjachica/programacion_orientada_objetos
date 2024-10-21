##  Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases,
##  Contacto y Agenda, para gestionar los contactos de una agenda. El objetivo es permitir al
##  usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos. Además,
##  el programa debe finalizar correctamente cuando el usuario lo solicite.

## Clase Contacto
## La clase debe tener los atributos privados de nombre, teléfono y email.
## Métodos de la clase
## ● Constructor
## ● Método mágico que retorne una cadena con el nombre, teléfono y email del contacto.
## ● Otro método que permite modificar el nombre, teléfono o email de un contacto. Solo
## los datos que se proporcionen deben ser modificados.
## Clase Agenda
## La clase debe tener un atributo que almacene una lista pública de contactos.
## Métodos de la clase
## ● Crear método que permita añadir un nuevo contacto a la agenda.
## ● Agregar método que muestre todos los contactos en la agenda.
## ● Un método para buscar un contacto en la agenda por nombre y lo muestra.
## ● Agregar un método para buscar un contacto por nombre y editar sus datos.
## ● Por último, crear un método que finalice el programa.

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def __str__(self):
        return f"contacto {self.__nombre} - {self.__telefono} - {self.__email}"
    def modificar(self, nombre, telefono, email):
        if nombre:
            self.__nombre = nombre
        if telefono:
            self.__telefono = telefono
        if email:
            self.__email = email
class Agenda:
    def __init__(self, agenda):
        self.agenda = agenda
        self.contactos = []
    def agregar(self, contacto):
        if isinstance(contacto, Contacto):
            self.contactos.append(contacto)
            print(f"el contacto {contacto._Contacto__nombre} ha sido agregado con exito")
        else:
            print(f"el contacto {contacto} no pertenece a la clase contactos")
    
    def buscar(self, nombre):
        encontrado = False
        for contacto in self.contactos:
            if contacto._Contacto__nombre == nombre._Contacto__nombre:
                print(f"el contacto ha sido encontrado {contacto}")
                encontrado = True
            if not encontrado:
                print(f"no se ha encontrado el contacto en la agenda") 
        
        
    def mostrar(self):
        if not self.contactos:
            print(f"no existen contactos")
        else:
            for cantidad in self.contactos:
                print(cantidad)
agenda1 = Agenda("Agenda de Galaxy")
contacto1 = Contacto("Maria", 12345678, "maria@gmail.com")
agenda1.agregar(contacto1)
agenda1.buscar(contacto1)