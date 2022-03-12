


import tkinter as tk




def creer_rectangle():
    canvas.create_rectangle(50,75,100,150,fill="blue")

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre,width=500,height=500,bg="red")
canvas.grid()

bouton = tk.Button(fenetre,text="ok",fill="blue",command = creer_rectangle)
bouton.grid()

canvas.bind("<Button-1>",creer_rectangle)

fenetre.mainloop()