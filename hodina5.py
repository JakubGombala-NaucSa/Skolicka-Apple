import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="turquoise")
platno.pack()

lopticky = []

def Start():
    vytvor_gulicky()

def vytvor_gulicky():
    for i in range(10):
        gulicka = platno.create_oval(10 + i*20, 10, 30 + i*20, 30, fill="red")
        lopticky.append(gulicka)

Start()
