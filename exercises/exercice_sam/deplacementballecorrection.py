import tkinter as tk
import random as rd

#Constantes
HAUTEUR = 500
LARGEUR = 500

#Variables

est_arrete = True


#Fonctions

def demarrer():
    "blabla"
    global est_arrete
    if est_arrete:
        mouvement_balle()
        bouton_demarrer.config(text="arreter")
    else:
        canvas.after_cancel(id_after)
        bouton_demarrer.config(text="démarrer")
        
    est_arrete = not est_arrete



def creer_balle():
    "blabla"
    r = 20
    xmil = LARGEUR // 2
    ymil = HAUTEUR // 2
    cercle = canvas.create_oval(xmil-r,ymil-r,xmil+r,ymil+r,fill = "red")
    dx = rd.randint(1,7)
    dy = rd.randint(1,7)
    return [cercle,dx,dy]

def mouvement_balle():
    "blabla"
    global id_after
    canvas.move(balle[0],balle[1],balle[2])
    id_after = canvas.after(20,mouvement_balle)

def rebond1():
    "blabla"
    x0,y0,x1,y1 = canvas.coords(balle[0])
    if y1 > HAUTEUR or y1 <0:
        balle[2] = -1 *balle[2]
    
    if x1 > HAUTEUR or x1<0:
        balle[1] = -1 *balle[1]

def rebond2():
    pass




#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("test")

#Widgets
canvas = tk.Canvas(fenetre,width=HAUTEUR,height=LARGEUR,bg="black")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())
bouton_demarrer = tk.Button(fenetre,text="démarrer",command=demarrer)


balle = creer_balle()





#Placement des widgets
canvas.grid()
bouton_quitter.grid()
bouton_demarrer.grid()





#Lancement de la boucle
fenetre.mainloop()