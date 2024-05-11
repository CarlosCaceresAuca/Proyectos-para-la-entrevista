import tkinter as tk
from tkinter import ttk

class ListaCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append({"nombre": item, "comprado": False})

    def marcar_comprado(self, indice):
        if 0 <= indice < len(self.items):
            self.items[indice]["comprado"] = True

    def eliminar_item(self, indice):
        if 0 <= indice < len(self.items):
            del self.items[indice]

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += 1 
        return total

def agregar_item():
    item = entrada_item.get()
    if item:
        lista_compras.agregar_item(item)
        actualizar_lista()

def marcar_comprado():
    seleccion = lista.get(tk.ACTIVE)
    if seleccion:
        indice = lista.get(0, tk.END).index(seleccion)
        lista_compras.marcar_comprado(indice)
        actualizar_lista()

def eliminar_item():
    seleccion = lista.get(tk.ACTIVE)
    if seleccion:
        indice = lista.get(0, tk.END).index(seleccion)
        lista_compras.eliminar_item(indice)
        actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for item in lista_compras.items:
        estado = "Comprado" if item["comprado"] else "Pendiente"
        lista.insert(tk.END, f"{item['nombre']} - {estado}")

def calcular_total():
    total = lista_compras.calcular_total()
    etiqueta_total.config(text=f"Total: ${total:.2f}")

ventana = tk.Tk()
ventana.title("Lista de Compras")
ventana.geometry("400x500") 
ventana.configure(bg="black")

etiqueta_item = ttk.Label(ventana, text="Nuevo Elemento:", foreground="white", background="black")
etiqueta_item.pack(pady=10)
entrada_item = ttk.Entry(ventana)
entrada_item.pack()

boton_agregar = ttk.Button(ventana, text="Agregar", command=agregar_item)
boton_agregar.pack()

lista = tk.Listbox(ventana, background="black", foreground="white", selectbackground="gray", selectforeground="black")
lista.pack(pady=10, expand=True, fill=tk.BOTH)  

boton_marcar = ttk.Button(ventana, text="Marcar como Comprado", command=marcar_comprado)
boton_marcar.pack()

boton_eliminar = ttk.Button(ventana, text="Eliminar", command=eliminar_item)
boton_eliminar.pack()

etiqueta_total = ttk.Label(ventana, text="", foreground="white", background="black")
etiqueta_total.pack(pady=10)

boton_total = ttk.Button(ventana, text="Calcular Total", command=calcular_total)
boton_total.pack()

lista_compras = ListaCompras()

ventana.mainloop()
