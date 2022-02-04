import tkinter as tk
from tkinter.constants import RAISED
import random
couleur = "blue"
objets = []
def cercle():
    a = random.randint(0,300) 
    b = random.randint(0,300) 
    identifiant = canvas.create_oval((a,b),(a+100,b+100),fill= couleur)
    objets.append(identifiant)
    
def carre():
    a = random.randint(0,300) 
    b = random.randint(0,300) 
    identifiant=canvas.create_rectangle((a,b),(a+100,b+100),fill= couleur)
    objets.append(identifiant)
def croix():
    a = random.randint(0,300) 
    b = random.randint(0,300) 
    identifiant =canvas.create_line((a,b),(a+100,b+100),fill= couleur, width= 10)
    identifiant =canvas.create_line((a,b+100),(a+100,b),fill= couleur, width= 10)
    objets.append(identifiant)
 
def choix_couleur():
    global couleur
    couleur = input("ecricrez une couleur")

def undo():
    if len(objets) == 0:
        return
    canvas.type(objets[-1])
    if type == "line":
        identifiant_objet = objets[-1]
        canvas.delete(identifiant_objet)
        del objets[-1]
    identifiant_objet = objets[-1]
    canvas.delete(identifiant_objet)
    del objets[-1]
    
    

    


dessin = tk.Tk() 

canvas = tk.Canvas(dessin, width =400, height =400,bg= "black")
canvas.grid(column=2, row=1, rowspan=3)
dessin.title("mon dessin")

bouton1 = tk.Button(dessin, text = "choisir une couleur", font=("helvetica","20"),command = choix_couleur)
bouton1.grid()
bouton1.grid(column=2, row = 0)

bouton2 = tk.Button(dessin, text = "cercle", font=("helvetica","20"),command = cercle)
bouton2.grid()
bouton2.grid(column=0, row = 1)

bouton3 = tk.Button(dessin, text = "carré", font=("helvetica","20"),command = carre)
bouton3.grid()
bouton3.grid(column=0, row = 2)

bouton4 = tk.Button(dessin, text = "croix", font=("helvetica","20"),command = croix)
bouton4.grid()
bouton4.grid(column=0, row = 3)

bouton5 = tk.Button(dessin,text="undo", font= ("helvetica","20"),command = undo)
bouton5.grid()
bouton5.grid(column=3,row=0)

dessin.mainloop()