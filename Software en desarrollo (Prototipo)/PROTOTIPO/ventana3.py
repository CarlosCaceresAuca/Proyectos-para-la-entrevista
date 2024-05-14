def ventana3():
    import tkinter as tk
    from PIL import Image, ImageTk
    import math
    from customtkinter import CTkButton
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

#     def import_image(canvas, image_path):
#         image = Image.open(image_path)
#         photo = ImageTk.PhotoImage(image)
#         canvas.create_image(940, 270, image=photo) 
#         canvas.image = photo  


    def ejecutar():
        print("Ejecutando...")

    def encender():
        print("¡Conexión establecida correctamente!")
        # Agregar mensaje de conexión establecida
        canvas.create_text(root.winfo_screenwidth() // 2, root.winfo_screenheight() - 100, text="Conectado correctamente", font=("Sans Serif", 50), fill="#ded9f7")

    root = tk.Tk()
    root.title("Ventana con fondo morado y ondas celestes")
    root.attributes('-fullscreen', True)  

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#7353ac")
    canvas.pack(fill="both", expand=True)

    draw_waves(canvas, "#54349c")

#     import_image(canvas, "Group 1.png")  # Asegúrate de tener la imagen pikachu.png en el mismo directorio que este script

    canvas.create_text(root.winfo_screenwidth() // 2, 50, text="Heat Control", font=("Sans Serif", 50), fill="#ded9f7")

    btn_ejecutar = tk.Button(root, text="Encender", font=("Sans Serif", 30), fg="#0c74bc", bg="#ded9f7", bd=3, command=encender)
    btn_ejecutar.place(relx=0.49, rely=1, anchor=tk.CENTER, y=-350)

    CTkButton(root,text="atras",width=100,height=100,command=root.destroy).place(anchor="se",relx=1,rely=1)
