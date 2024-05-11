def calcular_promedio(notas):
    return sum(notas) / len(notas)

def determinar_estado(promedio, puntaje_minimo):
    if promedio >= puntaje_minimo:
        return "Aprobado"
    else:
        return "Reprobado"

def main():
    estudiantes = {}

    num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

    for i in range(1, num_estudiantes + 1):
        nombre = input(f"Ingrese el nombre del estudiante {i}: ")
        notas = [float(x) for x in input(f"Ingrese las notas del estudiante {nombre} separadas por espacios: ").split()]
        estudiantes[nombre] = notas

    puntaje_minimo = float(input("Ingrese el puntaje mínimo para aprobar: "))

    aprobados = 0
    reprobados = 0
    suma_promedios = 0

    print("\nResultados:")

    for estudiante, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        estado = determinar_estado(promedio, puntaje_minimo)
        suma_promedios += promedio

        if estado == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1

        print(f"{estudiante}: Promedio = {promedio:.2f}, Estado = {estado}")

    promedio_general = suma_promedios / num_estudiantes
    print("\nPromedio general de la clase:", promedio_general)
    print("Cantidad de estudiantes aprobados:", aprobados)
    print("Cantidad de estudiantes reprobados:", reprobados)

main()
