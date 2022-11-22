import tkinter as tk
import tkinter.font
from tkinter import *
from tkinter.messagebox import showinfo

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import rumus_glbb as glbb

root = Tk()
root.geometry('600x600')

changefont = tkinter.font.Font(size=20)
Title = Label(root, text = "GLBB", font = changefont)
Title.place(x=250, y=10)

labelfr = LabelFrame(root, text="result", padx=20,pady=20)
labelfr.place(x=60,y=300)

x = Label(root,text = "Kecepatan Awal")
y = Label(root,text = "Akselerasi Awal")
z = Label(root,text = "Waktu")

e1 = Entry(root,width=80)
e2 = Entry(root,width=80)
e3 = Entry(root,width=80)

x.place(x = 250, y = 50)
y.place(x = 250, y = 90)
z.place(x = 250, y = 130)

e1.place(x = 55, y = 70)
e2.place(x = 55, y = 110)
e3.place(x = 55, y = 150)

e1= tk.DoubleVar()
e2= tk.DoubleVar()
e3= tk.DoubleVar()

def akhir():
    Vt = e1.get()+e2.get()*e3.get()
    hasil = print(Vt)
    showinfo("Kecepatan Akhir sebesar ", message=str(hasil))
def jarak():
    s = e1.get()*e3.get() + ((e2.get()*(e3.get()**2))/2)
    hasil = print(s)
    showinfo("Jarak", hasil)

btn = Button(root,text="Kecepatan Akhir", command=akhir).place(x = 55, y=190)
btn = Button(root,text="Jarak", command=jarak).place(x=155, y=190)

root.mainloop()