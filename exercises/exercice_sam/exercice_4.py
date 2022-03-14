import tkinter as tk




HAUTEURS = 500

LARGEUR =  500

x0=150
y0=200

x1=200
y1=300

def modification_carre(event):
    global x1,x0,y0,y1
    if x0<event.x <x1 and y0 <event.y <y1 :
        if x1-x0 >= 30:
            canvas.coords(rectangle,x0,x1,y0-10,y1-10)

    if 0<event.x<150 and 200<event.x<500:
        canvas.coords(rectangle,x0,x1,y0+10,y1+10)
    

    


         




def pause():
    pass


racine = tk.Tk()
racine.title("exercice_4")

canvas = tk.Canvas(racine, bg="white", height=HAUTEURS, width=LARGEUR)
canvas.grid()

bouton_pause = tk.Button(racine, text = "pause",command = pause)
bouton_pause.grid()


rectangle = canvas.create_rectangle(x0,x1,y0,y1,fill="red")
canvas.bind("<Button-1>",modification_carre)

racine.mainloop()