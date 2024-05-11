def agregar_actividad(actividades, nombre, descripcion, prioridad):
    actividades.append({"nombre": nombre, "descripcion": descripcion, "prioridad": prioridad, "completada": False})
    print("Actividad agregada con éxito.")

def marcar_completada(actividades, nombre):
    for actividad in actividades:
        if actividad["nombre"] == nombre:
            actividad["completada"] = True
            print(f"Actividad '{nombre}' marcada como completada.")
            return
    print("No se encontró la actividad especificada.")

def mostrar_pendientes(actividades):
    print("Actividades pendientes:")
    pendientes = [actividad for actividad in actividades if not actividad["completada"]]
    if pendientes:
        for actividad in pendientes:
            print(f"Nombre: {actividad['nombre']}, Descripción: {actividad['descripcion']}, Prioridad: {actividad['prioridad']}")
    else:
        print("No hay actividades pendientes.")

def main():
    actividades = [
        {"nombre": "Hacer ejercicio", "descripcion": "Correr 5 km", "prioridad": "Alta", "completada": False},
        {"nombre": "Estudiar", "descripcion": "Preparar para el examen", "prioridad": "Media", "completada": False},
        {"nombre": "Comprar alimentos", "descripcion": "Ir al supermercado", "prioridad": "Baja", "completada": False}
    ]

    while True:
        print("\n1. Agregar actividad")
        print("2. Marcar actividad como completada")
        print("3. Mostrar actividades pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la actividad: ")
            descripcion = input("Ingrese la descripción de la actividad: ")
            prioridad = input("Ingrese la prioridad de la actividad (Alta/Media/Baja): ")
            agregar_actividad(actividades, nombre, descripcion, prioridad)
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la actividad a marcar como completada: ")
            marcar_completada(actividades, nombre)
        elif opcion == "3":
            mostrar_pendientes(actividades)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
