class LineaTelefonica:
    def __init__(self, cliente, gigabytes_incluidos):
        self.cliente = cliente
        self.gigabytes_incluidos = gigabytes_incluidos
        self.gigabytes_consumidos = 0

    def registrar_consumo(self, gigabytes):
        if gigabytes <= 0:
            print("El consumo debe ser positivo.")
        elif (
            self.gigabytes_consumidos + gigabytes
            > self.gigabytes_incluidos
        ):
            print(
                "Aviso: el consumo supera los gigabytes incluidos. "
                "Operación rechazada."
            )
        else:
            self.gigabytes_consumidos += gigabytes
            print(f"Consumo registrado: {gigabytes} GB.")

            if self.gigabytes_consumidos == self.gigabytes_incluidos:
                print("Aviso: el paquete de datos se agotó.")

    def gigabytes_disponibles(self):
        return (
            self.gigabytes_incluidos
            - self.gigabytes_consumidos
        )

    def __str__(self):
        return (
            f"LÍNEA TELEFÓNICA\n"
            f"Cliente: {self.cliente}\n"
            f"Plan contratado: {self.gigabytes_incluidos} GB\n"
            f"Consumidos: {self.gigabytes_consumidos} GB\n"
            f"Disponibles: {self.gigabytes_disponibles()} GB"
        )


linea = LineaTelefonica("Daniel López", 10)

print(linea)
print()

linea.registrar_consumo(3)
print(linea)
print()

linea.registrar_consumo(5)
print(linea)
print()

linea.registrar_consumo(4)
print(linea)