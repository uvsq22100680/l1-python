import tkinter as tk

HAUTEUR = 500
LARGEUR = 500
clic=0
liste=[]

def clic_line(event):
    x0 = event.x
    liste.append(x0)
    y0 = event.y
    liste.append(y0)
    
    x1 = event.x
    y1 =event.y
    
    
    canvas.create_line(liste[1],y0,x1,y1,fill ="blue")

    



    pass



racine = tk.Tk()
canvas = tk.Canvas(racine,width=LARGEUR,height=HAUTEUR,bg = "white")
bouton_pause=tk.Button(racine,text="pause")


canvas.grid()
bouton_pause.grid()
canvas.bind("<Button-1>",clic_line)




racine.mainloop()