class Persona():
    def __init__(self, nombre, apellido, edad, peso, altura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = float(peso)
        self.altura = float(altura)

    def hablar(self):
        print(f"{self.nombre} esta hablando")
    def caminar(self):
        print(f"{self.nombre} esta caminando")
        ### inicializando metodo para calcular imc 
    def peso_imc(self):
        imc = self.peso/(self.altura **2) 
        print(f"IMC de {self.nombre}: {imc: 2f}")

            
        if imc < 18.5:
            print("Bajo peso")
        elif 18.5 <= imc < 24.9:
            print("Peso normal")
        elif 25 <= imc < 29.9:
            print("Sobrepeso")
        else:
            print("Obesidad")
        
        return imc
    def promedio_asignaturas(self, nota1, nota2, nota3):
        promedio = (nota1 + nota2 + nota3) /3 
        print(f"promedio de notas de {self.nombre} es de {promedio:2f}")

        if promedio >= 4.0:
            print(f"{self.nombre} ha aprobado")
        else:
            print(f"{self.nombre} ha reprobado")
        return promedio


persona1 = Persona("Cristina", "Torres", 23, 53.5, 1.53)
persona2 = Persona("Cristian", "Hada", 20, 72.7, 1.82)

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")
print(f"{persona1.peso}")
print(f"{persona1.altura}")

print(f"{persona2.nombre}")

persona1.hablar()
persona2.caminar()
persona1.peso_imc()
persona2.peso_imc()
persona1.promedio_asignaturas(3.5, 4.2, 4.0)
persona2.promedio_asignaturas(4.5, 3.8, 4.1)