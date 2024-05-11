class RegistroVentas:
    def __init__(self):
        self.ventas_diarias = []
    
    def agregar_venta(self, monto):
        self.ventas_diarias.append(monto)
    
    def calcular_total_ventas(self):
        return sum(self.ventas_diarias)
    
    def calcular_promedio_semanal(self):
        if len(self.ventas_diarias) == 0:
            return 0
        return sum(self.ventas_diarias) / len(self.ventas_diarias)

def main():
    registro = RegistroVentas()
    for i in range(7):
        ventas_dia = float(input(f"Ingrese el monto de las ventas del día {i+1}: "))
        registro.agregar_venta(ventas_dia)
    
    total_ventas = registro.calcular_total_ventas()
    promedio_semanal = registro.calcular_promedio_semanal()
    
    print(f"\nEl total de ventas del día es: {total_ventas}")
    print(f"El promedio de ventas diarias de la semana es: {promedio_semanal}")

main()
