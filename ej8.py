class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60

        return (
            f"{self.titulo} - {self.artista} "
            f"({minutos}:{segundos:02d})"
        )


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def calcular_duracion_total(self):
        total = 0

        for cancion in self.canciones:
            total += cancion.duracion

        return total

    def __str__(self):
        texto = f"LISTA DE REPRODUCCIÓN: {self.nombre}\n"

        for numero, cancion in enumerate(self.canciones, start=1):
            texto += f"{numero}. {cancion}\n"

        duracion = self.calcular_duracion_total()
        minutos = duracion // 60
        segundos = duracion % 60

        texto += (
            f"Duración total: "
            f"{minutos}:{segundos:02d}"
        )

        return texto


cancion1 = Cancion("Imagine", "John Lennon", 183)
cancion2 = Cancion("Perfect", "Ed Sheeran", 263)
cancion3 = Cancion("Viva la vida", "Coldplay", 242)

lista = ListaReproduccion("Mis canciones favoritas")

lista.agregar_cancion(cancion1)
lista.agregar_cancion(cancion2)
lista.agregar_cancion(cancion3)

print(lista)