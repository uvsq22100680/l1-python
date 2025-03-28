
#############################################
# groupe 1
# Ilerioluwa OLAYODE
# Aymeric GOUDOUT
# Sam BARBOSA
# https://github.com/ilrx/Projet_tas_de_sable
#############################################

######################
#Import des librairies
######################

import tkinter as tk
import random as rd

##########################
#Définition des constantes
##########################

HAUTEUR = 800
LARGEUR = 800
GRILLE = 10

##################################
#Définition des variables globales
##################################

liste_canvas = []
config_courante = []

#########################
#Définition des fonctions
#########################

def carre_canvas(x,y,rayon=5,couleur='blue'):
    liste_canvas = canvas.create_rectangle(x-rayon,y-rayon,x+rayon,y+rayon,fill=couleur)

def generation():
    global config_courante
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
    



def programmerlecalculd():
    global config_courante
    for i in range(config_courante):
        for j in range(config_courante):
            config_courante[i].append(3)
   
   




####################
#Programme principal
####################

root = tk.Tk()
root.title('Tas de Sable - Groupe 1')
canvas = tk.Canvas(root,height=HAUTEUR,width=LARGEUR,bg='black')
button_generation = tk.Button(root,text='Génération',command=generation,activebackground='red')
button_ajoutgrain= tk.Button(root,text ="rajout grain", command=programmerlecalculd)

button_ajoutgrain.grid(row=0,column=2)
button_generation.grid(row=0,column=0)
canvas.grid(row=0,column=1)




root.mainloop()