def agregar_producto(inventario, producto, cantidad):
    inventario[producto] = cantidad
    print("Producto agregado con éxito.")

def actualizar_cantidad(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
        print("Cantidad actualizada con éxito.")
    else:
        print("El producto no existe en el inventario.")

def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print("Producto eliminado del inventario.")
    else:
        print("El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

def main():
    inventario = {}

    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar cantidad de producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad disponible: "))
            agregar_producto(inventario, producto, cantidad)
        elif opcion == "2":
            producto = input("Ingrese el nombre del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            actualizar_cantidad(inventario, producto, cantidad)
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(inventario, producto)
        elif opcion == "4":
            mostrar_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
