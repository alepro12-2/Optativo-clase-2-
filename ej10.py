class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (
            f"{self.nombre} - "
            f"{self.precio:,.0f} Gs."
        )


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        subtotal = self.calcular_subtotal()

        return (
            f"{self.producto.nombre} | "
            f"Cantidad: {self.cantidad} | "
            f"Subtotal: {subtotal:,.0f} Gs."
        )


class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar_item(self, item):
        if item.cantidad <= 0:
            print("La cantidad debe ser positiva.")
        else:
            self.items.append(item)
            print(f"Se agregó {item.producto.nombre} al carrito.")

    def calcular_total(self):
        total = 0

        for item in self.items:
            total += item.calcular_subtotal()

        return total

    def mostrar_detalle(self):
        print(f"CARRITO DE {self.cliente}")
        print("-" * 40)

        for item in self.items:
            print(item)

        print("-" * 40)
        print(f"TOTAL: {self.calcular_total():,.0f} Gs.")

    def __str__(self):
        return (
            f"Carrito de {self.cliente} - "
            f"{len(self.items)} artículo(s)"
        )


producto1 = Producto("Auriculares", 150000)
producto2 = Producto("Teclado", 180000)
producto3 = Producto("Mouse", 80000)

item1 = Item(producto1, 1)
item2 = Item(producto2, 2)
item3 = Item(producto3, 1)

carrito = Carrito("Miguel Torres")

carrito.agregar_item(item1)
carrito.agregar_item(item2)
carrito.agregar_item(item3)

print()
carrito.mostrar_detalle()