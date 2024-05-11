import tkinter as tk
from tkinter import ttk

def calcular_propina():
    total_cuenta = float(entrada_total_cuenta.get())
    porcentaje_propina = float(combobox_porcentaje_propina.get())
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina
    etiqueta_resultado.config(text=f"Propina: ${propina:.2f}\nTotal a pagar: ${total_a_pagar:.2f}")

ventana = tk.Tk()
ventana.title("Calculadora de Propinas")
ventana.geometry("400x200")
ventana.configure(bg="black")

etiqueta_total_cuenta = ttk.Label(ventana, text="Total de la cuenta:", foreground="white", background="black")
etiqueta_total_cuenta.grid(row=0, column=0, padx=10, pady=10)
entrada_total_cuenta = ttk.Entry(ventana)
entrada_total_cuenta.grid(row=0, column=1, padx=10, pady=10)

etiqueta_porcentaje_propina = ttk.Label(ventana, text="Porcentaje de propina:", foreground="white", background="black")
etiqueta_porcentaje_propina.grid(row=1, column=0, padx=10, pady=10)
porcentajes = [10, 15, 20, 25]
combobox_porcentaje_propina = ttk.Combobox(ventana, values=porcentajes)
combobox_porcentaje_propina.grid(row=1, column=1, padx=10, pady=10)
combobox_porcentaje_propina.current(0)

boton_calcular = ttk.Button(ventana, text="Calcular Propina", command=calcular_propina)
boton_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

etiqueta_resultado = ttk.Label(ventana, text="", foreground="white", background="black")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
