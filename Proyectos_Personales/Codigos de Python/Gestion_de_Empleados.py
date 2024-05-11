def agregar_empleado(registro, nombre, edad, salario, genero):
    empleado = {"nombre": nombre, "edad": edad, "salario": salario, "genero": genero}
    registro.append(empleado)
    print("Empleado agregado exitosamente.")

def eliminar_empleado(registro, nombre):
    for empleado in registro:
        if empleado["nombre"] == nombre:
            registro.remove(empleado)
            return True
    return False

def listar_empleados(registro):
    if not registro:
        print("No hay empleados registrados.")
    else:
        print("Lista de empleados:")
        for empleado in registro:
            print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}, Género: {empleado['genero']}")

def menu():
    registro = [
        {"nombre": "María", "edad": 30, "salario": 2500.0, "genero": "Femenino"},
        {"nombre": "Juan", "edad": 35, "salario": 3000.0, "genero": "Masculino"},
        {"nombre": "Ana", "edad": 28, "salario": 2200.0, "genero": "Femenino"}
    ]

    while True:
        print("\n1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Listar empleados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            edad = int(input("Ingrese la edad del empleado: "))
            salario = float(input("Ingrese el salario del empleado: "))
            genero = input("Ingrese el género del empleado (Femenino/Masculino): ")
            agregar_empleado(registro, nombre, edad, salario, genero)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del empleado que desea eliminar: ")
            if eliminar_empleado(registro, nombre):
                print("Empleado eliminado exitosamente.")
            else:
                print("No se encontró ningún empleado con ese nombre.")

        elif opcion == "3":
            listar_empleados(registro)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()
