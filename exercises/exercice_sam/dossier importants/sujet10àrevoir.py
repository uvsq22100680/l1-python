import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt = 0
###################
# Fonctions



def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""

    rebond()
    balle_change_couleur()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)
        
    


def rebond():

    """Fait rebondir la balle sur les bords du canevas"""
    global balle,cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])

    if cpt < 30:
            if x0 <= 0 or x1 >= 600:
                balle[1] = -balle[1]
                cpt +=1
            
            if y0 <= 0 or y1 >= 400:
                balle[2] = -balle[2]
                cpt +=1
    else:
        balle[1], balle[2] = 0,0
    
       
    
def creer_rectangles(event):
    global  zone1,zone2,zone3,zone4
    zone1=0,0,event.x,event.y
    zone2=LARGEUR,0,event.x,event.y
    zone3=0,HAUTEUR,event.x,event.y
    zone4=LARGEUR,HAUTEUR,event.x,event.y
    zone1=canvas.create_rectangle(zone1[0],zone1[1],zone1[2],zone1[3],fill="red")
    zone2=canvas.create_rectangle(zone2[0],zone2[1],zone2[2],zone2[3],fill="white")
    zone3=canvas.create_rectangle(zone3[0],zone3[1],zone3[2],zone3[3],fill="white")
    zone4=canvas.create_rectangle(zone4[0],zone4[1],zone4[2],zone4[3],fill="red")

    

def balle_change_couleur():
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    
    if zone1[0]< x0 <zone1[2] and zone1[1] < y0 <zone1[3]:
        canvas.itemconfigure(balle[0],fil="white")

    if zone2[0]< x0 <zone2[2] and zone2[1] < y0 <zone2[3]:
        canvas.itemconfigure(balle[0],fil="red")
    
    if zone3[0]< x0 <zone3[2] and zone3[1] < y0 <zone3[3]:
        canvas.itemconfigure(balle[0],fil="red")

    if zone4[0]< x0 <zone4[2] and zone4[1] < y0 <zone4[3]:
        canvas.itemconfigure(balle[0],fil="white")



def demarrer(event):
    global balle
    
    creer_rectangles(event)
    
    balle = creer_balle() 
    mouvement()
    
    

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()
canvas.bind("<Button-1>",demarrer)

# initialisation de la balle


# déplacement de la balle

# boucle principale
racine.mainloop()
