
#PROGRAMME BALLE REBONDISANTE

#bibliothèque

import tkinter as tk
import random as rd



#constante
LARGEUR =600
HAUTEUR=400

#variable
liste_balle=[]
variable =-1
x0 =LARGEUR/2
y0 =HAUTEUR/2
x1 =LARGEUR/2+20
y1 = HAUTEUR/2+20


#fonctions

def creer_balle():
    global liste_balle
    identifiant= canvas.create_oval(LARGEUR/2,HAUTEUR/2,LARGEUR/2+20,HAUTEUR/2+20,fil="blue")
    liste_balle.append(identifiant)
    liste_balle.append(rd.randint(1,8))
    liste_balle.append(rd.randint(1,8))
    print(liste_balle)


def mouvement_balle():
    global x1,x0,y1,y0,variable
    while  variable != 10:
        x0 +=10
        x1 += 10
        y0 +=10
        y1 +=10
        canvas.coords(balle,x0,y0,x1,y1)
        variable +=10


    

def rebond1(balle):
    pass



def rebond2(balle):
    pass


#programme principal


fenetre = tk.Tk()

fenetre.title("deplacement balle")


#widgets
canvas = tk.Canvas(fenetre, width=LARGEUR, height=HAUTEUR,bg = "black")
bouton_demarrer = tk.Button(fenetre, text = "mt_balle", font=("helvetica","20"),command=mouvement_balle)
bouton_quitter =tk.Button(fenetre,text="quiiter",font=("helvetica","20"),command= lambda : fenetre.destroy())



#widgets placements
bouton_demarrer.grid()
bouton_quitter.grid()
canvas.grid()


balle= canvas.create_oval(x0,y0,x1,y1,fil="blue")




                                       









#Lancement de la boucle

fenetre.mainloop()

