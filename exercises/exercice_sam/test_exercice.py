import tkinter as tk

#Constantes
HAUTEUR = 500
LARGEUR = 500

#Variables




#Fonctions




#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("test")

#Widgets
canvas = tk.Canvas(fenetre,width=HAUTEUR,height=LARGEUR,bg="black")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())

canvas.create_rectangle(HAUTEUR/2-50,LARGEUR/2-50,HAUTEUR/2+50,LARGEUR/2+50,fil="red")






#Placement des widgets
canvas.grid()
bouton_quitter.grid()





#lancement de la boucle
fenetre.mainloop()