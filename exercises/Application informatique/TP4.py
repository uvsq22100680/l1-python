import tkinter as tk
import random as rd
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

#fonctions principal
def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)

def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat

create=True
nomImgCourante=""
nomImgDebut = ""

def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    global nomImgDebut
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    nomImgDebut = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
        create=False
        
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)

def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"

def reaffiche():
    global imgDebut
    global nomImgCourante
    if not create :
        imgDebut=ImageTk.PhotoImage(file=nomImgDebut)
        canvas.itemconfigure(dessin, image=imgDebut)
        nomImgCourante = nomImgDebut

def filtre_vert():
    mat=loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(0,mat[i][j][1],0,255)
    modify(mat)
            
def negatif():
    mat=loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(255-mat[i][j][0],255-mat[i][j][1],255-mat[i][j][2],255)
    modify(mat)
            
def symetrique():
    mat=loading(nomImgCourante)
    matSym=[[(0,0,0,0)]*nbrCol(mat) for k in range(nbrLig(mat))]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            matSym[i][nbrCol(mat)-1-j]=mat[i][j]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=matSym[i][j]
    modify(mat)

def luminosite(r,g,b):
    return int(0.2125 * r + 0.7154 * g + 0.0721 * b)

def gris():
    #On utilisera la conversion CIE709 qui permet de calculer la teinte de gris qui va être affichée dans le pixel
    #La teinte affichée est : gris=0,2125*rouge + 0,0721*bleu + 0,7154*vert
    mat=loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            l = luminosite(mat[i][j][0],mat[i][j][1],mat[i][j][2])
            mat[i][j] =(l,l,l,255)
            #r,g,b = mat[i][j]l = luminosite(r,g,b)mat[i],[j] = (l,l,l,255)
            # calcul de la teinte de gris du pixel (CIE709)

    modify(mat)

def noirBlanc():
    mat=loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            l = luminosite(mat[i][j][0],mat[i][j][1],mat[i][j][2])
            mat[i][j] =(0,0,0) if l <127 else (255,255,255)
            

            # un pixel est blanc quand sa luminosité est > à 127, noir sinon
    modify(mat)

create=True

def zoom():
    mat=loading(nomImgCourante)
    out =[]
    #créer une matrice de largeur et hauteur deux fois plus grande 
    for i in range(nbrLig(mat)):
        l =[]
        for j in range(nbrCol(mat)):
           l.append(mat[i][j])
           l.append(mat[i][j])
        out.append(l)
        out.append(l)
    mat = out


    modify(mat)

def shrink():
    mat=loading(nomImgCourante)
    #créer une matrice de largeur et hauteur deux fois plus petite 
    out = []
    for i in range(nbrLig(mat)):
        if i % 2 == 1 :
            continue
        l = []
        for j in range(nbrCol(mat)):
            if j % 2 == 0 :
                try :
                    r = int((mat[i][j][0] + mat[i][j+1][0] + mat[i+1][j][0] + mat[i+1][j+1][0]) / 4)
                    g = int((mat[i][j][1] + mat[i][j+1][1] + mat[i+1][j][1] + mat[i+1][j+1][1]) / 4)
                    b = int((mat[i][j][2] + mat[i][j+1][2] + mat[i+1][j][2] + mat[i+1][j+1][2]) / 4)
                    l.append((r, g, b, 255))
                except :
                    pass
        out.append(l)
    mat = out
    modify(mat)



def rotate():
    
    mat=loading(nomImgCourante)
    out =[]
    for i in range(nbrCol(mat)):
        l = []
        for j in range(nbrLig(mat)):
            l.append(mat[j][i])
        l.reverse()
        out.append(l)
    mat = out
    modify(mat)


def dithering():
    mat=loading(nomImgCourante)
    random = rd.randint(0, 255)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            l = luminosite(mat[i][j][0], mat[i][j][1], mat[i][j][2])
            if l > random :
                mat[i][j] = (255, 255, 255, 255)
            else :
                mat[i][j] = (0, 0, 0, 255)
    modify(mat)



#Fonctions auxiliaires 
fenetre = tk.Tk()
fenetre.title("mon petit photoshop")

#Création des Widgets
bouton_reaffiche= tk.Button(fenetre,text="reaffiche",command =  reaffiche)
bouton_charger = tk.Button(fenetre, text = "charger", command = lambda : charger(fenetre))
bouton_quitter = tk.Button(fenetre,text="quitter",command = lambda : fenetre.destroy())

bouton_filtrevert= tk.Button(fenetre,text="filtre vert",command = filtre_vert)
bouton_negatif = tk.Button(fenetre, text = "negatif", command = negatif)
bouton_symetrique = tk.Button(fenetre,text="symetrique",command = symetrique)

bouton_gris = tk.Button(fenetre,text="gris",command=gris)
bouton_noirblanc = tk.Button(fenetre,text="noirblanc",command=noirBlanc)
bouton_zoom=tk.Button(fenetre,text="zoom",command=zoom)
bouton_shrink=tk.Button(fenetre,text="shrink",command=shrink)
bouton_rotate=tk.Button(fenetre,text="rotate",command=rotate)
bouton_dithering=tk.Button(fenetre,text="dithering",command=dithering)

#Positionnement des Widgets
bouton_charger.grid(row=4,column=0)
bouton_reaffiche.grid(row=4,column=1)
bouton_quitter.grid(row=4,column=2)

bouton_filtrevert.grid(row=5,column=0)
bouton_negatif.grid(row=5,column=1)
bouton_symetrique.grid(row=5,column=2)

bouton_gris.grid(row=6,column=0)
bouton_noirblanc.grid(row=6,column=1)

bouton_zoom.grid(row=6,column=2)
bouton_shrink.grid(row =7,column=0)
bouton_rotate.grid(row =7,column=1)
bouton_dithering.grid(row =7,column=2)
#Lancement de la boucle 
fenetre.mainloop()
