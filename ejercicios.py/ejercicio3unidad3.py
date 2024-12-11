class MetodoDePago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

class TarjetaDeCredito(MetodoDePago):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta

    def validar(self):
        # Aquí iría la lógica para validar la tarjeta
        print(f"Validando tarjeta {self.numero_tarjeta}...")
        return True  # Simulamos que la validación es exitosa

    def procesar_pago(self, monto):
        if self.validar():
            print(f"Procesando pago de {monto} con tarjeta de crédito {self.numero_tarjeta}.")
        else:
            print("La validación de la tarjeta ha fallado.")

class TransferenciaBancaria(MetodoDePago):
    def __init__(self, codigo_confirmacion):
        self.codigo_confirmacion = codigo_confirmacion

    def confirmar(self):
        # Aquí iría la lógica para confirmar la transferencia
        print(f"Confirmando transferencia con código {self.codigo_confirmacion}...")
        return True  # Simulamos que la confirmación es exitosa

    def procesar_pago(self, monto):
        if self.confirmar():
            print(f"Procesando transferencia bancaria de {monto}.")
        else:
            print("La confirmación de la transferencia ha fallado.")

class PagoEnEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Registrando pago en efectivo de {monto}.")

# Código principal para probar los métodos de pago
if __name__ == "__main__":
    # Crear instancias de diferentes métodos de pago
    tarjeta = TarjetaDeCredito("1234-5678-9012-3456")
    transferencia = TransferenciaBancaria("CONFIRM123")
    efectivo = PagoEnEfectivo()

    # Procesar pagos
    tarjeta.procesar_pago(100)
    transferencia.procesar_pago(200)
    efectivo.procesar_pago(50)
