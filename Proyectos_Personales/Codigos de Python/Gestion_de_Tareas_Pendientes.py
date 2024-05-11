def agregar_tarea(tareas, descripcion, fecha_limite):
    tarea = {"descripcion": descripcion, "fecha_limite": fecha_limite, "completada": False}
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

def marcar_completada(tareas, descripcion):
    for tarea in tareas:
        if tarea["descripcion"] == descripcion:
            tarea["completada"] = True
            print(f"Tarea '{descripcion}' marcada como completada.")
            return
    print("No se encontró la tarea especificada.")

def mostrar_pendientes(tareas):
    print("Tareas pendientes:")
    pendientes = [tarea for tarea in tareas if not tarea["completada"]]
    if pendientes:
        for tarea in pendientes:
            print(f"Descripción: {tarea['descripcion']}, Fecha límite: {tarea['fecha_limite']}")
    else:
        print("No hay tareas pendientes.")

def main():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas pendientes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_limite = input("Ingrese la fecha límite de la tarea (por ejemplo, DD/MM/AAAA): ")
            agregar_tarea(tareas, descripcion, fecha_limite)
        elif opcion == "2":
            descripcion = input("Ingrese la descripción de la tarea a marcar como completada: ")
            marcar_completada(tareas, descripcion)
        elif opcion == "3":
            mostrar_pendientes(tareas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
