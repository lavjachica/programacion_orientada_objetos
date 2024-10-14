### Implementar un programa que gestione la información de un grupo de estudiantes. Cada
### estudiante tendrá un nombre y un promedio de notas. Además, el sistema debe determinar
### si el estudiante ha aprobado o no, y permitir la actualización de sus notas de forma controlada.
# 1. Implementar la clase Estudiante con los atributos privados (nombre y promedio) y
# atributo público (estado) que debe indicar si el estudiante ha aprobado o no
# (Booleano)
# 2. El programa debe permitir la creación de al menos tres estudiantes con su
# respectivo nombre y promedio.
# 3. Imprimir el estado de cada estudiante utilizando un método mágico para mostrar su
# nombre y promedio.
# 4. Simular una actualización de notas utilizando un método para ello.
# 5. Evaluar si los estudiantes han aprobado llamando a un método para evaluar el estado
# del estudiante, y que muestre un mensaje con su estado de aprobación.
class Estudiante:
    def __init__(self, nombre, promedio, estado):
        self.__nombre = nombre
        self.__promedio = promedio
        self.estado = True

estudiante1 = Estudiante("Carlos", 56, True)
estudiante2 = Estudiante("Maria", 65, True)
estudiante3 = Estudiante("Claudia", 39, False)

def getnombre(self):
    return self.__nombre
print(estudiante1._Estudiante__nombre)
print(estudiante2._Estudiante__nombre)
print(estudiante3._Estudiante__nombre)

def getpromedio(self):
    return self.__promedio
print(estudiante1._Estudiante__promedio)
print(estudiante2._Estudiante__promedio)
print(estudiante3._Estudiante__promedio)
def obtener_nombre(self):
    return self.__nombre
def obtener_promedio(self):
    return self.__promedio
def __str__(self):
    return f"El estudiante {self.obtener_nombre()}, con promedio {self.obtener_promedio()}, ¿ha aprobado? {self.estado}"


print(estudiante1)