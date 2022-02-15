
###################
##import libraire##
###################


import tkinter as tk
import random as rd


##############
##Constantes##
##############


HAUTEUR = 500
LARGEUR = 500
N = 3


#######################
##Variables globales###
#######################

Liste=[]
GRILLE = []

#####################
##Fonctions##########
#####################

def carre_canvas(x,y,rayon=5,couleur='blue'):
    liste_canvas = canvas.create_rectangle(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur)

def generation():
    canvas.delete('all')
    config_courante = []
    for i in range(GRILLE):
        config_courante.append([])
        for j in range(GRILLE):
            config_courante[i].append(rd.randint(0,9))
    espacement = HAUTEUR / GRILLE
    for x in range(GRILLE):
        for y in range(GRILLE):
            if config_courante[x][y] < 4:
                carre_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement)
            else:
                carre_canvas(espacement / 2 + x * espacement, espacement / 2 + y*espacement,couleur='red')


########################
##Programme principal###
########################


racine =tk.Tk()

racine.title("tas de sable")

canvas = tk.Canvas(racine, bg="black", height=HAUTEUR, width=LARGEUR)
canvas.grid()

bouton1= tk.Button(racine, text="créer la config aléatoire", font = ("helvetica", "30"),command=generation)
bouton1.grid()




racine.mainloop()


