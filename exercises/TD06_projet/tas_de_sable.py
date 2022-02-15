
###################
##import libraire##
###################


import tkinter as tk


##############
##Constantes##
##############


HAUTEUR = 500
LARGEUR = 500

#######################
##Variables globales###
#######################

Liste=[]


#####################
##Fonctions##########
#####################

def config_aleatoire():
    


    



########################
##Programme principal###
########################


racine =tk.Tk()

racine.title("tas de sable")

canvas = tk.Canvas(racine, bg="black", height=HAUTEUR, width=LARGEUR)
canvas.grid()

bouton1= tk.Button(racine, text="créer la config aléatoire", font = ("helvetica", "30"))
bouton1.grid()






racine.mainloop()


