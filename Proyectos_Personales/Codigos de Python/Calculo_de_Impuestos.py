def calcular_impuesto(ingresos):
    if ingresos <= 10000:
        impuesto = ingresos * 0.1
    elif ingresos <= 30000:
        impuesto = 10000 * 0.1 + (ingresos - 10000) * 0.2
    elif ingresos <= 60000:
        impuesto = 10000 * 0.1 + 20000 * 0.2 + (ingresos - 30000) * 0.3
    else:
        impuesto = 10000 * 0.1 + 20000 * 0.2 + 30000 * 0.3 + (ingresos - 60000) * 0.4
    return impuesto

def main():
    ingresos_anuales = float(input("Ingrese el monto de sus ingresos anuales: $"))
    impuesto_a_pagar = calcular_impuesto(ingresos_anuales)
    print(f"El monto de impuestos a pagar es: ${impuesto_a_pagar:.2f}")

main()
