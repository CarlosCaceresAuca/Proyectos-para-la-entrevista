def ingresar_calificaciones(estudiantes, asignaturas):
    for estudiante in estudiantes:
        print(f"Ingresando calificaciones para {estudiante}:")
        for asignatura in asignaturas:
            calificacion = float(input(f"Ingrese la calificación de {asignatura} para {estudiante}: "))
            estudiantes[estudiante][asignatura] = calificacion

def calcular_promedio_por_asignatura(estudiantes, asignaturas):
    promedios = {}
    for asignatura in asignaturas:
        suma_calificaciones = 0
        cantidad_estudiantes = len(estudiantes)
        for estudiante, calificaciones in estudiantes.items():
            suma_calificaciones += calificaciones[asignatura]
        promedio = suma_calificaciones / cantidad_estudiantes
        promedios[asignatura] = promedio
    return promedios

def mostrar_resumen_calificaciones(estudiantes, promedios):
    print("Resumen de calificaciones por asignatura:")
    for asignatura, promedio in promedios.items():
        print(f"{asignatura}: Promedio = {promedio:.2f}")
        for estudiante, calificaciones in estudiantes.items():
            print(f"    {estudiante}: {calificaciones[asignatura]}")

def main():
    estudiantes = {
        "Estudiante 1": {},
        "Estudiante 2": {},
        "Estudiante 3": {}
    }

    asignaturas = ["Matemáticas", "Ciencias", "Historia"]

    ingresar_calificaciones(estudiantes, asignaturas)
    promedios = calcular_promedio_por_asignatura(estudiantes, asignaturas)
    mostrar_resumen_calificaciones(estudiantes, promedios)

main()

