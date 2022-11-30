import tkinter as tk
from turtle import *
import turtle
import threading

def glbb(v0,t,a):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=400)
    canvas.pack()

    def semua(v0,t,a):
        tp = turtle.RawTurtle(canvas)
        sizefont = 18
        sizef = 15
        FONT = ('Halvetica', sizefont, 'normal')
        Font = ('Halvetica', sizef, 'normal')
        tp.penup()
        tp.pensize(3)
        tp.goto(-100,0)
        tp.pendown()
        s = v0*t + ((a*(t**2))/2)
        Vt = v0 + a*t
        tp.fillcolor('cyan')
        tp.forward(200)
        tp.penup()
        tp.write(" "+str(s)+" m", font=Font)
        tp.penup()
        tp.goto(-240,50)
        tp.pendown()
        tp.write("Kecepatan Akhir Sebesar : " + str(Vt) + "  m/s", font=FONT)
        tp.hideturtle()
        
    
    t1 = threading.Thread(target=semua, args=(v0,t,a))
    t1.start()
    root.mainloop()