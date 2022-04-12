
import tkinter as tk

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
nombre = 0
nombre_colonne1 = 0
nombre_colonne2 = 0
nombre_colonne3 = 0
nombre_colonne4 = 0
nombre_colonne5 = 0
nombre_colonne6 = 0
nombre_colonne7 = 0


#Fonctions

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
        couleur="yellow"
        label_info.config(text="joueur jaune à vous de jouer")
        
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
        couleur="red"
        label_info.config(text="joueur rouge à vous de jouer")


#1ER COLONNE

def jouer(event):

        global nombre_colonne1,nombre_colonne2,nombre_colonne3,nombre_colonne4,nombre_colonne5,nombre_colonne6,nombre_colonne7

        #1er colonne
        if 0<event.x<LARGEUR//7:

                if nombre_colonne1 == 0 :
                        matrice[5][0]= 1
                        canvas.create_oval(0,500,0+rayon,500+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne1 == 1:
                        matrice[4][0]= 1
                        canvas.create_oval(0,400,0+rayon,400+rayon,fil=couleur)
                        
                        print(matrice)

                if nombre_colonne1 == 2 :
                        matrice[3][0]= 1
                        canvas.create_oval(0,300,0+rayon,300+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne1 == 3:
                        matrice[2][0]= 1
                        canvas.create_oval(0,200,0+rayon,200+rayon,fil=couleur)
                
                if nombre_colonne1 == 4:
                        matrice[1][0]= 1
                        canvas.create_oval(0,100,0+rayon,100+rayon,fil=couleur)

                
                if nombre_colonne1 == 5:
                        matrice[0][0]= 1
                        canvas.create_oval(0,0,0+rayon,0+rayon,fil=couleur)

        #2eme colonne
        if LARGEUR//7<event.x<LARGEUR//7+100:
                

                if nombre_colonne2 == 0 :
                        matrice[5][1]= 1
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+400,LARGEUR//7+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne2 == 1:
                        matrice[4][1]= 1
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+300,LARGEUR//7+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        
                        print(matrice)

                if nombre_colonne2 == 2 :
                        matrice[3][1]= 1
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+200,LARGEUR//7+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne2 == 3:
                        matrice[2][1]= 1
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6+100,LARGEUR//7+rayon,HAUTEUR//6+100+rayon,fil=couleur)

                
                if nombre_colonne2 == 4:
                        matrice[1][1]= 1
                        canvas.create_oval(LARGEUR//7,HAUTEUR//6,LARGEUR//7+rayon,HAUTEUR//6+rayon,fil=couleur)

                
                if nombre_colonne2 == 5:
                        matrice[0][1]= 1
                        canvas.create_oval(LARGEUR//7,0,LARGEUR//7+rayon,0+rayon,fil=couleur)

        #3eme colonne
        if LARGEUR//7+100<event.x<LARGEUR//7+200:
                

                if nombre_colonne3 == 0 :
                        matrice[5][2]= 1
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+400,LARGEUR//7+100+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne3 == 1:
                        matrice[4][2]= 1
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+300,LARGEUR//7+100+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        
                        print(matrice)

                if nombre_colonne3 == 2 :
                        matrice[3][2]= 1
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+200,LARGEUR//7+100+rayon,HAUTEUR//6+200+rayon,fil=couleur)
                        print(matrice)
                
                if nombre_colonne3 == 3:
                        matrice[2][2]= 1
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6+100,LARGEUR//7+100+rayon,HAUTEUR//6+100+rayon,fil=couleur)

                
                if nombre_colonne3 == 4:
                        matrice[1][2]= 1
                        canvas.create_oval(LARGEUR//7+100,HAUTEUR//6,LARGEUR//7+100+rayon,HAUTEUR//6+rayon,fil=couleur)

                
                if nombre_colonne3 == 5:
                        matrice[0][2]= 1
                        canvas.create_oval(LARGEUR//7+100,0,LARGEUR//7+100+rayon,0+rayon,fil=couleur)
                
        #4ème colonne
        if LARGEUR//7+200<event.x<LARGEUR//7+300:
                

                if nombre_colonne4 == 0 :
                        matrice[5][2]= 1
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+400,LARGEUR//7+200+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne4 == 1:
                        matrice[4][2]= 1
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+300,LARGEUR//7+200+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne4 == 2 :
                        matrice[3][2]= 1
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+200,LARGEUR//7+200+rayon,HAUTEUR//6+200+rayon,fil=couleur)

                
                if nombre_colonne4 == 3:
                        matrice[2][2]= 1
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6+100,LARGEUR//7+200+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                
                if nombre_colonne4 == 4:
                        matrice[1][2]= 1
                        canvas.create_oval(LARGEUR//7+200,HAUTEUR//6,LARGEUR//7+200+rayon,HAUTEUR//6+rayon,fil=couleur)
                
                if nombre_colonne4 == 5:
                        matrice[0][2]= 1
                        canvas.create_oval(LARGEUR//7+200,0,LARGEUR//7+200+rayon,0+rayon,fil=couleur)
        
        #5ème colonne
        if LARGEUR//7+300<event.x<LARGEUR//7+400:
                

                if nombre_colonne5 == 0 :
                        matrice[5][2]= 1
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+400,LARGEUR//7+300+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne5 == 1:
                        matrice[4][2]= 1
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+300,LARGEUR//7+300+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne5 == 2 :
                        matrice[3][2]= 1
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+200,LARGEUR//7+300+rayon,HAUTEUR//6+200+rayon,fil=couleur)

                
                if nombre_colonne5 == 3:
                        matrice[2][2]= 1
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6+100,LARGEUR//7+300+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                
                if nombre_colonne5 == 4:
                        matrice[1][2]= 1
                        canvas.create_oval(LARGEUR//7+300,HAUTEUR//6,LARGEUR//7+300+rayon,HAUTEUR//6+rayon,fil=couleur)
                
                if nombre_colonne5 == 5:
                        matrice[0][2]= 1
                        canvas.create_oval(LARGEUR//7+300,0,LARGEUR//7+300+rayon,0+rayon,fil=couleur)
        

        #6ème colonne
        if LARGEUR//7+400<event.x<LARGEUR//7+500:
                

                if nombre_colonne6 == 0 :
                        matrice[5][2]= 1
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+400,LARGEUR//7+400+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne6 == 1:
                        matrice[4][2]= 1
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+300,LARGEUR//7+400+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne6 == 2 :
                        matrice[3][2]= 1
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+200,LARGEUR//7+400+rayon,HAUTEUR//6+200+rayon,fil=couleur)

                
                if nombre_colonne6 == 3:
                        matrice[2][2]= 1
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6+100,LARGEUR//7+400+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                
                if nombre_colonne6 == 4:
                        matrice[1][2]= 1
                        canvas.create_oval(LARGEUR//7+400,HAUTEUR//6,LARGEUR//7+400+rayon,HAUTEUR//6+rayon,fil=couleur)
                
                if nombre_colonne6 == 5:
                        matrice[0][2]= 1
                        canvas.create_oval(LARGEUR//7+400,0,LARGEUR//7+400+rayon,0+rayon,fil=couleur)
                
        
        #7ème colonne
        if LARGEUR//7+500<event.x<LARGEUR//7+600:
                if nombre_colonne7 == 0 :
                        matrice[5][2]= 1
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+400,LARGEUR//7+500+rayon,HAUTEUR//6+400+rayon,fil=couleur)
                        
                        print(matrice)
                
                if nombre_colonne7 == 1:
                        matrice[4][2]= 1
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+300,LARGEUR//7+500+rayon,HAUTEUR//6+300+rayon,fil=couleur)
                        print(matrice)

                if nombre_colonne7 == 2 :
                        matrice[3][2]= 1
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+200,LARGEUR//7+500+rayon,HAUTEUR//6+200+rayon,fil=couleur)

                
                if nombre_colonne7 == 3:
                        matrice[2][2]= 1
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6+100,LARGEUR//7+500+rayon,HAUTEUR//6+100+rayon,fil=couleur)
                
                if nombre_colonne7 == 4:
                        matrice[1][2]= 1
                        canvas.create_oval(LARGEUR//7+500,HAUTEUR//6,LARGEUR//7+500+rayon,HAUTEUR//6+rayon,fil=couleur)
                
                if nombre_colonne7 == 5:
                        matrice[0][2]= 1
                        canvas.create_oval(LARGEUR//7+500,0,LARGEUR//7+500+rayon,0+rayon,fil=couleur)
                                        
                        
                                        
                        
    
                                        
                        
    
    
    
    
    

def choix_couleur():

    for i in range(0,LARGEUR,LARGEUR//7):
        for j in range(0,HAUTEUR,HAUTEUR//6):
                canvas.create_oval(fenetre,i,j,i+rayon,j+rayon,fil="white")
              

       
    


#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("puissance 4")

#Widgets
canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="blue")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())
label_info = tk.Label(fenetre,text= "joueur_rouge à vous de commencer")




for i in range(0,LARGEUR,LARGEUR//7):
    canvas.create_line(i,0,i,HAUTEUR,width=3,fil="black")
    for j in range(0,HAUTEUR,HAUTEUR//6):
        canvas.create_line(0,j,LARGEUR,j,width=3)
        rayon = 100
        canvas.create_oval(i,j,i+rayon,j+rayon,fil="white")
    





#Placement des widgets


canvas.grid(row=1,column=0,columnspan=7)
bouton_quitter.grid(columnspan=7)



label_info.grid(columnspan=7)

canvas.bind("<Button-1>", afficher)




#Lancement de la boucle
fenetre.mainloop()