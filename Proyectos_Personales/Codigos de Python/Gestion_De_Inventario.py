def actualizar_inventario(producto, cantidad, inventario):
    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        return True
    else:
        return False

def main():
    inventario = {
        "Sandias": 10,
        "Manzanas": 5,
        "Peras": 8,
    }

    producto_deseado = input("Ingrese el nombre del producto que desea: ").strip()
    cantidad_deseada = int(input("Ingrese la cantidad deseada: "))

    if actualizar_inventario(producto_deseado, cantidad_deseada, inventario):
        print(f"¡Compra exitosa! Se han vendido {cantidad_deseada} unidades de {producto_deseado}.")
    else:
        print(f"Lo sentimos, el producto {producto_deseado} está agotado o no hay suficiente cantidad en stock.")

main()
