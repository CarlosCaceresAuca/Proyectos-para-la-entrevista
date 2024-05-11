import tkinter as tk

class AdministradorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def marcar_tarea_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def obtener_tareas_filtradas(self, estado):
        return [tarea for tarea in self.tareas if tarea["completada"] == estado]

def agregar_tarea():
    texto_tarea = entrada_tarea.get()
    if texto_tarea:
        administrador_tareas.agregar_tarea(texto_tarea)
        entrada_tarea.delete(0, tk.END)
        actualizar_lista_tareas()

def marcar_completada(indice):
    administrador_tareas.marcar_tarea_completada(indice)
    actualizar_lista_tareas()

def actualizar_lista_tareas():
    lista_tareas.delete(0, tk.END)
    for i, tarea in enumerate(administrador_tareas.obtener_tareas_filtradas(False)):
        lista_tareas.insert(tk.END, f"{i+1}. {tarea['tarea']}")
        lista_tareas.itemconfig(i, {'bg': 'white'})
        lista_tareas.itemconfig(i, {'cursor': 'hand2'})
        lista_tareas.bind("<Button-1>", lambda event, i=i: marcar_completada(i))

def filtrar_tareas():
    estado = variable_filtro.get()
    lista_tareas.delete(0, tk.END)
    for i, tarea in enumerate(administrador_tareas.obtener_tareas_filtradas(estado)):
        lista_tareas.insert(tk.END, f"{i+1}. {tarea['tarea']}")

administrador_tareas = AdministradorTareas()

raiz = tk.Tk()
raiz.title("Administrador de Tareas")
raiz.geometry("1024x768")

etiqueta_tarea = tk.Label(raiz, text="Nueva Tarea:")
etiqueta_tarea.pack()

entrada_tarea = tk.Entry(raiz, width=50)
entrada_tarea.pack(pady=10)

boton_agregar = tk.Button(raiz, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

variable_filtro = tk.BooleanVar()
variable_filtro.set(False)
boton_pendientes = tk.Radiobutton(raiz, text="Pendientes", variable=variable_filtro, value=False, command=filtrar_tareas)
boton_pendientes.pack(anchor='w')
boton_completadas = tk.Radiobutton(raiz, text="Completadas", variable=variable_filtro, value=True, command=filtrar_tareas)
boton_completadas.pack(anchor='w')

lista_tareas = tk.Listbox(raiz, width=100, height=20)
lista_tareas.pack(pady=20)

actualizar_lista_tareas()

raiz.mainloop()
