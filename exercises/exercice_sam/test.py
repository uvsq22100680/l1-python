import tkinter as tk
import random as rd

#Constantes
HAUTEUR = 400
LARGEUR = 400

#Variables


carre = 100

#Fonctions




#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("taquin")

#Widgets
canvas = tk.Canvas(fenetre,width=HAUTEUR,height=LARGEUR,bg="black")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())


liste_aleatoire = [i for i in range(16)]



for i in range(4):
        for j in range(4):
                choix_au_hasard = rd.choice(liste_aleatoire)
                liste_aleatoire.remove(choix_au_hasard)
                canvas.create_rectangle(i*carre+2,j*carre+2,i*carre+carre-2,j*carre+carre-2,fill = "blue")
                canvas.create_text(i*carre+carre//2,j*carre-carre//2-2,text =choix_au_hasard ,fill = "yellow",font = ("helvetica","25"))





#Placement des widgets
canvas.grid()
bouton_quitter.grid()





#Lancement de la boucle
fenetre.mainloop()