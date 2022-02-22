
import tkinter as tk
import random as rd


H = 500
L = 500
grille = 10
liste_canvas = []



def ma_commande(event):
    x = rd.randint(0,250)
    y = rd.randint(250,500)
    
    canvas.create_rectangle(x,y,x+100,y+100,fill="red")

def delete():
    canvas.delete("all")

def generation():
    for i  in range(grille):
        liste_canvas.append([])
        for j in range(grille):
            liste_canvas.append(rd.randint(0,9))
    for x in range(grille):
        for y in range(grille):
            canvas.create_rectangle(50,50,100,100,texte=grille,fill="white")
        

    

def change_coleur(event):
    canvas.itemconfigure(carre,fill = "white")





racine = tk.Tk() 

canvas=tk.Canvas(racine,height=H,width=L,bg='black')


bouton1= tk.Button(racine, text="test",bg = "red",command=ma_commande)
bouton2= tk.Button(racine,text="delete",command=delete)
bouton3 = tk.Button(racine,text="generation",command=generation)
bouton4 = tk.Button(racine,text ="change couleur",command=change_coleur)
#columnspan étend l'affichage sur plusieurs colonnes
bouton1.grid(row=0,column=0)

bouton2.grid(row=0,column=1)
bouton3.grid(row=0, column=2)
bouton4.grid(row =0,column=4)
canvas.grid(row=1,columnspan=4)

canvas.bind("<Button-1>", ma_commande)
canvas.bind("<Button-2>", change_coleur)

carre = canvas.create_line(50,50,100,100,fill="blue")











racine.mainloop()