import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt =0

###################
# Fonctions



def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon-250, y-rayon),
                                (x+rayon-250, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""

    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)
    canvas.move(ligne1,1,0)
    canvas.move(ligne2,1,0)  
    


def rebond():

    """Fait rebondir la balle sur les bords du canevas"""
    global balle,cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])

    if cpt <30:
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            cpt +=1
        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            cpt+=1
    else:
        balle[1],balle[2]=0,0
    

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

ligne1 = canvas.create_line(1,0,1,HAUTEUR,fil="yellow")
ligne2 = canvas.create_line(150,0,150,HAUTEUR,fil="yellow")

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()
