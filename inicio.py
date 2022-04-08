import tkinter as tk
import subprocess
import os


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('CarBoy')
        self.ventana1.iconbitmap('icon.ico')
        archivo = open("datos.txt", "w")


        self.canvas1 = tk.Canvas(self.ventana1, width=1280, height=700, background="white")
        self.canvas1.grid(column=0, row=0)

        # fondo
        fondo = tk.PhotoImage(file="C:\\Users\\user\\Desktop\\proyectoCopiladores\\img\\background.gif")
        self.canvas1.create_image(0, 0, anchor="nw", image=fondo)

        # Casillas estaticas


        self.icon1 = tk.PhotoImage(file="C:\\Users\\user\\Desktop\\proyectoCopiladores\\img\\r1.png")
        self.re = self.canvas1.create_image(70, 70, image=self.icon1, anchor="nw")
        self.re2 = self.canvas1.create_image(70, 150, image=self.icon1, anchor="nw")
        self.re21 = self.canvas1.create_image(150, 150, image=self.icon1, anchor="nw")

        self.re3 = self.canvas1.create_image(70, 220, image=self.icon1, anchor="nw")
        self.re4 = self.canvas1.create_image(70, 290, image=self.icon1, anchor="nw")
        self.re41 = self.canvas1.create_image(150, 290, image=self.icon1, anchor="nw")

        self.re5 = self.canvas1.create_image(150, 360, image=self.icon1, anchor="nw")
        self.re51 = self.canvas1.create_image(230, 360, image=self.icon1, anchor="nw")

        self.re6 = self.canvas1.create_image(70, 430, image=self.icon1, anchor="nw")
        # Arrastrables
        self.archi1 = tk.PhotoImage(file="png\\velocidad.png")
        b1 = self.canvas1.create_image(580, 530, image=self.archi1, anchor="nw", tags="movil")

        archi2 = tk.PhotoImage(file="png\\tanque.png")
        b2 = self.canvas1.create_image(680, 530, image=archi2, anchor="nw", tags="movil")

        archi3 = tk.PhotoImage(file="png\\gasolina.png")
        b3 = self.canvas1.create_image(780, 530, image=archi3, anchor="nw", tags="movil")

        archi4 = tk.PhotoImage(file="tanque\\cTanque_lleno.png")
        b4 = self.canvas1.create_image(880, 530, image=archi4, anchor="nw", tags="movil")

        archi5 = tk.PhotoImage(file="tanque\\Ctanque_medio.png")
        b5 = self.canvas1.create_image(980, 530, image=archi5, anchor="nw", tags="movil")

        archi6 = tk.PhotoImage(file="tanque\\Ctanque_cuarto.png")
        b6 = self.canvas1.create_image(1080, 530, image=archi6, anchor="nw", tags="movil")

        archi7 = tk.PhotoImage(file="demas\\izquierda.png")
        b7 = self.canvas1.create_image(580, 600, image=archi7, anchor="nw", tags="movil")

        archi8 = tk.PhotoImage(file="demas\\derecha.png")
        self.canvas1.create_image(680, 600, image=archi8, anchor="nw", tags="movil")

        archi9 = tk.PhotoImage(file="demas\\rebasar.png")
        self.canvas1.create_image(780, 600, image=archi9, anchor="nw", tags="movil")

        archi10 = tk.PhotoImage(file="demas\\si.png")
        self.canvas1.create_image(1180, 530, image=archi10, anchor="nw", tags="movil")

        archi11 = tk.PhotoImage(file="demas\\fin.png")
        fin=self.canvas1.create_image(880, 590, image=archi11, anchor="nw", tags="movil")

        archi12 = tk.PhotoImage(file="demas\\inicio.png")
        inicio=self.canvas1.create_image(880, 620, image=archi12, anchor="nw", tags="movil")

        archi13 = tk.PhotoImage(file="demas\\trafico.png")
        trafico=self.canvas1.create_image(980, 610, image=archi13, anchor="nw", tags="movil")

        self.btnPlay = tk.PhotoImage(file="C:\\Users\\user\\Desktop\\proyectoCopiladores\\img\\play.png")
        self.btn = self.canvas1.create_image(200, 600, image=self.btnPlay, anchor="nw",tag="btn")

        self.canvas1.tag_bind("btn", "<ButtonPress-1>", self.btnpresionado)
        self.canvas1.tag_bind(inicio, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(inicio, "<Button1-Motion>", self.mover)
        self.opcion_seleccionada = None

        self.ventana1.mainloop()

    def btnpresionado(self,arg):
        print("se presiono boton")
        subprocess.call("script2.py", shell=True)


    def renglon1(self,texto):
        archivo = open("datos.txt", "w")
        archivo.write(texto)

    def presionar(self, evento):
        opcion = self.canvas1.find_withtag(tk.CURRENT)
        self.opcion_seleccionada = (opcion, evento.x, evento.y)

    def mover(self, evento):
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        print("X: " + str(evento.x) + " Y: " + str(evento.y))
        a1 = self.canvas1.bbox(self.re)
        b = self.canvas1.bbox(tk.CURRENT)
        print(a1)
        print(b)
        texto = "Inicio:"
        texto2 = "Error"
        if b[0] in range(a1[0], a1[2]) or b[2] in range(a1[0], a1[2]) and b[1] in range(a1[1], a1[3]) or b[3] in range(a1[1],a1[3]):
            print("colision r1 --Inicio")
            self.renglon1(texto)
        else:
            print("error de posicion")
            self.renglon1(texto2)

aplicacion1 = Aplicacion()
