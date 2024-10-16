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
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio =promedio
        self.estado = self.evaluar_estado()
    def __str__(self):
        return f"nombre estudiante: {self.__nombre}, promedio: {self.__promedio}, aprobado: {self.estado}"

    def evaluar_estado(self):
        return self.__promedio >= 4.0
    
    def actualizar_notas(self, new_nota):
        print(f"promedio anterior: {self.__promedio} de {self.__nombre}")
        self.__promedio = ((self.__promedio + new_nota) /2)
        print(f"nuevo promedio: {self.__promedio}")
        self.estado = self.evaluar_estado()
        print(f"aprobado :{self.estado}")
estudiante1 = Estudiante("Carlos", 5.6)
estudiante2 = Estudiante("Maria", 6.5)
estudiante3 = Estudiante("Claudia", 3.9)


for estudiante in(estudiante1, estudiante2, estudiante3):
    print(estudiante)
estudiante1.actualizar_notas(2.1)
estudiante2.actualizar_notas(4.5)
estudiante3.actualizar_notas(7.0)

estudiante.evaluar_estado()