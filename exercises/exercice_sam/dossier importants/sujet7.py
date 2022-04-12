#programme qui rebondit balle sur trait verticale augmente de 50 lors d'un rebond sur le trait verticale et diminue de 1 lorsque que balle avance


import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400


#variable
cpt =0
coordx=LARGEUR//2

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
    global coordx
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)
    canvas.move(ligne_blanche,-1,0)
    coordx-=1


def rebond():

    """Fait rebondir la balle sur les bords du canevas"""
    global balle,ligne_blanche,cpt,coordx
    x0, y0, x1, y1 = canvas.coords(balle[0])

    if cpt<30:   
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            cpt+=1

        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            cpt+=1
    
        if x1 >= coordx:
            balle[1] = -balle[1]
            canvas.move(ligne_blanche,50,0)
            cpt+=1
            coordx+=50
    else:
        balle[1],balle[2]=0,0



        
    

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

ligne_blanche = canvas.create_line(LARGEUR//2,0,coordx,HAUTEUR,fil="white")

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()
