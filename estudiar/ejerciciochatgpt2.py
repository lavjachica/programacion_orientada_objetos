#Crea una clase llamada CuentaBancaria que tenga los siguientes atributos:

#titular (str)
#saldo (float)
#Implementa los siguientes métodos:

#depositar(cantidad): que sume la cantidad al saldo.
#retirar(cantidad): que reste la cantidad del saldo, pero asegúrate de que no se retire más de lo que hay en el saldo.
#mostrar_saldo(): que muestre el saldo actual de la cuenta.
#Crea una instancia de CuentaBancaria, realiza depósitos y retiros, y muestra el saldo.
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = str(titular)
        self.saldo = float(saldo)
    
    def deposito(self, cantidad):
        self.saldo += cantidad 
        print(f"Su nuevo saldo es de {self.saldo}")
    def retiro(self, retirar):
        if self.saldo >= retirar:
            self.saldo -= retirar 
            print(f"Su nuevo saldo es de {self.saldo}")
    def saldo_actual(self):
        saldo = self.saldo
        print(f"su saldo es de {saldo}")
persona1 = CuentaBancaria("juan", 35567)
persona1.deposito(10000)
persona1.retiro(5000)
persona1.saldo_actual()