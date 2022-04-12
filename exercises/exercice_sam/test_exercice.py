
import tkinter as tk
import random as rd


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
        global Alternance,couleur,nombre_colonne1,nombre_colonne2,nombre_colonne3,nombre_colonne4,nombre_colonne5,nombre_colonne6,nombre_colonne7
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
        
            Alternance = False
            if couleur == "red":
                couleur = "yellow"
                label_info_jouer.config(text="joueur jaune à vous de jouer")
            else:
                 couleur = "red"
                 label_info_jouer.config(text="joueur rouge à vous de jouer")  
           
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
            Alternance =True
            if couleur == "red":
                couleur = "yellow"
                label_info_jouer.config(text="joueur jaune à vous de jouer")
            else:
                 couleur = "red"
                 label_info_jouer.config(text="joueur rouge à vous de jouer")  

def jouer(event):

        global nombre_colonne1,nombre_colonne2,nombre_colonne3,nombre_colonne4,nombre_colonne5,nombre_colonne6,nombre_colonne7

        #1er colonne
        if 0<event.x<LARGEUR//7:

                if nombre_colonne1 == 0 :
                        if couleur == "red":
                                matrice[5][0]= 1
                        else:
                                matrice[5][0]= 2
                        canvas.create_oval(0,500,0+rayon,500+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne1 == 1:
                        if couleur == "red":
                                matrice[4][0]= 1
                        else:
                                matrice[4][0]= 2
                        canvas.create_oval(0,400,0+rayon,400+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne1 == 2 :
                        if couleur == "red":
                                matrice[3][0]= 1
                        else:
                                matrice[3][0]= 2
                        canvas.create_oval(0,300,0+rayon,300+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne1 == 3:
                        if couleur == "red":
                                matrice[2][0]= 1
                        else:
                                matrice[2][0]= 1
                        canvas.create_oval(0,200,0+rayon,200+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne1 == 4:
                        if couleur == "red":
                                matrice[1][0]= 1
                        else:
                                matrice[1][0]= 2

                        canvas.create_oval(0,100,0+rayon,100+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne1 == 5:
                        if couleur == "red":
                                matrice[0][0]= 1
                        else:
                                matrice[0][0]= 2
                        canvas.create_oval(0,0,0+rayon,0+rayon,fil=couleur)
                        print(matrice)
                
                

        #2eme colonne
        if LARGEUR//7<event.x<LARGEUR//7+100:
                

                if nombre_colonne2 == 0 :
                        if couleur == "red":
                                matrice[5][1]= 1
                        else:
                                matrice[5][1]=2
        
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+400,LARGEUR//7+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne2 == 1:
                        if couleur == "red":
                                matrice[4][1]= 1
                        else:
                                matrice[4][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+300,LARGEUR//7+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne2 == 2 :
                        if couleur == "red":
                                matrice[3][1]= 1
                        else:
                                matrice[3][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+200,LARGEUR//7+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne2 == 3:
                        if couleur == "red":
                                matrice[2][1]= 1
                        else:
                                matrice[2][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+100,LARGEUR//7+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne2 == 4:
                        if couleur == "red":
                                matrice[1][1]= 1
                        else:
                                matrice[1][1]=2
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6,LARGEUR//7+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne2 == 5:
                        if couleur == "red":
                                matrice[0][1]= 1
                        else:
                                matrice[0][1]=2
                        canvas.create_oval(LARGEUR//7,0,LARGEUR//7+rayon,0+rayon,fil=couleur)
                        print(matrice)

        #3eme colonne
        if LARGEUR//7+100<event.x<LARGEUR//7+200:
                

                if nombre_colonne3 == 0 :
                        if couleur == "red":
                                matrice[5][2]= 1
                        else:
                                matrice[5][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+400,LARGEUR//7+100+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne3 == 1:
                        if couleur == "red":
                                matrice[4][2]= 1
                        else:
                                matrice[4][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+300,LARGEUR//7+100+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne3 == 2 :
                        if couleur == "red":
                                matrice[3][2]= 1
                        else:
                                matrice[3][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+200,LARGEUR//7+100+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne3 == 3:
                        if couleur == "red":
                                matrice[2][2]= 1
                        else:
                                matrice[2][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+100,LARGEUR//7+100+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne3 == 4:
                        if couleur == "red":
                                matrice[1][2]= 1
                        else:
                                matrice[1][2]=2
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6,LARGEUR//7+100+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne3 == 5:
                        if couleur == "red":
                                matrice[0][2]= 1
                        else:
                                matrice[0][2]=2
                        canvas.create_oval(LARGEUR//7+100,0,LARGEUR//7+100+rayon,0+rayon,fil=couleur)
                        print(matrice)
                
        #4ème colonne
        if LARGEUR//7+200<event.x<LARGEUR//7+300:
                

                if nombre_colonne4 == 0 :
                        if couleur == "red":
                                matrice[5][3]= 1
                        else:
                                matrice[5][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+400,LARGEUR//7+200+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne4 == 1:
                        if couleur == "red":
                                matrice[4][3]= 1
                        else:
                                matrice[4][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+300,LARGEUR//7+200+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne4 == 2 :
                        if couleur == "red":
                                matrice[3][3]= 1
                        else:
                                matrice[3][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+200,LARGEUR//7+200+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne4 == 3:
                        if couleur == "red":
                                matrice[2][3]= 1
                        else:
                                matrice[2][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+100,LARGEUR//7+200+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne4 == 4:
                        if couleur == "red":
                                matrice[1][3]= 1
                        else:
                                matrice[1][3]=2
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6,LARGEUR//7+200+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne4 == 5:
                        if couleur == "red":
                                matrice[0][3]= 1
                        else:
                                matrice[0][3]=2
                        canvas.create_oval(LARGEUR//7+200,0,LARGEUR//7+200+rayon,0+rayon,fil=couleur)
                        print(matrice)
        
        #5ème colonne
        if LARGEUR//7+300<event.x<LARGEUR//7+400:
                

                if nombre_colonne5 == 0 :
                        if couleur == "red":
                                matrice[5][4]= 1
                        else:
                                matrice[5][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+400,LARGEUR//7+300+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne5 == 1:
                        if couleur == "red":
                                matrice[4][4]= 1
                        else:
                                matrice[4][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+300,LARGEUR//7+300+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne5 == 2 :
                        if couleur == "red":
                                matrice[3][4]= 1
                        else:
                                matrice[3][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+200,LARGEUR//7+300+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne5 == 3:
                        if couleur == "red":
                                matrice[2][4]= 1
                        else:
                                matrice[2][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+100,LARGEUR//7+300+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne5 == 4:
                        if couleur == "red":
                                matrice[1][4]= 1
                        else:
                                matrice[1][4]=2
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6,LARGEUR//7+300+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne5 == 5:
                        if couleur == "red":
                                matrice[0][4]= 1
                        else:
                                matrice[0][4]=2
                        canvas.create_oval(LARGEUR//7+300,0,LARGEUR//7+300+rayon,0+rayon,fil=couleur)
                        print(matrice)
        

        #6ème colonne
        if LARGEUR//7+400<event.x<LARGEUR//7+500:
                

                if nombre_colonne6 == 0 :
                        if couleur == "red":
                                matrice[5][5]= 1
                        else:
                                matrice[5][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+400,LARGEUR//7+400+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne6 == 1:
                        if couleur == "red":
                                matrice[4][5]= 1
                        else:
                                matrice[4][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+300,LARGEUR//7+400+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne6 == 2 :
                        if couleur == "red":
                                matrice[3][5]= 1
                        else:
                                matrice[3][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+200,LARGEUR//7+400+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne6 == 3:
                        if couleur == "red":
                                matrice[2][5]= 1
                        else:
                                matrice[2][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+100,LARGEUR//7+400+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne6 == 4:
                        if couleur == "red":
                                matrice[1][5]= 1
                        else:
                                matrice[1][5]=2
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6,LARGEUR//7+400+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne6 == 5:
                        if couleur == "red":
                                matrice[0][5]= 1
                        else:
                                matrice[0][5]=2
                        canvas.create_oval(LARGEUR//7+400,0,LARGEUR//7+400+rayon,0+rayon,fil=couleur)
                        print(matrice)
                
        
        #7ème colonne
        if LARGEUR//7+500<event.x<LARGEUR//7+600:
                if nombre_colonne7 == 0 :
                        if couleur == "red":
                                matrice[5][6]= 1
                        else:
                                matrice[5][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+400,LARGEUR//7+500+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne7 == 1:
                        if couleur == "red":
                                matrice[4][6]= 1
                        else:
                                matrice[4][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+300,LARGEUR//7+500+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne7 == 2 :
                        if couleur == "red":
                                matrice[3][6]= 1
                        else:
                                matrice[3][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+200,LARGEUR//7+500+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)

                
                if nombre_colonne7 == 3:
                        if couleur == "red":
                                matrice[2][6]= 1
                        else:
                                matrice[2][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+100,LARGEUR//7+500+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne7 == 4:
                        if couleur == "red":
                                matrice[1][6]= 1
                        else:
                                matrice[1][6]=2
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6,LARGEUR//7+500+rayon,HAUTEUR//6+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne7 == 5:
                        if couleur == "red":
                                matrice[0][6]= 1
                        else:
                                matrice[0][6]=2
                        canvas.create_oval(LARGEUR//7+500,0,LARGEUR//7+500+rayon,0+rayon,fil=couleur)
                        print(matrice)

def verification():
        pass
                                





#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("puissance 4")

#Widgets
canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="blue")

bouton_quitter = tk.Button(fenetre,text="quitter le jeu",command= lambda : fenetre.destroy())
bouton_aleatoire = tk.Button(fenetre,text="Bouton démarrer",command=aleatoire)

label_info_jouer = tk.Label(fenetre,text= "")
label_info_gagner = tk.Label(fenetre,text= "Le joeur qui gagne la partie est :")

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
bouton_quitter.grid(columnspan=7)
label_info_jouer.grid(columnspan=7)
label_info_gagner.grid(column=0)



#Lancement de la boucle
fenetre.mainloop()
