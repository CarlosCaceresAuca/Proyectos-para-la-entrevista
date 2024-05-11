def sugerir_destinos(destinos, presupuesto):
    destinos_sugeridos = []
    for destino, costo in destinos.items():
        if costo <= presupuesto:
            destinos_sugeridos.append(destino)
    return destinos_sugeridos

def main():
    destinos = {
        "París": 1500,
        "Roma": 1200,
        "Nueva York": 2000,
        "Tokio": 2500,
        "Bali": 1000
    }

    print("Bienvenido al sistema de planificación de viajes.")

    destino_elegido = input("Ingrese el destino al que le gustaría viajar: ")
    fecha_viaje = input("Ingrese la fecha de viaje (por ejemplo, mes y año): ")
    presupuesto_disponible = float(input("Ingrese su presupuesto disponible para el viaje: $"))

    destinos_sugeridos = sugerir_destinos(destinos, presupuesto_disponible)

    print("\nBasado en sus preferencias y presupuesto, le sugerimos los siguientes destinos:")
    for destino in destinos_sugeridos:
        print(destino)

main()
