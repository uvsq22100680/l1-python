
from pickle import TRUE
import tkinter as tk
import random as rd
import sys


#Constantes
HAUTEUR = 600
LARGEUR = 700

#Variables
matrice = []
for i in range(6):
    matrice.append([])
    for j in range(7):
        matrice[i].append(0)
    
couleur = "red"
Alternance = True
nombre_colonne1 = 0
nombre_colonne2 = 0
nombre_colonne3 = 0
nombre_colonne4 = 0
nombre_colonne5 = 0
nombre_colonne6 = 0
nombre_colonne7 = 0
player_rouge = 0
player_jaune = 1
tirage_aleatoire = rd.randint(0,1)
bouton_press=0
gagner = False
arret_du_jeu = 0
Possible = True
liste_id = []


#Fonctions


def aleatoire():
        global couleur,tirage_aleatoire,bouton_press
        if tirage_aleatoire == 0:
                couleur = "red"
                label_info_jouer.config(text="joueur rouge à vous de commencer")
        else :
                couleur ="yellow"
                label_info_jouer.config(text="joueur jaune à vous de commencer")
        bouton_press+=1
        if bouton_press == 1:
                canvas.bind("<Button-1>", afficher)   
        


def afficher(event):

        "blabla"
        global Alternance,couleur,nombre_colonne1,nombre_colonne2,nombre_colonne3,nombre_colonne4,nombre_colonne5,nombre_colonne6,nombre_colonne7,arret_du_jeu,Possible
        if Alternance ==True:
                jouer(event)
                if 0<event.x<LARGEUR//7:
                        nombre_colonne1+=1
                if LARGEUR//7<event.x<LARGEUR//7+100:
                        nombre_colonne2+=1
        
                if LARGEUR//7+100<event.x<LARGEUR//7+200:
                        nombre_colonne3+=1
                if LARGEUR//7+200<event.x<LARGEUR//7+300:
                        nombre_colonne4+=1
                if LARGEUR//7+300<event.x<LARGEUR//7+400:
                        nombre_colonne5+=1
                if LARGEUR//7+400<event.x<LARGEUR//7+500:
                        nombre_colonne6+=1
                if LARGEUR//7+500<event.x<LARGEUR//7+600:
                        nombre_colonne7+=1
                verification_horizontale()
                verification_verticale()
                manche_nulle()
                if Possible == True:
                        Alternance = False
                        if couleur == "red":
                                couleur = "yellow"
                                label_info_jouer.config(text="joueur jaune à vous de jouer")
                        else:        
                                couleur = "red"
                                label_info_jouer.config(text="joueur rouge à vous de jouer")
                else:
                        Alternance = True
                
                
                        
                
                
                
           
        else:
                jouer(event)
                if 0<event.x<LARGEUR//7:
                        nombre_colonne1+=1
                if LARGEUR//7<event.x<LARGEUR//7+100:
                        nombre_colonne2+=1
                if LARGEUR//7+100<event.x<LARGEUR//7+200:
                        nombre_colonne3+=1
                if LARGEUR//7+200<event.x<LARGEUR//7+300:
                        nombre_colonne4+=1
                if LARGEUR//7+300<event.x<LARGEUR//7+400:
                        nombre_colonne5+=1
                if LARGEUR//7+400<event.x<LARGEUR//7+500:
                        nombre_colonne6+=1
                if LARGEUR//7+500<event.x<LARGEUR//7+600:
                        nombre_colonne7+=1
                verification_horizontale()
                verification_verticale()
                manche_nulle()
                if Possible == True:
                        Alternance = True
                        if couleur == "red":
                                couleur = "yellow"
                                label_info_jouer.config(text="joueur jaune à vous de jouer")
                        else:        
                                couleur = "red"
                                label_info_jouer.config(text="joueur rouge à vous de jouer")
                else:
                        Alternance = False
                        

                

                        
                

