import tkinter as tk
import random as rd
from copy import deepcopy
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#vérifier la win diagonale
# save/load c'est bon mais faut  que maitenant réafficher la save
#constante
########CONSTANTES###########
HAUTEUR = 600
LARGEUR = 700

########VARIABLES###########
couleur = ""
alternance = True
liste_couleur = ["red","yellow"]
n1,n2,n3,n4,n5,n6,n7 = 0,0,0,0,0,0,0
arret_du_jeu = 0
player = "rouge"
tirage = rd.randint(0,2)
save = False

#######FONCTIONS##########
def affichage() :
    global liste_objets,liste_matrice_objets,matrice_jeu,info
    if save == False:
        info_consigne.config(text = "La grille est affichée.")
        liste_objets = []
        liste_matrice_objets = []
        for i in range(7):
            for j in range(6):
                canvas.create_line(i*100,j*100,i*100,j*100+100,width=3,fill="black")
                canvas.create_line(i*100,j*100,i*100+100,j*100,width=3,fill="black")
                liste_objets.append( canvas.create_oval(100*i,100*j,100*i+100,100*j+100,fill = "white"))
        liste_matrice_objets.append([liste_objets[0],liste_objets[1],liste_objets[2],liste_objets[3],liste_objets[4],liste_objets[5]])
        liste_matrice_objets.append([liste_objets[6],liste_objets[7],liste_objets[8],liste_objets[9],liste_objets[10],liste_objets[11]])
        liste_matrice_objets.append([liste_objets[12],liste_objets[13],liste_objets[14],liste_objets[15],liste_objets[16],liste_objets[17]])
        liste_matrice_objets.append([liste_objets[18],liste_objets[19],liste_objets[20],liste_objets[21],liste_objets[22],liste_objets[23]])
        liste_matrice_objets.append([liste_objets[24],liste_objets[25],liste_objets[26],liste_objets[27],liste_objets[28],liste_objets[29]])
        liste_matrice_objets.append([liste_objets[30],liste_objets[31],liste_objets[32],liste_objets[33],liste_objets[34],liste_objets[35]])
        liste_matrice_objets.append([liste_objets[36],liste_objets[37],liste_objets[38],liste_objets[39],liste_objets[40],liste_objets[41]])
    else:
        canvas.create_rectangle(canvas.coords(info[0]))

def clic(event):
    global n1,n2,n3,n4,n5,n6,n7
    if 0 < event.x <100 :
        if n1  <  6 :
            canvas.itemconfigure(liste_matrice_objets[0][5-n1], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n1][0] = 1
            else:
                matrice_jeu[5-n1][0] = 2
            n1 += 1
        else:
            pass
            
    if 100< event.x <200 :
        if n2 < 6 :
            canvas.itemconfigure(liste_matrice_objets[1][5-n2], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n2][1] = 1
            else:
                matrice_jeu[5-n2][1] = 2
            n2 += 1
        else:
            pass
            
    if 200< event.x <300 :
        if n3< 6 :
            canvas.itemconfigure(liste_matrice_objets[2][5-n3], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n3][2] = 1
            else:
                matrice_jeu[5-n3][2]  = 2
            n3 += 1
        else:
            pass    
            
    if 300< event.x <400 :
        if n4 < 6 :
            canvas.itemconfigure(liste_matrice_objets[3][5-n4], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n4][3] = 1
            else:
                matrice_jeu[5-n4][3] = 2
            n4 += 1
        else:
            pass
    
    if  400< event.x <500 :
        if n5 < 6 :
            canvas.itemconfigure(liste_matrice_objets[4][5-n5], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n5][4] = 1
            else:
                matrice_jeu[5-n5][4] = 2
            n5 += 1
        else:
            pass
       
    if 500< event.x <600 :
        if n6 < 6 :
            canvas.itemconfigure(liste_matrice_objets[5][5-n6], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n6][5] = 1
            else:
                matrice_jeu[5-n6][5] = 2
            n6 += 1
        else:
            pass
    
    if 600< event.x <700 :
        if n7 < 6 :
            canvas.itemconfigure(liste_matrice_objets[6][5-n7], fill = couleur)
            if couleur == "red" :
                matrice_jeu[5-n7][6] = 1
            else:
                matrice_jeu[5-n7][6] = 2
            n7 += 1
        else:
            pass
    print(matrice_jeu)

