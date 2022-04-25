import tkinter as tk
import time
from PIL import Image, ImageTk
import subprocess
import os

ixc=730
iyc=168

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title('CarBoy')
        self.ventana1.iconbitmap('icon.ico')
        archivo = open("datos.txt", "w")
        xVelocity = 1
        yVelocity = 1

        self.canvas1 = tk.Canvas(self.ventana1, width=1280, height=700, background="white")
        self.canvas1.grid(column=0, row=0)

        # fondo
        fondo = tk.PhotoImage(file="imagenes\\background.gif")
        self.canvas1.create_image(0, 0, anchor="nw", image=fondo,)

        # Animacion
        pista = tk.PhotoImage(file="imagenes\\animacion\\pista.png")
        self.canvas1.create_image(560, 53, anchor="nw", image=pista)


        # Casillas estaticas

        self.icon1 = tk.PhotoImage(file="imagenes\\r1.png")
        self.re = self.canvas1.create_image(70, 70, image=self.icon1, anchor="nw")
        #tanque
        self.r2 = self.canvas1.create_image(70, 150, image=self.icon1, anchor="nw")
        self.r21 = self.canvas1.create_image(150, 150, image=self.icon1, anchor="nw")
        self.r22 = self.canvas1.create_image(230, 150, image=self.icon1, anchor="nw")
        #Velocidad
        self.r31 = self.canvas1.create_image(70, 220, image=self.icon1, anchor="nw")
        self.r32 = self.canvas1.create_image(150, 220, image=self.icon1, anchor="nw")
        self.r33 = self.canvas1.create_image(230, 220, image=self.icon1, anchor="nw")

        self.r4 = self.canvas1.create_image(70, 290, image=self.icon1, anchor="nw")

        self.r5 = self.canvas1.create_image(70, 360, image=self.icon1, anchor="nw")
        self.r51 = self.canvas1.create_image(150, 360, image=self.icon1, anchor="nw")

        self.r6 = self.canvas1.create_image(150, 430, image=self.icon1, anchor="nw")

        self.re7 = self.canvas1.create_image(70, 480, image=self.icon1, anchor="nw")
        self.re8 = self.canvas1.create_image(70, 550, image=self.icon1, anchor="nw")
        # Arrastrables

        # Tanque
        archi2 = tk.PhotoImage(file="imagenes\\png\\tanque.png")
        b2 = self.canvas1.create_image(680, 530, image=archi2, anchor="nw", tags="movil")
        archi3 = tk.PhotoImage(file="imagenes\\png\\gasolina.png")
        b3 = self.canvas1.create_image(780, 530, image=archi3, anchor="nw", tags="movil")
        archi4 = tk.PhotoImage(file="imagenes\\tanque\\cTanque_lleno.png")
        lleno = self.canvas1.create_image(880, 530, image=archi4, anchor="nw", tags="movil")
        archi5 = tk.PhotoImage(file="imagenes\\tanque\\Ctanque_medio.png")
        medio = self.canvas1.create_image(950, 530, image=archi5, anchor="nw", tags="movil")
        archi6 = tk.PhotoImage(file="imagenes\\tanque\\Ctanque_cuarto.png")
        cuarto = self.canvas1.create_image(1020, 530, image=archi6, anchor="nw", tags="movil")

        #Direcciones
        archi7 = tk.PhotoImage(file="imagenes\\demas\\izquierda.png")
        izq = self.canvas1.create_image(580, 600, image=archi7, anchor="nw", tags="movil")
        archi8 = tk.PhotoImage(file="imagenes\\demas\\derecha.png")
        dere=self.canvas1.create_image(680, 600, image=archi8, anchor="nw", tags="movil")
        archi9 = tk.PhotoImage(file="imagenes\\demas\\rebasar.png")
        rebasar=self.canvas1.create_image(780, 600, image=archi9, anchor="nw", tags="movil")
        archi13 = tk.PhotoImage(file="imagenes\\demas\\trafico.png")
        trafico = self.canvas1.create_image(950, 610, image=archi13, anchor="nw", tags="movil")

        #condiciones
        archi10 = tk.PhotoImage(file="imagenes\\demas\\si.png")
        si = self.canvas1.create_image(1120, 520, image=archi10, anchor="nw", tags="movil")
        archi11 = tk.PhotoImage(file="imagenes\\demas\\fin.png")
        fin = self.canvas1.create_image(880, 590, image=archi11, anchor="nw", tags="movil")
        archi12 = tk.PhotoImage(file="imagenes\\demas\\inicio.png")
        inicio = self.canvas1.create_image(880, 620, image=archi12, anchor="nw", tags="movil")

        #Velocidades
        self.archi1 = tk.PhotoImage(file="imagenes\\png\\velocidad.png")
        velocidad = self.canvas1.create_image(580, 530, image=self.archi1, anchor="nw", tags="movil")
        archi14 = tk.PhotoImage(file="imagenes\\velocidad\\lento.png")
        lento = self.canvas1.create_image(1050, 583, image=archi14, anchor="nw", tags="movil")
        archi15 = tk.PhotoImage(file="imagenes\\velocidad\\normal.png")
        normal = self.canvas1.create_image(1050, 612, image=archi15, anchor="nw", tags="movil")
        archi16 = tk.PhotoImage(file="imagenes\\velocidad\\rapido.png")
        rapido = self.canvas1.create_image(1050, 640, image=archi16, anchor="nw", tags="movil")

        #Signos
        archi17 = tk.PhotoImage(file="imagenes\\demas\\igual.png")
        igual = self.canvas1.create_image(1150, 583, image=archi17, anchor="nw", tags="movil")
        mayor = self.canvas1.create_image(1150, 612, image=archi17, anchor="nw", tags="movil")
        archi19 = tk.PhotoImage(file="imagenes\\demas\\menor.png")
        menor = self.canvas1.create_image(1150, 640, image=archi19, anchor="nw", tags="movil")

        #Carro
        self.car1 = tk.PhotoImage(file="imagenes\\animacion\\red-car.png")
        self.car11 = tk.PhotoImage(file="imagenes\\animacion\\c2.png")
        self.car12 = tk.PhotoImage(file="imagenes\\animacion\\c3.png")
        self.car13 = tk.PhotoImage(file="imagenes\\animacion\\c4.png")
        self.car2 = tk.PhotoImage(file="imagenes\\animacion\\purple-car.png")
        self.carro2 = self.canvas1.create_image(640, 135, image=self.car2, anchor="nw")
        self.fin = tk.PhotoImage(file="imagenes\\animacion\\fin.png")
        self.malo = tk.PhotoImage(file="imagenes\\animacion\\mal.png")

        self.btnPlay = tk.PhotoImage(file="imagenes\\play.png")
        self.btn = self.canvas1.create_image(200, 600, image=self.btnPlay, anchor="nw", tag="btn")

        self.rei = tk.PhotoImage(file="imagenes\\animacion\\reiniciar.png")

        #eventos
        self.canvas1.tag_bind("btn", "<ButtonPress-1>", self.btnpresionado)
        self.canvas1.tag_bind("btn", "<ButtonPress-1>", self.animacion)

        self.canvas1.tag_bind("btnre", "<ButtonPress-1>", self.btnReinicio)

        #----------
        self.canvas1.tag_bind(inicio, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(inicio, "<Button1-Motion>", self.moverInicio)
        self.canvas1.tag_bind(fin, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(fin, "<Button1-Motion>", self.moverFin)
        self.canvas1.tag_bind(si, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(si, "<Button1-Motion>", self.moversi)

        #Tanque
        self.canvas1.tag_bind(b2, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(b2, "<Button1-Motion>", self.moverTanque)
        self.canvas1.tag_bind(b3, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(b3, "<Button1-Motion>", self.moverGasolina)
        self.canvas1.tag_bind(lleno, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(lleno, "<Button1-Motion>", self.moverLleno)
        self.canvas1.tag_bind(medio, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(medio, "<Button1-Motion>", self.movermedio)
        self.canvas1.tag_bind(cuarto, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(cuarto, "<Button1-Motion>", self.movervacio)

        # fila velocidad
        self.canvas1.tag_bind(velocidad, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(velocidad, "<Button1-Motion>", self.moverVelocidad)
        self.canvas1.tag_bind(lento, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(lento, "<Button1-Motion>", self.moverlento)
        self.canvas1.tag_bind(normal, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(normal, "<Button1-Motion>", self.moverNormal)
        self.canvas1.tag_bind(rapido, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(rapido, "<Button1-Motion>", self.moverRapido)

        #Signos
        self.canvas1.tag_bind(igual, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(igual, "<Button1-Motion>", self.moverigual)
        self.canvas1.tag_bind(mayor, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(mayor, "<Button1-Motion>", self.movermayor)
        self.canvas1.tag_bind(menor, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(menor, "<Button1-Motion>", self.movermenor)

        #fila direcciones

        self.canvas1.tag_bind(trafico, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(trafico, "<Button1-Motion>", self.movertrafico)
        self.canvas1.tag_bind(rebasar, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(rebasar, "<Button1-Motion>", self.moverRebasar)
        self.canvas1.tag_bind(izq, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(izq, "<Button1-Motion>", self.moverIzquierda)
        self.canvas1.tag_bind(dere, "<ButtonPress-1>", self.presionar)
        self.canvas1.tag_bind(dere, "<Button1-Motion>", self.moverDerecha)

        self.opcion_seleccionada = None
        self.animacion2()
        self.ventana1.mainloop()

    def create_circle(self,xs, ys, r):  # center coordinates, radius
        x0 = xs - r
        y0 = ys - r
        x1 = xs + r
        y1 = ys + r

        return self.canvas1.create_oval(x0, y0, x1, y1,fill="green")

    def btnpresionado(self,cInicio):
        print("se presiono boton")

        self.chek()
        print(".")
        print(".")
        #subprocess.call("script2.py", shell=True)

    def btnReinicio(self, cInicio):
        print("se presiono reinicio")
        self.canvas1.delete(self.mal)
        self.canvas1.delete(self.fin)
        self.canvas1.delete(self.btnrei)
        self.chek()



    def presionar(self, evento):
        opcion = self.canvas1.find_withtag(tk.CURRENT)
        self.opcion_seleccionada = (opcion, evento.x, evento.y)

    def renglon1(self,texto):
        archivo = open("datos.txt", "a")
        archivo.write(texto)

    def chek(self):
        global cInicio
        try:
            if co[0] in range(66, 85) and co[1] in range(66, 95):
                print("r1")
                self.renglon1("Inicio:\n")
                self.create_circle(400, 90, 15)

                if ct[0] in range(60, 85) and ct[1] in range(145, 172):
                    print("r2")
                    self.renglon1("Tanque")
                    if coIgual[0] in range(142, 170) and coIgual[1] in range(142, 170):
                        print("r21")
                        self.renglon1(" = ")
                        if ctl[0] in range(228, 250) and ctl[1] in range(147, 160):
                            print("r22")
                            self.renglon1("Lleno \n")
                            self.create_circle(400, 170, 15)

                if cVelo[0] in range(55, 85) and cVelo[1] in range(200, 225):
                    print("r3")
                    self.renglon1("Velocidad")
                    if coMayor[0] in range(142, 170) and coMayor[1] in range(215, 238):
                        print("r31")
                        self.renglon1(" = ")
                        if cVeloN[0] in range(220, 250) and cVeloN[1] in range(220, 245):
                            print("r32")
                            self.renglon1("Normal \n")
                            self.create_circle(400, 250, 15)

                    if coDerecha[0] in range(55, 85) and coDerecha[1] in range(276, 305):
                        print("r4")
                        self.renglon1("Derecha \n")
                        self.create_circle(400, 310, 15)

                        if co21[0] in range(55, 72) and co21[1] in range(348, 360):
                            print("r5")
                            self.renglon1("Si")
                            if co2[0] in range(142, 170) and co2[1] in range(355, 385):
                                print("r51")
                                self.renglon1(" Trafico\n")
                                self.create_circle(400, 380, 15)

                            if coRebasar[0] in range(130, 170) and coRebasar[1] in range(414, 445):
                                print("r61")
                                self.renglon1("Rebasar\n")
                                self.create_circle(400, 450, 15)

                                if coizquierda[0] in range(53, 90) and coizquierda[1] in range(465, 490):
                                    print("r71")
                                    self.renglon1("Izquierda\n")
                                    self.create_circle(400, 510, 15)

                                    if coFin[0] in range(65, 85) and coFin[1] in range(544, 573):
                                        print("r81")
                                        self.renglon1("Fin:\n")
                                        self.create_circle(400, 580, 15)
                                        return True
            else:
                print("incorrecto")
                self.renglon1("error\n")

        except:
            print("Faltan casillas por rellenar")
            return False

#-------------------------------------
    def moverInicio(self, evento):
        global co
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        co = self.canvas1.coords(tk.CURRENT)
        print("-inicio-----" + str(co))
    def moverFin(self, evento):
        global coFin
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coFin = self.canvas1.coords(tk.CURRENT)
        print("-Fin-----" + str(coFin))
#Velocidades
    def moverVelocidad(self, evento):
        global cVelo
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        cVelo = self.canvas1.coords(tk.CURRENT)
        print("-velocidad-----" + str(cVelo))
    def moverlento(self, evento):
        global cVeloL
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        cVeloL = self.canvas1.coords(tk.CURRENT)
        print("-Lento-----" + str(cVeloL))
    def moverRapido(self, evento):
        global cVeloR
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        cVeloR = self.canvas1.coords(tk.CURRENT)
        print("-Rapido-----" + str(cVeloR))
    def moverNormal(self, evento):
        global cVeloN
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        cVeloN = self.canvas1.coords(tk.CURRENT)
        print("-Normal-----" + str(cVeloN))

#Tanque
    def moverTanque(self, evento):
        global ct
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        ct = self.canvas1.coords(tk.CURRENT)
        print("-Tanque-----" + str(ct))
    def moverGasolina(self, evento):
        global cg
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        cg = self.canvas1.coords(tk.CURRENT)
        print("-gasolina-----" + str(cg))
    def moverLleno(self, evento):
        global ctl
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        ctl = self.canvas1.coords(tk.CURRENT)
        print("-LLeno-----" + str(ctl))
    def movervacio(self, evento):
        global ctva
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        ctva = self.canvas1.coords(tk.CURRENT)
        print("-vacio-----" + str(ctva))
    def movermedio(self, evento):
        global ctme
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        ctme = self.canvas1.coords(tk.CURRENT)
        print("-medio-----" + str(ctme))
#Direcciones
    def moverIzquierda(self, evento):
        global coizquierda
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coizquierda = self.canvas1.coords(tk.CURRENT)
        print("-izquierda-----" + str(coizquierda))
    def moverDerecha(self, evento):
        global coDerecha
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coDerecha = self.canvas1.coords(tk.CURRENT)
        print("-derecha-----" + str(coDerecha))
    def moverRebasar(self, evento):
        global coRebasar
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coRebasar = self.canvas1.coords(tk.CURRENT)
        print("-rebasar-----"+str(coRebasar))
    def movertrafico(self, evento):
        global co2
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        co2 = self.canvas1.coords(tk.CURRENT)
        print("-trafico-----"+str(co2))
    def moversi(self, evento):
        global co21
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        co21 = self.canvas1.coords(tk.CURRENT)
        print("-si-----"+str(co21))

#Signos
    def moverigual(self, evento):
        global coIgual
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coIgual = self.canvas1.coords(tk.CURRENT)
        print("-igual-----"+str(coIgual))
    def movermayor(self, evento):
        global coMayor
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coMayor = self.canvas1.coords(tk.CURRENT)
        print("-Mayor-----" + str(coMayor))
    def movermenor(self, evento):
        global coMenor
        x, y = evento.x, evento.y
        opcion, x1, y1 = self.opcion_seleccionada
        self.canvas1.move(opcion, x - x1, y - y1)
        self.opcion_seleccionada = (opcion, x, y)
        coMenor = self.canvas1.coords(tk.CURRENT)
        print("-Menor-----" + str(coMenor))

    def animacion2(self):
        while True:
            a1x = 641
            a1y = 135
            for i in range(0, 40):
                a1y += 3
                time.sleep(0.05)
                self.canvas1.coords(self.carro2, a1x, a1y)
                self.ventana1.update()
            for i in range(0, 40):
                a1y -= 3
                time.sleep(0.05)
                self.canvas1.coords(self.carro2, a1x, a1y)
                self.ventana1.update()

    def animacion(self,cInicio):
        if self.chek():
            time.sleep(0.5)
            self.carro11 = self.canvas1.create_image(1000, 1000, image=self.car11, anchor="nw")
            self.carro11 = self.canvas1.create_image(1000, 1000, image=self.car11, anchor="nw")
            self.carro12 = self.canvas1.create_image(1000, 1000, image=self.car12, anchor="nw")
            self.carro13 = self.canvas1.create_image(1000, 1000, image=self.car13, anchor="nw")
            self.carro1 = self.canvas1.create_image(1000, 1000, image=self.car1, anchor="nw")
            while True:
                ax = 725
                ay = 168
                for i in range(0, 30):

                    print(i)
                    ay-=3
                    time.sleep(0.05)
                    self.canvas1.coords(self.carro1,ax,ay)
                    print(ay)
                    self.ventana1.update()

                for i in range(0,20):
                    self.canvas1.delete(self.carro1)
                    ax-=3
                    time.sleep(0.05)
                    self.canvas1.coords(self.carro11, ax, ay)
                    print(ax)
                    self.ventana1.update()


                for i in range(0, 70):
                    self.canvas1.delete(self.carro11)
                    print(i)
                    ay += 3
                    time.sleep(0.05)
                    self.canvas1.coords(self.carro12, ax, ay)
                    print(ay)
                    self.ventana1.update()

                for i in range(0,50):
                    self.canvas1.delete(self.carro12)
                    ax += 3
                    for ii in range(0,1):
                        ay += 2
                        time.sleep(0.05)
                        self.canvas1.coords(self.carro13, ax, ay)
                        print(ay)
                        self.ventana1.update()

                self.canvas1.delete(self.carro13)
                self.final = self.canvas1.create_image(500, 250, image=self.fin, anchor="nw")
                time.sleep(1)
                self.btnrei = self.canvas1.create_image(510, 405, image=self.rei, anchor="nw", tag="btnre")
                print("Fin")

        else:
            self.mal = self.canvas1.create_image(500, 250, image=self.malo, anchor="nw")
            print("NO!")
            time.sleep(1)
            self.btnrei = self.canvas1.create_image(510, 405, image=self.rei, anchor="nw", tag="btnre")
aplicacion1 = Aplicacion()
