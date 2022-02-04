#######
##SAM##
#######


#########
#import librairies
import tkinter as tk

#########
#def des constantes

#hauteur du canevas
HAUTEUR = 600

#largeur du canvenas
LARGEUR = 600

#########
#Fonctions
def init_terrain():
    """initialise le terrain de la manière suivante:
    "met à 0 la liste à 2D qui cintient pour chaque case la valeur
    1 si il y a un mur et 0 sinon
    "initilise la liste grille 2D qui contient l'identifiant du carre
    dessiné sur le cannevas pour chaque case
    """
    
    pass




#########
#prgramme principal


#Def des widgets
racine = tk.Tk()
racine.title("generation de terrain")
canvas = tk.Canvas(racine, width =LARGEUR, height =HAUTEUR,bg= "red")

#placements des widgets

canvas.grid(column = 0, row = 0)

#boucle principal

racine.mainloop()
