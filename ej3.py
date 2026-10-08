class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        # Se incluyen 12 meses más un aguinaldo.
        return self.salario_mensual * 13

    def __str__(self):
        return (
            f"EMPLEADO\n"
            f"Nombre: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Salario mensual: {self.salario_mensual:,.0f} Gs.\n"
            f"Salario anual con aguinaldo: "
            f"{self.calcular_salario_anual():,.0f} Gs."
        )


empleado1 = Empleado("Carlos Benítez", "Vendedor", 3500000)
empleado2 = Empleado("Laura González", "Administradora", 5000000)

print(empleado1)
print()
print(empleado2)