def jeu(event):
    global alternance, couleur
    if arret_du_jeu == 0:
        if alternance == True:
            clic(event)
            if couleur == "red":
                couleur = "yellow"
                info_consigne.config(text = "Joeur jaune à vous de jouer.")
            else:
                couleur = "red"
                info_consigne.config(text = "Joeur rouge à vous de jouer.")
        
            alternance == False
            check_win_horizontale()
            check_win_verticale()
            check_win_diagonale()
    
        else:
            clic(event)
            if couleur == "red":
                couleur = "yellow"
                info_consigne.config(text = "Joeur jaune à vous de jouer.")
            else:
                couleur = "red"
                info_consigne.config(text = "Joeur rouge à vous de jouer.")
            alternance == True
            check_win_horizontale()
            check_win_verticale()
            check_win_diagonale()
            
def check_win_horizontale():
    global arret_du_jeu 
    for i in range(6):
        cpt = 0
        for j in range(6):
            if matrice_jeu[i][j] == matrice_jeu[i][j+1] and matrice_jeu[i][j+1] != 0 :
                cpt+=1
                if cpt == 3:
                    arret_du_jeu+=1
                    if couleur == "red" :
                         info_win.config(text = "Le joueur jaune à gagner")
                    if couleur == "yellow" :
                        info_win.config(text = "Le joueur rouge à gagner")
            else:
                cpt=0

def check_win_verticale():    
    global arret_du_jeu 
    for j in range(7):
        cpt = 0
        for i in range(5):
            if matrice_jeu[i][j] == matrice_jeu[i+1][j] and matrice_jeu[i+1][j] != 0 :
                cpt+=1
                if cpt == 3:
                    arret_du_jeu+=1
                    if couleur == "red" :
                        info_win.config(text = "Le joueur jaune à gagner")
                    if couleur == "yellow" :
                        info_win.config(text = "Le joueur rouge à gagner")
            else:
                cpt=0

def check_win_diagonale():
    global arret_du_jeu
    for j in range(7):
        cpt = 0
        for i in range(5):
            if matrice_jeu[i][j] == matrice_jeu[i+1][j+1] and matrice_jeu[i+1][j+1] != 0 :
                cpt+=1
                if cpt == 3:
                    arret_du_jeu+=1
                    if couleur == "red" :
                        info_win.config(text = "Le joueur jaune à gagner")
                    if couleur == "yellow" :
                        info_win.config(text = "Le joueur rouge à gagner")
            else:
                cpt=0


def save_party():
    """Sauvegarde la partie en cours et les mouvements effectués
    lors de celle-ci dans un fichier '.taquin'."""
    save_dir = asksaveasfilename(initialdir=os.getcwd(),
                                 initialfile="save.puissance4")
    if save_dir[-11::] == ".puissance4":
        print("Directory : ", save_dir)
        fichier = open(file=save_dir, mode="w")
        info = deepcopy(str(liste_matrice_objets))
        #info2 = deepcopy(str(matrice_jeu))
        fichier.write(info)
        #fichier.write(info2)
        fichier.close()
    elif save_dir == "":
        print("tu as quitter la fentre sauvegarde")
    else:
        print("Wmauvais type de fichier")
        save_party()

def load_party():
    global info
    load_dir = askopenfilename(initialdir=os.getcwd())
    fichier = open(file=load_dir, mode="r")
    info = fichier.readline().split()
    fichier.close()
    affichage(info)

def retour():
    pass
    
######BOUCLE_PRINCIPALE#########
root = tk.Tk()
root.title("puissance4")
canvas = tk.Canvas(root,width=LARGEUR,height=HAUTEUR,bg="blue")
canvas.grid(row=1,column= 0, columnspan=4)

bouton_save = tk.Button(root, text = "sauvegarder", command = save_party)
bouton_save.grid(row = 2,column= 0)

bouton_affichage = tk.Button(root, text = "affichage de la grille", command = affichage)
bouton_affichage.grid(row=2,column= 1)

bouton_load = tk.Button(root, text = "chargement", command = load_party)
bouton_load.grid(row = 2,column= 2)

bouton_retour = tk.Button(root, text = "retour", command = retour)
bouton_retour.grid(row = 2,column= 3)

info_consigne = tk.Label(root,text = "Bienvenue  ce jeu est un puissance4. \n Appuyer sur affichage pour commerncer le jeu.",font = ("helvetica",16),fg = "red")
info_consigne.grid(row = 0,column=2)
info_win = tk.Label(root,text = "", font = ("helvetica",15))
info_win.grid(row = 0 ,column=1)

matrice_jeu = []
for i in range(6) :
    matrice_jeu.append([])
    for j in range(7):
        matrice_jeu[i].append(0)
print(matrice_jeu)

if tirage == 0:
    couleur = "red"
else:
    couleur = "yellow"

jeu()
canvas.bind("<Button-1>", jeu)

#####BOUCLE_COPNTINUE######
root.mainloop()