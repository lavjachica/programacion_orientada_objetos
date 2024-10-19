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
    