import tkinter as tk




HAUTEURS =500

LARGEUR = 500

def modification_carre():
     if x1-x0 >20:
         canvas.itemconfig(nf)




    pass


def pause():
    pass


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HAUTEURS, width=LARGEUR)
canvas.grid()

bouton_pause = tk.Button(racine, text = "pause",command = pause)
bouton_pause.grid()


canvas.create_rectangle(240,240,260,260,fill="red")


racine.mainloop()