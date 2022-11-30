from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH
import tkinter.font
from modul_glbb import glbb

root = Tk()
root.geometry('300x300')

changefont = tkinter.font.Font(size=20)
Title = Label(root, text = "GLBB", font = changefont)
Title.place(x=115, y=10)

x = Label(root, text = 'Kecepatan Awal')
y = Label(root, text = 'Akselerasi Awal')
z = Label(root, text = 'Waktu')

e1 = Entry(root,width=40)
e2 = Entry(root,width=40)
e3 = Entry(root,width=40)

x.place(x = 113, y = 50)
y.place(x = 114, y = 90)
z.place(x = 133, y = 130)

e1.place(x = 28, y = 70)
e2.place(x = 28, y = 110)
e3.place(x = 28, y = 150)

def plot():
    v0 = float(e1.get())
    a = float(e2.get())
    t = float(e3.get())
    glbb(v0,t,a)

plot_button = Button(master = root,
                    command=plot,
                    text='Hitung Kecepatan dan Jarak')
plot_button.place(x = 70, y = 190)
root.mainloop()