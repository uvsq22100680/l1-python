
#PROGRAMME BALLE REBONDISANTE

#bibliothèque

import tkinter as tk
import random as rd



#constante
LARGEUR =600
HAUTEUR=400
ALPHA_HORIZONTALE=0
ALPHA_VERTICALE=0
A = 0
#variable
liste_balle=[]


#fonctions

def creer_balle():
    global liste_balle
    identifiant= canvas.create_oval(LARGEUR/2,HAUTEUR/2,LARGEUR/2+20,HAUTEUR/2+20,fil="black")
    liste_balle.append(identifiant)
    liste_balle.append(rd.randint(1,8))
    liste_balle.append(rd.randint(1,8))
    print(liste_balle)


def mouvement_balle():
    global ALPHA_VERTICALE,ALPHA_HORIZONTALE
    
    if  A == 0 :
        ALPHA_HORIZONTALE += liste_balle[1]
        ALPHA_VERTICALE += liste_balle[2]
        canvas.coords(balle,LARGEUR/2+ALPHA_HORIZONTALE,HAUTEUR/2+ALPHA_VERTICALE,LARGEUR/2+20+ALPHA_HORIZONTALE,HAUTEUR/2+20+ALPHA_VERTICALE)
        rebond1()
    canvas.after(5,mouvement_balle)
        
    if bouton_demarrer["text"]=="arreter":
         canvas.after_cancel(mouvement_balle)
         bouton_demarrer["text"]="démarrer"
    bouton_demarrer["text"]="arreter"
    
    

def rebond1():
    if canvas.coords(balle)[3]>HAUTEUR or canvas.coords(balle)[3]<0:
            liste_balle[2] =  -1 * liste_balle[2]
    if canvas.coords(balle)[2]>LARGEUR or canvas.coords(balle)[2]<0:
            liste_balle[1] =  -1 * liste_balle[1]
    
def rebond2(balle):
    pass


#programme principal


fenetre = tk.Tk()

fenetre.title("deplacement balle")


#widgets
canvas = tk.Canvas(fenetre, width=LARGEUR, height=HAUTEUR,bg = "black")
bouton_demarrer = tk.Button(fenetre, text = "démarrer", font=("helvetica","20"),command=mouvement_balle)
bouton_quitter =tk.Button(fenetre,text="quiiter",font=("helvetica","20"),command= lambda : fenetre.destroy())



#widgets placements
bouton_demarrer.grid()
bouton_quitter.grid()
canvas.grid()





balle= canvas.create_oval(LARGEUR/2,HAUTEUR/2,LARGEUR/2+20,HAUTEUR/2+20,fil="blue")




                                       

creer_balle()







#Lancement de la boucle

fenetre.mainloop()

