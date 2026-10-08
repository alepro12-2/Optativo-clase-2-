class Habitacion:
    def __init__(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(
                f"La habitación {self.numero} ya está ocupada."
            )
        else:
            self.ocupada = True
            print(
                f"La habitación {self.numero} fue ocupada correctamente."
            )

    def liberar(self):
        if not self.ocupada:
            print(
                f"La habitación {self.numero} ya está libre."
            )
        else:
            self.ocupada = False
            print(
                f"La habitación {self.numero} fue liberada."
            )

    def calcular_estadia(self, noches):
        if noches <= 0:
            print("La cantidad de noches debe ser positiva.")
            return 0

        return self.tarifa_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"

        return (
            f"HABITACIÓN\n"
            f"Número: {self.numero}\n"
            f"Tipo: {self.tipo}\n"
            f"Tarifa por noche: {self.tarifa_noche:,.0f} Gs.\n"
            f"Estado: {estado}"
        )


habitacion = Habitacion(
    205,
    "Doble",
    350000
)

print(habitacion)
print()

habitacion.ocupar()
print(habitacion)
print()

costo = habitacion.calcular_estadia(4)
print(f"Costo de la estadía: {costo:,.0f} Gs.")
print()

habitacion.ocupar()
print()

habitacion.liberar()
print(habitacion)   