import tkinter as tk

fenetre = tk.Tk()
fenetre.title("exercice 6")

LARGEUR=500
HAUTEUR=500


def clic(event):
    if 0<event.x<25 and 0<event.y<50 :
        canvas.itemconfig(cercle,fil='green')
    elif 25<event.x<50 and 0<event.y<50:
        canvas.itemconfig(cercle,fil='yellow')
    
    elif 50<event.x<100 and 0<event.y<50:
        canvas.itemconfig(cercle,fil='blue') 

    else:
        canvas.itemconfig(cercle,fil="black")
    

def annuler():
     pass

   
    

canvas = tk.Canvas(fenetre,width=LARGEUR,height=HAUTEUR,bg="white")
bouton_annuler = tk.Button(fenetre,text="annuler",command=annuler)
bouton_quitter = tk.Button(fenetre,text="quitter",command = lambda : fenetre.destroy())

canvas.grid(row=0,column=1)
bouton_annuler.grid(row=0,column=0)
bouton_quitter.grid()


canvas.create_rectangle(0,0,50,50,fil="green")
canvas.create_rectangle(25,0,75,50,fil="yellow")
canvas.create_rectangle(50,0,100,50,fil="blue")
cercle =canvas.create_oval(LARGEUR/2-25,HAUTEUR/2-25,LARGEUR/2+25,HAUTEUR/2+25,fil="black")


canvas.bind("<Button-1>",clic)






fenetre.mainloop()