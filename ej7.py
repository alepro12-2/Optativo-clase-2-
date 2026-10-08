class ProductoStock:
    def __init__(self, nombre, stock, stock_minimo):
        self.nombre = nombre
        self.stock = stock
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad <= 0:
            print("La cantidad ingresada debe ser positiva.")
        else:
            self.stock += cantidad
            print(f"Ingresaron {cantidad} unidades.")
            self.verificar_alerta()

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("La cantidad vendida debe ser positiva.")
        elif cantidad > self.stock:
            print("Venta rechazada: stock insuficiente.")
        else:
            self.stock -= cantidad
            print(f"Venta registrada: {cantidad} unidades.")
            self.verificar_alerta()

    def verificar_alerta(self):
        if self.stock < self.stock_minimo:
            print(
                f"ALERTA: el stock de {self.nombre} está por debajo "
                f"del mínimo."
            )

    def __str__(self):
        return (
            f"CONTROL DE STOCK\n"
            f"Producto: {self.nombre}\n"
            f"Stock actual: {self.stock} unidades\n"
            f"Stock mínimo: {self.stock_minimo} unidades"
        )


producto = ProductoStock("Yerba mate", 20, 10)

print(producto)
print()

producto.registrar_venta(8)
print(producto)
print()

producto.registrar_venta(5)
print(producto)
print()

producto.ingresar_mercaderia(15)
print(producto)
print()

producto.registrar_venta(50)
print(producto)