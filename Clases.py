class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def hablar(self):
        print(f"{self.nombre} esta hablando")
    def caminar(self):
        print(f"{self.nombre} esta caminando")

persona1 = Persona("Cristina", "Torres", 23)
persona2 = Persona("Cristian", "Hada", 20)

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")

print(f"{persona2.nombre}")

persona1.hablar
persona2.caminar


