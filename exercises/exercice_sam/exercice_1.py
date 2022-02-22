
#prgramme crer un retangle selon la couleur demander par l'utilisateur
import tkinter as tk


nb_clic=0

LARGEUR=500
HAUTEUR=500

def remplir_vider(event):
    global nb_clic
    nb_clic +=1
    if nb_clic % 2 == 1:
        couleur = "red"
    else:
        couleur = "blue"
    canvas.itemconfigure(rectangle,fill= couleur)

def initialisation ():
    canvas.itemconfigure(rectangle, fill="red")

racine =tk.Tk()
racine.title("test")
canvas = tk.Canvas(racine, bg="black", height=HAUTEUR, width=LARGEUR)
buton01= tk.Button(racine, text="recommencer", font = ("helvetica", "30"),background="red" , command=initialisation)
buton01.config(bg="red")
canvas.grid()
buton01.grid()

rectangle = canvas.create_rectangle(50,100,300,300,fill = "red")
canvas.bind("<Button-1>", remplir_vider)
racine.mainloop()

