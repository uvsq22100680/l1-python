import tkinter as tk

from matplotlib.pyplot import new_figure_manager

#Constantes
HAUTEUR = 500
LARGEUR = 500
liste_identifiant = []
#Variables




#Fonctions
def affichage():
    global liste_identifiant
    for i in range(10):
        for j in range(11):
            canvas.create_line(i*100,j*100,i*100,j*100+50,width=3,fill="black")
            canvas.create_line(i*100,j*100,i*100+50,j*100,width=3,fill="black")
            liste_identifiant.append(canvas.create_rectangle(i*50,j*50,i*50+50,j*50+50,fill = "green"))
            





#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Mastermind")

#Widgets
canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="white")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())
bouton_afficher = tk.Button(fenetre,text="Affichage",command= affichage)







#Placement des widgets

bouton_quitter.grid(row = 0,column=1)
bouton_afficher.grid(row=0,column=2)
canvas.grid(row = 1,column=0,columnspan=8)





#Lancement de la boucle
fenetre.mainloop()