
###################
##import libraire##
###################


import tkinter as tk


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


#####################
##Fonctions##########
#####################

def init_terrain():
    """Initialiser le terrain:
    * initialiser la liste carrée terrain à 2D de taille N telle
    que la case de coordonnées (i,j) vaut 1 si il y a un mur
    dessus et 0 sinon
    * initialiser la liste carrée grille à 2D de taille N
    telle que la case de coordonnées (i,j) contient l'identifiant
    du carré dessiné sur le canevas 
    * Une case est un mur avec probabilité P
    """
    grille = []
    for i in range(N):
        grille.append([0]*N)
        
        
    canvas.create_text(250,250,text=grille,fill="white")
    


    



########################
##Programme principal###
########################


racine =tk.Tk()

racine.title("tas de sable")

canvas = tk.Canvas(racine, bg="black", height=HAUTEUR, width=LARGEUR)
canvas.grid()

bouton1= tk.Button(racine, text="créer la config aléatoire", font = ("helvetica", "30"),command=init_terrain)
bouton1.grid()



init_terrain()

racine.mainloop()


