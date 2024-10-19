## Imagina que estás diseñando un sistema para gestionar cuentas bancarias. Para ello, crea
## una clase llamada CuentaBancaria que modele el comportamiento básico de una cuenta de
## banco. El sistema debe permitir realizar operaciones como depósitos, retiros y consultar el
## saldo actual. Además, se debe utilizar el concepto de encapsulamiento para proteger la
## información sensible de la cuenta. Asegúrate de encapsular adecuadamente los atributos
## que consideres sensibles. Define métodos para interactuar con estos atributos de manera controlada.

class CuentaBancaria:
    def __init__(self, nombre, rut, saldo):
        self.__nombre = nombre
        self.__rut = rut
        self.__saldo = saldo

    def __str__(self):
        return f"Cuenta Rut Banco Estado {self.__nombre} - {self.__rut} - {self.__saldo}"
    
    def deposito(self, depositar):
        print(f"{self.__nombre} su saldo actual: {self.__saldo}")
        self.__saldo += depositar 
        print (f"{self.__nombre} su nuevo saldo despues del deposito es de: {self.__saldo}")

    def retiros(self, retirar):
        print(f"{self.__nombre} su saldo actual es de: {self.__saldo}")
        if self.__saldo >= retirar:
          self.__saldo -= retirar 
          print(f"{self.__nombre} su nuevo saldo despues del retiro es de {self.__saldo}")
        else:
            print(f"los fondos de la cuenta son insuficientes para hacer el retiro de {retirar}, saldo: {self.__saldo}")

persona1 = CuentaBancaria("Francisca", 123458903, 25000)
persona2 = CuentaBancaria("Raul", 234556778, 76000)

persona1.deposito(4500)
persona2.retiros(80000)
print(persona1)