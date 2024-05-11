def contar_digitos_pares_impares(numero):
    pares = 0
    impares = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            pares += 1
        else:
            impares += 1
        numero //= 10
    return pares, impares

def main():
    while True:
        try:
            numero = int(input("Por favor, ingresa un número entero positivo: "))
            if numero <= 0:
                print("El número ingresado no es positivo. Por favor, intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

    pares, impares = contar_digitos_pares_impares(numero)
    print("Cantidad de dígitos pares:", pares)
    print("Cantidad de dígitos impares:", impares)

main()
