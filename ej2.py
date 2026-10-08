class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_valor_stock(self):
        return self.precio * self.stock

    def __str__(self):
        valor_total = self.calcular_valor_stock()

        return (
            f"PRODUCTO\n"
            f"Nombre: {self.nombre}\n"
            f"Precio unitario: {self.precio:,.0f} Gs.\n"
            f"Stock: {self.stock} unidades\n"
            f"Valor total en stock: {valor_total:,.0f} Gs."
        )


producto1 = Producto("Arroz", 8500, 20)
producto2 = Producto("Aceite", 12000, 15)
producto3 = Producto("Azúcar", 7000, 25)

print(producto1)
print()
print(producto2)
print()
print(producto3)