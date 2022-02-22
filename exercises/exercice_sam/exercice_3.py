import tkinter as tk




LARGEUR = 500
HAUTEUR = 500
object=[]


def rectangle(event): 
        if  166 <event.x < 360 :
            canvas.create_rectangle(event.x,event.y, event.x+10,event.y+10,fill="green")

def rectanle_vert(event):
    if  len(object) == 3:
        rectangle(event)


def creer_croix(event):
    
    if 0<event.x<HAUTEUR/3:
        
        x0 = event.x
        x1 = event.x
   
   
        y0 = event.y
        y1 = event.y

        identifiant = canvas.create_line(x0,y0,x1+10,y1+10,fill = "blue",width = 2)
        identifiant = canvas.create_line(x0,y0+10,x1+10,y1,fill="blue",width=2)
        object.append(identifiant)


def efface_canvas():
    canvas.delete(object)

racine = tk.Tk()
racine.title("exo3")
canvas = tk.Canvas(racine,width=LARGEUR,height=HAUTEUR,bg = "black")
canvas.grid()


bouton_restart = tk.Button(racine,text ="restart",command=efface_canvas)
bouton_restart.grid()
canvas.create_line(LARGEUR/3,0,LARGEUR/3,HAUTEUR,fill ="white")
canvas.create_line((LARGEUR/3)*2,0,(LARGEUR/3)*2,HAUTEUR,fill ="white")

canvas.bind("<Button-1>",creer_croix)
canvas.bind("<Button-2>",rectanle_vert)





racine.mainloop()