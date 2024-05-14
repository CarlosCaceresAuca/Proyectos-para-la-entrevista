from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image, ImageTk
import math
import ventana3 as v3
import ventana4 as v4
import ventana5 as v5
root=Tk()
root.bind('<Escape>',lambda e:root.destroy())
root.config(bg="#54349c")
actualvalue=False
button_style = {  
                "font": ("Sans Serif",40),
                "border_color": "#0c74bc", 
                "text_color":"#0c74bc",
                "fg_color":"#ded9f7",
                "hover_color":"#ded9f7",
                "corner_radius": 25
                }
def wait_what():
    messagebox.showinfo(title="wait_what",message="segun franz kevin dijo que haria esto.")
def end():
        root.destroy()
def ventana2():
    def draw_waves_h(canvas, color, wave_count=90):
        canvas_height = int(canvas.cget("height"))
        canvas_width = int(canvas.cget("width"))
        wave_color = color
        delta_y = canvas_height // wave_count
        points = [(0, 0)]
        for i in range(wave_count + 10):
            y = i * delta_y
            x = (canvas_width // 12) * math.sin(i * math.pi / wave_count) + canvas_width // 3
            points.append((x, y))
        points.append((canvas_width, canvas_height))
        points.append((0, canvas_height))
        canvas.create_polygon(points, fill=wave_color, outline="")
    temp=Toplevel()
    temp.config(bg="#7573ac")
    temp.attributes("-fullscreen",1)
    root.bind('<Escape>',lambda e:root.destroy())
    
    canvas=Canvas(temp,width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#54349c",highlightthickness=0)
    canvas.pack(fill="both",expand=1)
    draw_waves_h(canvas, "#7573ac")
    
    CTkButton(temp,text="Control Remoto",**button_style,width=500,height=100,command=heatcontrol).place(anchor="center",relx=0.2,rely=0.3)
    CTkButton(temp,text="Temporizador",**button_style,width=500,height=100,command=temporizador).place(anchor="center",relx=0.2,rely=0.5)
    CTkButton(temp,text="Sensor",**button_style,width=500,height=100,command=temperatura).place(anchor="center",relx=0.2,rely=0.7)
    back=CTkButton(temp,text="atras",**button_style,width=50,height=20,command=temp.destroy)
    back.place(anchor="se",relx=0.98,rely=0.98)
def heatcontrol():
    v3.ventana3()
def temporizador():
    v4.ventana4()
def temperatura():
    v5.ventana5()
def ventana1():
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
    canvas=Canvas(root,width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="#7573ac",highlightthickness=0)
    canvas.pack(fill="both",expand=1)
    draw_waves(canvas, "#54349c")
    CTkButton(root,**button_style
                  ,text="INICIAR"
                  ,width=500
                  ,height=100
                  ,command=ventana2).place(anchor="center",relx=0.5,rely=0.6)
    CTkButton(root,**button_style
                  ,text="REGISTRARSE"
                  ,width=500
                  ,height=100
                  ,command=wait_what).place(anchor="center",relx=0.5,rely=0.75)
root.attributes("-fullscreen",True)
test='Apagado'
ventana1()
root.mainloop()