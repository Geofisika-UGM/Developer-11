import tkinter as tk
from turtle import *
import turtle
import threading

def glbb(v0,t,a):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=600)
    canvas.pack()

    def semua(v0,t,a):
        tp = turtle.RawTurtle(canvas)
        tp.penup()
        tp.goto(-100,-150)
        tp.pendown()
        s = v0*t + ((a*(t**2))/2)
        Vt = v0 + a*t
        tp.fillcolor('cyan')
        tp.forward(200)
        tp.penup()
        tp.write(" "+str(s)+" m")
        tp.penup()
        tp.goto(-100,-170)
        tp.pendown()
        tp.write("Kecepatan Akhir Sebesar : " + str(Vt) + "  m/s")
        tp.hideturtle()
        
    
    t1 = threading.Thread(target=semua, args=(v0,t,a))
    t1.start()
    root.mainloop()