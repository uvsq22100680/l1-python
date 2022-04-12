
import tkinter as tk

#Constantes
HAUTEUR = 600
LARGEUR = 600

#Variables

Alternance = True


#Fonctions

def afficher(event):
    "blabla"
    global Alternance
    if Alternance ==True:
        croix(event)
        Alternance = False
        label_cercle.config(text="joueur cercle à vous de jouer")
        label_croix.config(text="ne joue pas")
    else:
        cercle(event)
        Alternance =True
        label_croix.config(text="joueur croix à vous de jouer")
        label_cercle.config(text="ne joue pas")


def croix(event):
    #1ERCoLoNNE
    if  0<event.x <LARGEUR//3 and 0<event.y<HAUTEUR//3:
        canvas.create_line(0,0,LARGEUR//3,HAUTEUR//3)
        canvas.create_line(0,HAUTEUR//3,LARGEUR//3,0)

    if  0<event.x <LARGEUR//3 and HAUTEUR//3<event.y<HAUTEUR//3 +(HAUTEUR//3):
        canvas.create_line(0,HAUTEUR//3,LARGEUR//3,HAUTEUR//3+(HAUTEUR//3))#### à modifier
        canvas.create_line(0,HAUTEUR//3+(HAUTEUR//3),LARGEUR//3,HAUTEUR//3)
    
    if  0<event.x <LARGEUR//3 and HAUTEUR//3 +(HAUTEUR//3)<event.y<HAUTEUR:
        canvas.create_line(0,HAUTEUR//3 +(HAUTEUR//3),LARGEUR//3,HAUTEUR)
        canvas.create_line(0,HAUTEUR,LARGEUR//3,HAUTEUR//3+(HAUTEUR//3))

#2EME COLONNE
    if  LARGEUR//3<event.x <LARGEUR//3+(LARGEUR//3) and 0<event.y<HAUTEUR//3:
        canvas.create_line(LARGEUR//3,0,LARGEUR//3+LARGEUR//3,HAUTEUR//3)
        canvas.create_line(LARGEUR//3,HAUTEUR//3,LARGEUR//3+LARGEUR//3,0)

    if  LARGEUR//3<event.x <LARGEUR//3+(LARGEUR//3) and HAUTEUR//3<event.y<HAUTEUR//3+HAUTEUR//3:
        canvas.create_line(LARGEUR//3,HAUTEUR//3,LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3)
        canvas.create_line(LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR//3+LARGEUR//3,HAUTEUR//3)

    
    if  LARGEUR//3<event.x <LARGEUR//3+LARGEUR//3 and HAUTEUR//3 +(HAUTEUR//3)<event.y<HAUTEUR:
        canvas.create_line(LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR//3+LARGEUR//3,HAUTEUR)
        canvas.create_line(LARGEUR//3,HAUTEUR,LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3)

#3EME COLONNE
    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and 0<event.y<HAUTEUR//3:
         canvas.create_line(LARGEUR//3+LARGEUR//3,0,LARGEUR,HAUTEUR//3)
         canvas.create_line(LARGEUR//3+LARGEUR//3,HAUTEUR//3,LARGEUR,0)

    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and HAUTEUR//3<event.y<HAUTEUR//3+HAUTEUR//3:
         canvas.create_line(LARGEUR//3+LARGEUR//3,HAUTEUR//3,LARGEUR,HAUTEUR//3+HAUTEUR//3)
         canvas.create_line(LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR,HAUTEUR//3)

    
    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and HAUTEUR//3+HAUTEUR//3<event.y<HAUTEUR:
         canvas.create_line(LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR,HAUTEUR)
         canvas.create_line(LARGEUR//3+LARGEUR//3,HAUTEUR,LARGEUR,HAUTEUR//3+HAUTEUR//3)


def cercle(event):
    
    #1ERCoLoNNE
    
    if  0<event.x <LARGEUR//3 and 0<event.y<HAUTEUR//3:
       canvas.create_oval(0,0,LARGEUR//3,HAUTEUR//3)

    if  0<event.x <LARGEUR//3 and HAUTEUR//3<event.y<HAUTEUR//3 +(HAUTEUR//3):
        canvas.create_oval(0,HAUTEUR//3,LARGEUR//3,HAUTEUR//3+HAUTEUR//3)
    
    if  0<event.x <LARGEUR//3 and HAUTEUR//3 +(HAUTEUR//3)<event.y<HAUTEUR:
        canvas.create_oval(0,HAUTEUR//3+HAUTEUR//3,LARGEUR//3,HAUTEUR)

#2EME COLONNE
   
    if  LARGEUR//3<event.x <LARGEUR//3+(LARGEUR//3) and 0<event.y<HAUTEUR//3:
       canvas.create_oval(LARGEUR//3,0,LARGEUR//3+LARGEUR//3,HAUTEUR//3)

    if  LARGEUR//3<event.x <LARGEUR//3+(LARGEUR//3) and HAUTEUR//3<event.y<HAUTEUR//3+HAUTEUR//3:
        canvas.create_oval(LARGEUR//3,HAUTEUR//3,LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3)

    
    if  LARGEUR//3<event.x <LARGEUR//3+LARGEUR//3 and HAUTEUR//3 +(HAUTEUR//3)<event.y<HAUTEUR:
       canvas.create_oval(LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR//3+LARGEUR//3,HAUTEUR)
#3EME COLONNE
   
    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and 0<event.y<HAUTEUR//3:
        canvas.create_oval(LARGEUR//3+LARGEUR//3,0,LARGEUR,HAUTEUR//3)
    
    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and HAUTEUR//3<event.y<HAUTEUR//3+HAUTEUR//3:
        canvas.create_oval(LARGEUR//3+LARGEUR//3,HAUTEUR//3,LARGEUR,HAUTEUR//3+HAUTEUR//3)
    
    if  LARGEUR//3+LARGEUR//3<event.x <LARGEUR and HAUTEUR//3+HAUTEUR//3<event.y<HAUTEUR:
        canvas.create_oval(LARGEUR//3+LARGEUR//3,HAUTEUR//3+HAUTEUR//3,LARGEUR,HAUTEUR)
    
#Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("test")

#Widgets
canvas = tk.Canvas(fenetre,width=HAUTEUR,height=LARGEUR,bg="white")
bouton_quitter = tk.Button(fenetre,text="quitter",command= lambda : fenetre.destroy())
label_croix = tk.Label(fenetre,text="croix")
label_cercle = tk.Label(fenetre,text="cercle")

#Programme principal

canvas.create_line(LARGEUR//3,0,LARGEUR//3,HAUTEUR,fil= "black")
canvas.create_line(LARGEUR//3+(LARGEUR//3),0,LARGEUR//3+(LARGEUR//3),HAUTEUR,fil= "black")


canvas.create_line(0,HAUTEUR//3,LARGEUR,HAUTEUR//3,fil= "black")
canvas.create_line(0,HAUTEUR//3 +(HAUTEUR//3),LARGEUR,HAUTEUR//3 +(HAUTEUR//3),fil= "black")

canvas.bind("<Button-1>",afficher)
 


#Placement des widgets
canvas.grid(column=0,row=0,rowspan=3)
bouton_quitter.grid(column=1,row=0)
label_cercle.grid(column=1,row=1)
label_croix.grid(column=1,row=2)



#Lancement de la boucle
fenetre.mainloop()