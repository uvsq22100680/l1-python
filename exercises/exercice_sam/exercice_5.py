import tkinter as tk

fenetre = tk.Tk()
fenetre.title("exercice 5")

LARGEUR=600
HAUTEUR=600
deplacement_ligne =10

def clic(event):
    global deplacement_ligne
    if 0 <event.x < LARGEUR/3 :
        canvas.coords(ligne_gauche,LARGEUR/3-deplacement_ligne,0,LARGEUR/3-deplacement_ligne,HAUTEUR)
        canvas.coords(ligne_droite,LARGEUR/3+(LARGEUR/3)-deplacement_ligne,0,LARGEUR/3+(LARGEUR/3)-deplacement_ligne,HAUTEUR)
        deplacement_ligne += 10

    if LARGEUR/3 <event.x < LARGEUR/3+(LARGEUR/3) :
        canvas.coords(ligne_gauche,LARGEUR/3+deplacement_ligne,0,LARGEUR/3+deplacement_ligne,HAUTEUR)
        canvas.coords(ligne_droite,LARGEUR/3+(LARGEUR/3)-deplacement_ligne,0,LARGEUR/3+(LARGEUR/3)-deplacement_ligne,HAUTEUR)
        deplacement_ligne += 10
    
    if LARGEUR/3+(LARGEUR/3) < event.x < LARGEUR :
        canvas.coords(ligne_gauche,LARGEUR/3+deplacement_ligne,0,LARGEUR/3+deplacement_ligne,HAUTEUR)
        canvas.coords(ligne_droite,LARGEUR/3+(LARGEUR/3)+deplacement_ligne,0,LARGEUR/3+(LARGEUR/3)+deplacement_ligne,HAUTEUR)
        deplacement_ligne += 10

def recommencer():
    canvas.coords(ligne_gauche,LARGEUR/3,0,LARGEUR/3,HAUTEUR)
    canvas.coords(ligne_droite,LARGEUR/3+(LARGEUR/3),0,LARGEUR/3+(LARGEUR/3),HAUTEUR)
    

canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="white")
bouton_recommencer = tk.Button(fenetre,text="recommencer",command=recommencer)

canvas.grid()
bouton_recommencer.grid()

ligne_gauche=canvas.create_oval(LARGEUR/3,0,LARGEUR/3,HAUTEUR,fil ="red")
ligne_droite=canvas.create_oval(LARGEUR/3+(LARGEUR/3),0,LARGEUR/3+(LARGEUR/3),HAUTEUR,fil ="blue")



canvas.bind("<Button-1>",clic)






fenetre.mainloop()