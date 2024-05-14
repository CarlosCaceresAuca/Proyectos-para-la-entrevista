def ventana4():
    import tkinter as tk
    from PIL import Image, ImageTk
    import math
    import time

    # Función para generar el efecto ondulado celeste en la parte superior
    def draw_waves(canvas, color, wave_count=90):
        canvas_height = int(canvas.cget("height"))
        canvas_width = int(canvas.cget("width"))
        wave_color = color
        delta_x = canvas_width // wave_count
        points = [(0, canvas_height)]
        for i in range(wave_count + 10):
            x = i * delta_x
            y = (canvas_height // 2) * math.sin(i * math.pi / wave_count) + canvas_height // 180
            points.append((x, y))
        points.append((canvas_width, canvas_height))
        points.append((0, canvas_height))
        canvas.create_polygon(points, fill=wave_color, outline="")

#     # Función para importar una imagen
#     def import_image(canvas, image_path):
#         image = Image.open(image_path)
#         photo = ImageTk.PhotoImage(image)
#         canvas.create_image(750, 400, image=photo)  # Ajusta las coordenadas según la posición deseada
#         canvas.image = photo  # Mantener una referencia para evitar que la imagen sea eliminada por el recolector de basura

    # Función para regresar
    def regresar():
        print("Regresando...")
        root.destroy()

    # Función para ejecutar la cuenta regresiva
    def ejecutar():
        tiempo_usuario = entrada_tiempo.get()
        horas, minutos, segundos = map(int, tiempo_usuario.split(':'))

        total_segundos = horas * 3600 + minutos * 60 + segundos

        for i in range(total_segundos, -1, -1):
            tiempo_restante = time.strftime('%H:%M:%S', time.gmtime(i))
            tiempo_actual.config(text=tiempo_restante)
            root.update()
            time.sleep(1)

    # Configurar ventana principal
    root = tk.Tk()
    root.title("Ventana con fondo morado y ondas celestes")
    root.attributes('-fullscreen', True)  # Pantalla completa

    # Configurar canvas para dibujar el fondo
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#7353ac")
    canvas.pack(fill="both", expand=True)

    # Dibujar el efecto ondulado celeste en la parte superior
    draw_waves(canvas, "#54349c")

    # Importar la imagen de Pikachu con transparencia
#     import_image(canvas, "WhatsApp-Image-2024-04-29-at-9.26.11-PM (1).png")  # Asegúrate de tener la imagen pikachu.png en el mismo directorio que este script

    # Agregar texto "Bienvenido al temporizador" en la parte superior de la ventana
    canvas.create_text(root.winfo_screenwidth() // 2, 50, text="Bienvenido al temporizador", font=("Sans Serif", 50), fill="#ded9f7")

    # Agregar texto "Por favor ingrese un valor" en la parte superior de la ventana
    canvas.create_text(root.winfo_screenwidth() // 2, 650, text="Por favor ingrese un valor", font=("Sans Serif", 25), fill="#ded9f7")

    # Botón para regresar
    btn_regresar = tk.Button(root, text="Regresar", font=("Sans Serif", 20), fg="#0c74bc", bg="#ded9f7", bd=3, command=regresar)
    btn_regresar.place(x=20, y=root.winfo_screenheight() - 60)

    # Botón para ejecutar
    btn_ejecutar = tk.Button(root, text="Ejecutar", font=("Sans Serif", 20), fg="#0c74bc", bg="#ded9f7", bd=3, command=ejecutar)
    btn_ejecutar.place(relx=0.5, rely=1, anchor=tk.CENTER, y=-60)

    # Casilla para escribir el tiempo
    entrada_tiempo = tk.Entry(root, font=("Sans Serif", 15), bd=3, bg="#ded9f7", fg="#0c74bc", justify=tk.CENTER)
    entrada_tiempo.place(relx=0.5, rely=0.8, anchor=tk.CENTER, width=300)

    # Label para mostrar el tiempo restante
    tiempo_actual = tk.Label(root, text="00:00:00", font=("Sans Serif", 50), fg="#ded9f7", bg="#7353ac")
    tiempo_actual.place(relx=0.49, rely=0.2, anchor=tk.CENTER)

