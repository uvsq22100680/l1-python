
#prgramme crer un retangle selon la couleur demander par l'utilisateur
import tkinter as tk
import random



LARGEUR=300
HAUTEUR=300

def rectangle():
    a = random.randint(0,300) 
    b = random.randint(0,300) 
    canvas.create_rectangle(a,b,b+100,a+100,fill=couleur)


def choi_de_la_couleur():
    global couleur
    couleur = input("ecricrez une couleur")


racine =tk.Tk()
racine.title("test")
canvas = tk.Canvas(racine, bg="black", height=HAUTEUR, width=LARGEUR)
buton01= tk.Button(racine, text="creer rectangle", font = ("helvetica", "30"), command= rectangle)
buton02= tk.Button(racine, text="choix couleur", font = ("helvetica", "30"), command= choi_de_la_couleur)
canvas.grid()
buton01.grid()
buton02.grid()

racine.mainloop()