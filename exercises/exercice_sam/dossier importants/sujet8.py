import tkinter as tk
import random as rd

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt=0

###################
# Fonctions



def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global nombre_aleatoire,id_after
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    id_after =canvas.after(20, mouvement)
    nombre_aleatoire = rd.randint(0,101)
    if nombre_aleatoire < 5:
        canvas.after_cancel(id_after)
        
        
    


def rebond():

    """Fait rebondir la balle sur les bords du canevas"""
    global balle,x0,x1,y0,y1,cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])

    if cpt < 30:
        if x0 <= 0 or x1 >= 600:
             balle[1] = -balle[1]
             cpt +=1

        if y0 <= 0 or y1 >= 400:
             balle[2] = -balle[2]
             cpt+=1
        
    else:
        balle[1], balle[2] = 0,0


def balle_clic(event):
    global x0,x1,y0,y1,nombre_aleatoire
    if x0<event.x<x1 and y0 <event.y<y1:
        canvas.coords(balle[0],x0,y0,x1-5,y1-5)
        canvas.after(20,mouvement)
    else:
        canvas.coords(balle[0],x0,y0,x1+5,y1+5)
        canvas.after(20,mouvement)
    
        

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
canvas.bind("<Button-1>",balle_clic)

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()
