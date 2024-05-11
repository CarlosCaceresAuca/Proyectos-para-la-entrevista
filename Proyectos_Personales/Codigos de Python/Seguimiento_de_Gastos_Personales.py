def ingresar_gastos(gastos_diarios):
    dia = input("Ingrese el día del gasto (por ejemplo, 1 para el primer día del mes): ")
    categoria = input("Ingrese la categoría del gasto (por ejemplo, alimentación, transporte, entretenimiento, etc.): ")
    monto = float(input("Ingrese el monto del gasto: $"))

    if dia not in gastos_diarios:
        gastos_diarios[dia] = {}

    if categoria not in gastos_diarios[dia]:
        gastos_diarios[dia][categoria] = monto
    else:
        gastos_diarios[dia][categoria] += monto

    print("Gasto registrado con éxito.")

def calcular_gastos_mensuales(gastos_diarios):
    gastos_mensuales = {}
    for dia, gastos_dia in gastos_diarios.items():
        for categoria, monto in gastos_dia.items():
            if categoria not in gastos_mensuales:
                gastos_mensuales[categoria] = monto
            else:
                gastos_mensuales[categoria] += monto
    return gastos_mensuales

def mostrar_resumen_gastos(gastos_mensuales):
    print("Resumen de gastos mensuales por categoría:")
    for categoria, monto in gastos_mensuales.items():
        print(f"{categoria}: ${monto:.2f}")

def main():
    gastos_diarios = {}

    while True:
        print("\n1. Ingresar gasto diario")
        print("2. Mostrar resumen de gastos mensuales")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_gastos(gastos_diarios)
        elif opcion == "2":
            gastos_mensuales = calcular_gastos_mensuales(gastos_diarios)
            mostrar_resumen_gastos(gastos_mensuales)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
