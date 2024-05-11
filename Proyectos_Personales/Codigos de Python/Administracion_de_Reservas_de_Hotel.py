def reservar_habitacion(reservas, numero_habitacion, huesped, check_in, check_out):
    reservas[numero_habitacion] = {"huésped": huesped, "check-in": check_in, "check-out": check_out}
    print("Reserva realizada con éxito.")

def cancelar_reserva(reservas, numero_habitacion):
    if numero_habitacion in reservas:
        del reservas[numero_habitacion]
        print("Reserva cancelada.")
    else:
        print("La reserva no existe.")

def mostrar_resumen_reservas(reservas):
    print("Resumen de reservas:")
    if not reservas:
        print("No hay reservas actuales.")
    else:
        for numero_habitacion, detalles in reservas.items():
            print(f"Habitación {numero_habitacion}:")
            print(f"  Huésped: {detalles['huésped']}")
            print(f"  Check-in: {detalles['check-in']}")
            print(f"  Check-out: {detalles['check-out']}")
            print()

def main():
    reservas = {}

    while True:
        print("\n1. Reservar habitación")
        print("2. Cancelar reserva")
        print("3. Mostrar resumen de reservas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_habitacion = input("Ingrese el número de habitación: ")
            huesped = input("Ingrese el nombre del huésped: ")
            check_in = input("Ingrese la fecha de check-in (por ejemplo, DD/MM/AAAA): ")
            check_out = input("Ingrese la fecha de check-out (por ejemplo, DD/MM/AAAA): ")
            reservar_habitacion(reservas, numero_habitacion, huesped, check_in, check_out)
        elif opcion == "2":
            numero_habitacion = input("Ingrese el número de habitación a cancelar: ")
            cancelar_reserva(reservas, numero_habitacion)
        elif opcion == "3":
            mostrar_resumen_reservas(reservas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
