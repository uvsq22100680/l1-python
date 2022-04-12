import tkinter as tk
import random as rd

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
CPT = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon-100, y-rayon),
                                (x+rayon-100, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]

def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global CPT
    if CPT < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, CPT
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        CPT += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        CPT += 1
    aleatoire = rd.randint(0, 100)
    x0_l, y0_l, x1_l, y1_l = canvas.coords(ligne)
    if aleatoire < 10:
        if not (350 >= x1 >= 250 and 250 <= x0 <= 350):
            canvas.coords(ligne, 300, 0, 300, 400)
        else:
            canvas.coords(ligne, 650, 0, 650, 400)
    x0_l, y0_l, x1_l, y1_l = canvas.coords(ligne)
    if (x1 >= x1_l and x0 <= 300) or (x1 <= x1_l and x0 >= 300) and x0_l < 650:
        balle[1] = -balle[1]
        CPT += 1

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

ligne = canvas.create_line(LARGEUR//2, 0, LARGEUR//2, 400, fill="white")

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
