import tkinter as tk

racine= tk.Tk()

canvas = tk.Canvas(racine, width =500, height =500,bg= "black")
canvas.grid(column=0,row=0)

def affichage():
    canvas.create_rectangle(fill ="red")

canvas.bind("<Button-1>",affichage)















racine.mainloop()