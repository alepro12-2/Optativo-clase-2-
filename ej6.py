class CuentaCorriente:
    def __init__(self, cliente, saldo_inicial):
        self.cliente = cliente
        self.saldo = saldo_inicial if saldo_inicial >= 0 else 0

    def acreditar(self, monto):
        if monto <= 0:
            print("El monto a acreditar debe ser positivo.")
        else:
            self.saldo += monto
            print(f"Se acreditaron {monto:,.0f} Gs.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El consumo debe ser positivo.")
        elif monto > self.saldo:
            print("Compra rechazada: saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Consumo registrado: {monto:,.0f} Gs.")

    def __str__(self):
        return (
            f"CUENTA CORRIENTE\n"
            f"Cliente: {self.cliente}\n"
            f"Saldo disponible: {self.saldo:,.0f} Gs."
        )


cuenta = CuentaCorriente("Pedro Martínez", 100000)

print(cuenta)
print()

cuenta.acreditar(50000)
print(cuenta)
print()

cuenta.registrar_consumo(80000)
print(cuenta)
print()

cuenta.registrar_consumo(100000)
print(cuenta)
print()

cuenta.acreditar(-5000)
print(cuenta)