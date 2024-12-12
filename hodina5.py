import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="turquoise")
platno.pack()

lopticky = []

def Start():
    vytvor_gulicky()

def vytvor_gulicky():
    posun = -10
    for i in range(10):
        posun += 20
        gulicka = platno.create_oval(10 + posun, 10, 30 + posun, 30, fill="red")
        lopticky.append(gulicka)
        posun += 10

def Hra():
    for lopticka in lopticky:
        platno.move(lopticka, 0, 10)
    platno.after(100, Hra)
        

Start()
Hra()
