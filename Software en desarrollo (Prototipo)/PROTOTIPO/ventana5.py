def ventana5():
    import tkinter as tk
    from PIL import Image, ImageTk
    import math

    # Función para generar el efecto ondulado celeste apuntando hacia la derecha
    def draw_waves(canvas, color, wave_count=90):
        canvas_height = int(canvas.cget("height"))
        canvas_width = int(canvas.cget("width"))
        wave_color = color
        delta_y = canvas_height // wave_count
        points = [(0, 0)]
        for i in range(wave_count + 10):
            y = i * delta_y
            x = (canvas_width // 12) * math.sin(i * math.pi / wave_count) + canvas_width // 4.5
            points.append((x, y))
        points.append((canvas_width, canvas_height))
        points.append((0, canvas_height))
        canvas.create_polygon(points, fill=wave_color, outline="")

    # Función para importar una imagen
#     def import_image(canvas, image_path):
#         image = Image.open(image_path)
#         photo = ImageTk.PhotoImage(image)
#         canvas.create_image(300, 410, image=photo)  # Ajusta las coordenadas según la posición deseada
#         canvas.image = photo  # Mantener una referencia para evitar que la imagen sea eliminada por el recolector de basura

    # Función para actualizar la temperatura gradualmente
    def actualizar_temperatura(canvas, valor):
        temperatura_actual = obtener_temperatura_actual(canvas)
        if temperatura_actual < valor:
            aumentar_temperatura(canvas, temperatura_actual, valor)
        elif temperatura_actual > valor:
            disminuir_temperatura(canvas, temperatura_actual, valor)

    # Función para obtener la temperatura actual
    def obtener_temperatura_actual(canvas):
        try:
            temperatura_actual = int(canvas.itemcget("temperatura", "text").split(" ")[0])
        except:
            temperatura_actual = 0
        return temperatura_actual

    # Función para aumentar gradualmente la temperatura
    def aumentar_temperatura(canvas, valor_actual, valor_deseado):
        def animacion():
            nonlocal valor_actual
            if valor_actual <= valor_deseado:
                canvas.delete("temperatura")
                canvas.create_text(root.winfo_screenwidth() // 1.8, 390, text=f"{valor_actual} °C", font=("Sans Serif", 300), fill="#ded9f7", tag="temperatura")
                valor_actual += 1
                root.after(100, animacion)
        animacion()

    # Función para disminuir gradualmente la temperatura
    def disminuir_temperatura(canvas, valor_actual, valor_deseado):
        def animacion():
            nonlocal valor_actual
            if valor_actual >= valor_deseado:
                canvas.delete("temperatura")
                canvas.create_text(root.winfo_screenwidth() // 1.8, 390, text=f"{valor_actual} °C", font=("Sans Serif", 300), fill="#ded9f7", tag="temperatura")
                valor_actual -= 1
                root.after(100, animacion)
        animacion()

    # Función para regresar
    def regresar():
        print("Regresando...")
        root.destroy()

    # Función para ejecutar
    def ejecutar():
        temperatura = int(entrada_tiempo.get())
        actualizar_temperatura(canvas, temperatura)
        print("Ejecutando...")

    # Configurar ventana principal
    root = tk.Tk()
    root.title("Ventana con fondo morado y ondas celestes")
    root.attributes('-fullscreen', True)  # Pantalla completa

    # Configurar canvas para dibujar el fondo
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#7353ac")
    canvas.pack(fill="both", expand=True)

    # Dibujar el efecto ondulado celeste apuntando hacia la derecha
    draw_waves(canvas, "#54349c")

    # Importar la imagen de Pikachu con transparencia
#     import_image(canvas, "Designer (17) 1.png")  # Asegúrate de tener la imagen pikachu.png en el mismo directorio que este script

    # Agregar texto "La Temperatura actual es:" en la parte superior de la ventana
    canvas.create_text(root.winfo_screenwidth() // 2, 50, text="La Temperatura actual es:", font=("Sans Serif", 50), fill="#ded9f7")

    # Casilla para escribir el tiempo
    entrada_tiempo = tk.Entry(root, font=("Sans Serif", 15), bd=3, bg="#ded9f7", fg="#0c74bc", justify=tk.CENTER)
    entrada_tiempo.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=300)

    # Agregar texto "Ingrese la temperatura deseada" en la parte superior de la ventana
    canvas.create_text(root.winfo_screenwidth() // 2, 650, text="Ingrese la temperatura deseada", font=("Sans Serif", 20), fill="#ded9f7")

    # Botón para ejecutar
    btn_ejecutar = tk.Button(root, text="Ejecutar", font=("Sans Serif", 20), fg="#0c74bc", bg="#ded9f7", bd=3, command=ejecutar)
    btn_ejecutar.place(relx=0.5, rely=1, anchor=tk.CENTER, y=-60)

    # Botón para regresar
    btn_regresar = tk.Button(root, text="Regresar", font=("Sans Serif", 20), fg="#0c74bc", bg="#ded9f7", bd=3, command=regresar)
    btn_regresar.place(x=1380, y=root.winfo_screenheight() - 60)

