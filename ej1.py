class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (
            f"FICHA DEL CLIENTE\n"
            f"Nombre: {self.nombre}\n"
            f"Cédula: {self.cedula}\n"
            f"Teléfono: {self.telefono}"
        )


cliente1 = Cliente("Alexander Pintos", "5.517.840", "0981-123456")
cliente2 = Cliente("Alder Isaac", "6.678.901", "0972-654321")

print(cliente1)
print()
print(cliente2)