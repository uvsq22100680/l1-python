import tkinter as tk

HAUTEUR = 500
LARGEUR = 500
nb_clic = 0
point1=(-1,1)

def clic_line(event):
    global point1, nb_clic
    if nb_clic==0:
       point1=(event.x,event.y)
       nb_clic +=1
    else:
        point2 =(event.x,event.y)
        nb_clic=0
        canvas.create_line(point1[0],point1[1],point2[0],point2[1],fill ="blue")

    


    
    
   
   
   





racine = tk.Tk()
canvas = tk.Canvas(racine,width=LARGEUR,height=HAUTEUR,bg = "white")
bouton_pause=tk.Button(racine,text="pause")


canvas.grid()
bouton_pause.grid()
canvas.bind("<Button-1>",clic_line)




racine.mainloop()