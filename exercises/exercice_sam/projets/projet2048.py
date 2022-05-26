import tkinter as tk
import random as rd

#Constantes
HAUTEUR = 400
LARGEUR = 400

#Variables
matrice_jeu = []
for i in range(4) :
    matrice_jeu.append([])
    for j in range(4):
        matrice_jeu[i].append(0)
print(matrice_jeu)

nombre = 0



#Fonctions
def Affichage():
    global liste_identifiant
    liste_identifiant = []
    for i in range(4):
            for j in range(4):
                canvas.create_line(i*100,j*100,i*100,j*100+100,width=3,fill="black")
                canvas.create_line(i*100,j*100,i*100+100,j*100,width=3,fill="black")
                liste_identifiant.append([canvas.create_rectangle(i*100,j*100,i*100+100,j*100+100,fill="red"),canvas.create_text(i*100+50,j*100+50,text  = nombre,width=3, fill = "black")])
    print(liste_identifiant)
    
    i = rd.randint(0,16)
    j = rd.randint(0,16)
    if i == j and i < 16:
        j += 1
    elif i == j and i == 1:
        j +=1
    canvas.itemconfigure(liste_identifiant[i][1], text = 2)
    canvas.itemconfigure(liste_identifiant[j][1], text = 2)
    
  
    

def jeu(event):
   pass
   


#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("2048")

#Widgets
canvas = tk.Canvas(fenetre, width=HAUTEUR, height=LARGEUR, bg= "white")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())
bouton_jouer = tk.Button(fenetre,text="jeu",command= Affichage)








#Placement des widgets
canvas.grid()
bouton_quitter.grid()
bouton_jouer.grid()




canvas.bind("<Button-1>", jeu)
#Lancement de la boucle
fenetre.mainloop()