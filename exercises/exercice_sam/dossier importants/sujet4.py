import tkinter as tk

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

    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)
        
    
def rebond():

    """Fait rebondir la balle sur les bords du canevas"""
    global balle,cpt,x0, y0, x1, y1
    x0, y0, x1, y1 = canvas.coords(balle[0])
    changement_ballon()
    
    if cpt <30:

        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            cpt+=1

        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            cpt+=1
    else:
         balle[1],balle[2]=0,0
    
def changement_ballon():
    global x0, y0, x1, y1,cpt
    if cpt == 5 or cpt == 15 or cpt == 25:
        canvas.delete(balle[0])
        balle[0]=canvas.create_rectangle(x0,y0,x1,y1,fil="blue")
        cpt +=1
    
    elif cpt == 10 or cpt == 20 or cpt == 30:
        canvas.delete(balle[0])
        balle[0]=canvas.create_oval(x0,y0,x1,y1,fil="blue")
        cpt +=1
       

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()


# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()
