def suma_pares_hasta_n(n):
    suma = 0
    for i in range(2, n + 1, 2):
        suma += i
    return suma

def main():
    while True:
        try:
            n = int(input("Por favor, ingresa un número entero positivo: "))
            if n <= 0:
                print("El número ingresado no es positivo. Por favor, intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    suma_pares = suma_pares_hasta_n(n)
    print("La suma de todos los números pares desde 1 hasta", n, "es:", suma_pares)

main()