def jouer(event):

        global nombre_colonne1,nombre_colonne2,nombre_colonne3,nombre_colonne4,nombre_colonne5,nombre_colonne6,nombre_colonne7,Possible,liste_id,id61,id51,id41,id31,id21,id11

        #1er colonne
        if 0<event.x<LARGEUR//7:

                if nombre_colonne1 == 0 :
                        if couleur == "red":
                                matrice[5][0]= 1
                        else:
                                matrice[5][0]= 2
                        id61=canvas.create_oval(0,500,0+rayon,500+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id61)
                
                if nombre_colonne1 == 1:
                        if couleur == "red":
                                matrice[4][0]= 1
                        else:
                                matrice[4][0]= 2
                        id51 =canvas.create_oval(0,400,0+rayon,400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id51)

                if nombre_colonne1 == 2 :
                        if couleur == "red":
                                matrice[3][0]= 1
                        else:
                                matrice[3][0]= 2
                        id41 = canvas.create_oval(0,300,0+rayon,300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id41)
                
                if nombre_colonne1 == 3:
                        if couleur == "red":
                                matrice[2][0]= 1
                        else:
                                matrice[2][0]= 1
                        id31 = canvas.create_oval(0,200,0+rayon,200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id31)
                
                if nombre_colonne1 == 4:
                        if couleur == "red":
                                matrice[1][0]= 1
                        else:
                                matrice[1][0]= 2

                        id21 = canvas.create_oval(0,100,0+rayon,100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id21)

                
                if nombre_colonne1 == 5:
                        if couleur == "red":
                                matrice[0][0]= 1
                        else:
                                matrice[0][0]= 2
                        id11 = canvas.create_oval(0,0,0+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                        liste_id.append(id11)
                
                
                if nombre_colonne1 > 5 :
                        Possible = False
                
                

        #2eme colonne
        if LARGEUR//7<event.x<LARGEUR//7+100:
                

                if nombre_colonne2 == 0 :
                        if couleur == "red":
                                matrice[5][1]= 1
                        else:
                                matrice[5][1]=2
        
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+400,LARGEUR//7+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne2 == 1:
                        if couleur == "red":
                                matrice[4][1]= 1
                        else:
                                matrice[4][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+300,LARGEUR//7+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne2 == 2 :
                        if couleur == "red":
                                matrice[3][1]= 1
                        else:
                                matrice[3][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+200,LARGEUR//7+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne2 == 3:
                        if couleur == "red":
                                matrice[2][1]= 1
                        else:
                                matrice[2][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+100,LARGEUR//7+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne2 == 4:
                        if couleur == "red":
                                matrice[1][1]= 1
                        else:
                                matrice[1][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6,LARGEUR//7+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne2 == 5:
                        if couleur == "red":
                                matrice[0][1]= 1
                        else:
                                matrice[0][1]=2
                        canvas.create_oval(LARGEUR//7,0,LARGEUR//7+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne2 > 5 :
                        Possible = False

        #3eme colonne
        if LARGEUR//7+100<event.x<LARGEUR//7+200:
                

                if nombre_colonne3 == 0 :
                        if couleur == "red":
                                matrice[5][2]= 1
                        else:
                                matrice[5][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+400,LARGEUR//7+100+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne3 == 1:
                        if couleur == "red":
                                matrice[4][2]= 1
                        else:
                                matrice[4][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+300,LARGEUR//7+100+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne3 == 2 :
                        if couleur == "red":
                                matrice[3][2]= 1
                        else:
                                matrice[3][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+200,LARGEUR//7+100+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne3 == 3:
                        if couleur == "red":
                                matrice[2][2]= 1
                        else:
                                matrice[2][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+100,LARGEUR//7+100+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne3 == 4:
                        if couleur == "red":
                                matrice[1][2]= 1
                        else:
                                matrice[1][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6,LARGEUR//7+100+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne3 == 5:
                        if couleur == "red":
                                matrice[0][2]= 1
                        else:
                                matrice[0][2]=2
                        canvas.create_oval(LARGEUR//7+100,0,LARGEUR//7+100+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne3 > 5 :
                        Possible = False
                
        #4ème colonne
        if LARGEUR//7+200<event.x<LARGEUR//7+300:
                

                if nombre_colonne4 == 0 :
                        if couleur == "red":
                                matrice[5][3]= 1
                        else:
                                matrice[5][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+400,LARGEUR//7+200+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne4 == 1:
                        if couleur == "red":
                                matrice[4][3]= 1
                        else:
                                matrice[4][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+300,LARGEUR//7+200+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne4 == 2 :
                        if couleur == "red":
                                matrice[3][3]= 1
                        else:
                                matrice[3][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+200,LARGEUR//7+200+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne4 == 3:
                        if couleur == "red":
                                matrice[2][3]= 1
                        else:
                                matrice[2][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+100,LARGEUR//7+200+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne4 == 4:
                        if couleur == "red":
                                matrice[1][3]= 1
                        else:
                                matrice[1][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6,LARGEUR//7+200+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne4 == 5:
                        if couleur == "red":
                                matrice[0][3]= 1
                        else:
                                matrice[0][3]=2
                        canvas.create_oval(LARGEUR//7+200,0,LARGEUR//7+200+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne4 > 5 :
                        Possible = False
        
        #5ème colonne
        if LARGEUR//7+300<event.x<LARGEUR//7+400:
                

                if nombre_colonne5 == 0 :
                        if couleur == "red":
                                matrice[5][4]= 1
                        else:
                                matrice[5][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+400,LARGEUR//7+300+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne5 == 1:
                        if couleur == "red":
                                matrice[4][4]= 1
                        else:
                                matrice[4][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+300,LARGEUR//7+300+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne5 == 2 :
                        if couleur == "red":
                                matrice[3][4]= 1
                        else:
                                matrice[3][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+200,LARGEUR//7+300+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne5 == 3:
                        if couleur == "red":
                                matrice[2][4]= 1
                        else:
                                matrice[2][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+100,LARGEUR//7+300+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne5 == 4:
                        if couleur == "red":
                                matrice[1][4]= 1
                        else:
                                matrice[1][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6,LARGEUR//7+300+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne5 == 5:
                        if couleur == "red":
                                matrice[0][4]= 1
                        else:
                                matrice[0][4]=2
                        canvas.create_oval(LARGEUR//7+300,0,LARGEUR//7+300+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne5 > 5 :
                        Possible = False
        

        #6ème colonne
        if LARGEUR//7+400<event.x<LARGEUR//7+500:
                

                if nombre_colonne6 == 0 :
                        if couleur == "red":
                                matrice[5][5]= 1
                        else:
                                matrice[5][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+400,LARGEUR//7+400+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne6 == 1:
                        if couleur == "red":
                                matrice[4][5]= 1
                        else:
                                matrice[4][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+300,LARGEUR//7+400+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne6 == 2 :
                        if couleur == "red":
                                matrice[3][5]= 1
                        else:
                                matrice[3][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+200,LARGEUR//7+400+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne6 == 3:
                        if couleur == "red":
                                matrice[2][5]= 1
                        else:
                                matrice[2][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+100,LARGEUR//7+400+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne6 == 4:
                        if couleur == "red":
                                matrice[1][5]= 1
                        else:
                                matrice[1][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6,LARGEUR//7+400+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne6 == 5:
                        if couleur == "red":
                                matrice[0][5]= 1
                        else:
                                matrice[0][5]=2
                        canvas.create_oval(LARGEUR//7+400,0,LARGEUR//7+400+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne6 > 5 :
                        Possible = False
                
        
        #7ème colonne
        if LARGEUR//7+500<event.x<LARGEUR//7+600:
                if nombre_colonne7 == 0 :
                        if couleur == "red":
                                matrice[5][6]= 1
                        else:
                                matrice[5][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+400,LARGEUR//7+500+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne7 == 1:
                        if couleur == "red":
                                matrice[4][6]= 1
                        else:
                                matrice[4][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+300,LARGEUR//7+500+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                if nombre_colonne7 == 2 :
                        if couleur == "red":
                                matrice[3][6]= 1
                        else:
                                matrice[3][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+200,LARGEUR//7+500+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                        Possible = True

                
                if nombre_colonne7 == 3:
                        if couleur == "red":
                                matrice[2][6]= 1
                        else:
                                matrice[2][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+100,LARGEUR//7+500+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne7 == 4:
                        if couleur == "red":
                                matrice[1][6]= 1
                        else:
                                matrice[1][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6,LARGEUR//7+500+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne7 == 5:
                        if couleur == "red":
                                matrice[0][6]= 1
                        else:
                                matrice[0][6]=2
                        canvas.create_oval(LARGEUR//7+500,0,LARGEUR//7+500+rayon,0+rayon,fil=couleur)
                        print(matrice)
                        Possible = True
                
                if nombre_colonne7 > 5 :
                        Possible = False

def verification_horizontale():
        
        for i in range(6):
                global arret_du_jeu
                cpt = 0
                for j in range(6):
                        if matrice[i][j] == matrice[i][j+1] and matrice[i][j+1] != 0 :
                                cpt+=1
                                if cpt == 3:
                                        arret_du_jeu+=1
                                        if couleur == "red" :
                                                label_info_gagner.config(text="La partie est gagnée pour le joueur rouge")
                                        if couleur == "yellow" :
                                                label_info_gagner.config(text="La partie est gagnée pour le joueur jaune")
                        else:
                                cpt=0
                                
                             

def verification_verticale():
        global arret_du_jeu
        for j in range(7):
                cpt = 0
                for i in range(5):
                        if matrice[i][j] == matrice[i+1][j] and matrice[i+1][j] != 0 :
                                cpt+=1
                                if cpt == 3:
                                        arret_du_jeu+=1
                                        if couleur == "red" :
                                                label_info_gagner.config(text="La partie est gagnée pour le joueur rouge")
                                        if couleur == "yellow" :
                                                label_info_gagner.config(text="La partie est gagnée pour le joueur jaune")
                        else:
                                cpt=0




                                
def manche_nulle():
        if sum(matrice[0]) >9:
                label_info_gagner.config(text="La partie est nulle")
        

def retour():
        canvas.delete(liste_id[-1])

def save():
        pass

#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("puissance 4")

#Widgets
canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="blue")

bouton_quitter = tk.Button(fenetre,text="quitter le jeu",command= lambda : fenetre.destroy())
bouton_aleatoire = tk.Button(fenetre,text="Bouton démarrer",command=aleatoire)
bouton_retour = tk.Button(fenetre,text="Bouton revenir en arrière",command=retour)
bouton_save = tk.Button(fenetre,text="Bouton sauvegarder",command=save)

label_info_jouer = tk.Label(fenetre,text= "")
label_info_gagner = tk.Label(fenetre,text= "")

#programme principal
for i in range(0,LARGEUR,LARGEUR//7):
    canvas.create_line(i,0,i,HAUTEUR,width=3,fil="black")
    for j in range(0,HAUTEUR,HAUTEUR//6):
        canvas.create_line(0,j,LARGEUR,j,width=3)
        rayon = 100
        canvas.create_oval(i,j,i+rayon,j+rayon,fil="white")



#Placement des widgets
canvas.grid(row=1,column=0,columnspan=7)
bouton_aleatoire.grid(columnspan=7)
bouton_retour.grid(columnspan=7)
bouton_save.grid(columnspan=7)
bouton_quitter.grid(columnspan=7)
label_info_jouer.grid(columnspan=7)
label_info_gagner.grid(column=0)



#Lancement de la boucle
fenetre.mainloop()
