class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        precio_formateado = f"{self.precio:,.0f}".replace(",", ".")

        return (
            f"{self.marca} {self.modelo} {self.anio} — "
            f"{precio_formateado} Gs."
        )

    def __str__(self):
        return (
            f"VEHÍCULO\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.anio}\n"
            f"Precio: {self.precio:,.0f} Gs.\n"
            f"Descripción: {self.descripcion_comercial()}"
        )


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo2 = Vehiculo("Kia", "Sportage", 2022, 145000000)

print(vehiculo1)
print()
print(vehiculo2)