#librairie
import tkinter as tk

#constante
Hauteur = 300
Largeur = 300

liste=[]
nb_clic = 0

#fonctions

def destroy():
   """détruit la fenetre"""
   racine.destroy()


def le_nb_clic(event):
   """compte le nombre de clic"""
   global nb_clic
   nb_clic += 1
   label1["text"] = str(nb_clic)
   


def decompte(event):
   """decompte le nombre de clic"""
   global nb_clic
   nb_clic -= 1
   print(nb_clic)
   label1["text"] = str(nb_clic)
   

def renvoie_la_couleur_du_canvena(event):
   """renvoie la couleur du canvans dans le label"""
   if event.widget == canvas_rouge:
      label1["text"] = "rouge"
   if event.widget == canvas_black:
      label1["text"] = "noir"


#programme principal
racine = tk.Tk()
racine.title("Rappel du premier semestre")
label1= tk.Label(racine,text="J'adore python!")
bouton1=tk.Button(racine,text="destroy",command=destroy)
canvas_rouge = tk.Canvas(racine,width=Hauteur,height=Largeur,bg="red")
canvas_black = tk.Canvas(racine,width=Hauteur,height=Largeur,bg="black")

label1.grid(row=0,column=0)
bouton1.grid(row=1,column=0)
canvas_rouge.grid(row=0,column=1)
canvas_black.grid(row=1,column=1)

canvas_rouge.bind("<Button-1>",le_nb_clic)
canvas_rouge.bind("<Button-2>",decompte)
canvas_rouge.bind("<Double-Button-1>",renvoie_la_couleur_du_canvena)
canvas_black.bind("<Double-Button-1>",renvoie_la_couleur_du_canvena)




racine.mainloop()