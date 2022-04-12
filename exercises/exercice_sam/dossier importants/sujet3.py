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
    global balle,cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    
    if cpt <30:

        if x0 <= 0 :
            balle[1] = -balle[1]
            canvas.itemconfigure(balle[0],fill="yellow")
            cpt+=1
    
        if x1 >= 600:
             balle[1] = -balle[1]
             canvas.itemconfigure(balle[0],fill="green")
             cpt+=1

        if y0 <= 0 :
            balle[2] = -balle[2]
            canvas.itemconfigure(balle[0],fill="red")
            cpt+=1

        if y1 >= 400:
            balle[2] = -balle[2]
            canvas.itemconfigure(balle[0],fill="blue")
            cpt+=1
    else:
        balle[1],balle[2]=0,0
       
    

######################
# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# programme principal

canvas.create_line(3,3,LARGEUR,3,width=10,fill="red")
canvas.create_line(3,3,3,HAUTEUR,width=10,fill="yellow")
canvas.create_line(0,HAUTEUR,LARGEUR,HAUTEUR,width=10,fill="blue")
canvas.create_line(LARGEUR,0,LARGEUR,HAUTEUR,width=10,fill="green")


# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()
