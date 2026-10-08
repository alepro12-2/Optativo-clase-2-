class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def marcar_atendido(self):
        self.estado = "atendido"

    def __str__(self):
        return (
            f"Paciente: {self.paciente} | "
            f"Hora: {self.hora} | "
            f"Estado: {self.estado}"
        )


class Agenda:
    def __init__(self):
        self.turnos = []

    def agendar_turno(self, turno):
        self.turnos.append(turno)
        print(f"Turno agendado para {turno.paciente}.")

    def listar_pendientes(self):
        print("TURNOS PENDIENTES")

        hay_pendientes = False

        for turno in self.turnos:
            if turno.estado == "pendiente":
                print(turno)
                hay_pendientes = True

        if not hay_pendientes:
            print("No hay turnos pendientes.")

    def __str__(self):
        return f"Agenda con {len(self.turnos)} turnos registrados."


turno1 = Turno("Ana Fernández", "08:00")
turno2 = Turno("Luis Ramírez", "09:00")
turno3 = Turno("Sofía Benítez", "10:00")

agenda = Agenda()

agenda.agendar_turno(turno1)
agenda.agendar_turno(turno2)
agenda.agendar_turno(turno3)

print()
turno1.marcar_atendido()
turno3.marcar_atendido()

agenda.listar_pendientes()