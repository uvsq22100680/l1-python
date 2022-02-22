#######
##SAM##
#######


#########
#import librairies
import tkinter as tk
import random as rd

#########
#def des constantes

#hauteur du canevas
HAUTEUR = 600

#largeur du canvenas
LARGEUR = 600

#taille de la liste
N = 4 


P =0,5

couleur_mur="grey"
couleur_vide="white"

terrain=[]
grille=[]

#########
#Fonctions
def init_terrain():
    """initialise le terrain de la manière suivante:
    "met à 0 la liste à 2D apppelée terrain qui cintient pour chaque case la valeur
    1 si il y a un mur et 0 sinon
    "initilise la liste grille 2D qui contient l'identifiant du carre
    dessiné sur le cannevas pour chaque case
    """

    global terrain, grille

    for i in range(N):
        terrain.append([0]*N)
        grille.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0,1) < P :
                terrain[i][j] = 1
                couleur = couleur_mur
            else:
                couleur = couleur_vide
                largeur = LARGEUR//N
                hauteur= HAUTEUR//N
                x0,y0 = i * largeur, j * hauteur
                x1,y1 = (i+1)*largeur, (j+1)*hauteur
                canvas.create_rectangle((x0,y0),(x1,y1),fill=couleur)
            

    print(terrain)
    







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
