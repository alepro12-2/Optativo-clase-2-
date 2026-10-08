class Estudiante:
    def __init__(self, nombre, nota_minima=60):
        self.nombre = nombre
        self.materias = {}
        self.nota_minima = nota_minima

    def registrar_nota(self, materia, nota):
        if nota < 0 or nota > 100:
            print("La nota debe estar entre 0 y 100.")
        else:
            self.materias[materia] = nota
            print(f"Nota registrada para {materia}.")

    def calcular_promedio(self):
        if len(self.materias) == 0:
            return 0

        total = sum(self.materias.values())
        return total / len(self.materias)

    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima

    def mostrar_boletin(self):
        print(f"BOLETÍN DE {self.nombre}")
        print("-" * 35)

        for materia, nota in self.materias.items():
            print(f"{materia}: {nota:.2f}")

        promedio = self.calcular_promedio()
        condicion = "Aprobado" if self.esta_aprobado() else "No aprobado"

        print("-" * 35)
        print(f"Promedio: {promedio:.2f}")
        print(f"Condición final: {condicion}")

    def __str__(self):
        return (
            f"Estudiante: {self.nombre}\n"
            f"Materias registradas: {len(self.materias)}"
        )


estudiante = Estudiante("Valentina Gómez")

estudiante.registrar_nota("Programación", 85)
estudiante.registrar_nota("Matemática", 72)
estudiante.registrar_nota("Base de Datos", 90)
estudiante.registrar_nota("Inglés", 78)

print()
estudiante.mostrar_boletin()