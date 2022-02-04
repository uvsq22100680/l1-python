import tkinter as tk
import random

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

dessin= tk.Tk()
canvas = tk.Canvas(dessin, width =255, height =255,bg= "black")
canvas.grid(column=2, row=1, rowspan=3)

def draw_pixel(i, j, color):
  canvas.create_rectangle(i,j,i+1,j+1,fill=color,width=0)

def ecran_aleatoire():
    for i in range(255):
        for j in range(255):
            
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            couleur = get_color(red, green, blue)
            draw_pixel(i, j, couleur)

def degrade_gris():
    for i in range(255):
        for j in range(255):
            couleur = get_color(i,i,i)
            draw_pixel(i, j, couleur)


def degrade_2D():


            





bouton1 = tk.Button(dessin, text = "aléatoire", font=("helvetica","20"), command = ecran_aleatoire)
bouton1.grid()
bouton1.grid(column=0, row = 1)

bouton2 = tk.Button(dessin, text = "dégradé gris", font=("helvetica","20"),command =degrade_gris)
bouton2.grid()
bouton2.grid(column=0, row = 2)

bouton3 = tk.Button(dessin, text = "dégradé 2D", font=("helvetica","20"))
bouton3.grid()
bouton3.grid(column=0, row = 3)



dessin.mainloop()