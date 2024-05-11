def calcular_factorial(numero):
    factorial = 1
    if numero == 0:
        return 1
    else:
        for i in range(1, numero + 1):
            factorial *= i
        return factorial

def main():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número entero no negativo: "))
            if numero < 0:
                print("El número ingresado es negativo. Por favor, ingresa un número no negativo.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    factorial = calcular_factorial(numero)
    print("El factorial de", numero, "es:", factorial)

main()
