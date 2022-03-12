import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog

mat =   [[1,1,2,3],[3,5,6,2],[7,8,5,5]]


def nbrCol(matrice):
    return (len(matrice[0]))


def nbrLig(matrice):
    return len(matrice)

def rempli9(matrice):
    
    for i in range(nbrLig(matrice)):
        for j in range(nbrCol(matrice)):
            matrice[i][j] = 9
           
    

rempli9(mat)
print(mat)

def rempli8(matrice):
    for l in matrice:
        for i in range(len(l)):
            l[i]=8




rempli8(mat)
print(mat)

for v in mat:
    print(v)

for i in range(len(mat)):
    print(i)



def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)


matVB=[[(0,0,0,255)]*100 for i in range(100)]

def rempliVB(matrice):
    for i in range(nbrLig(matrice)):
        for j in range(nbrCol(matrice)):
            if j<=49:
                matrice[i][j]= (0,255,0,255)
            else:
                matrice[i][j]= (0,0,255,255)
    



def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat



print(nbrCol(mat)*nbrLig(mat)*len(mat[0][0]))



def ajouteCarreNoir(mat):
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            if 25 < i<75 and 25<j<75:
                matrice[i][j]= (0,0,0,255)





matrice=loading("tomate.png")

def filtre_vert(mat):
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]= (0,mat[i][j][1],0)

filtre_vert(matrice)
saving(matrice,"tomateVert.png")

matrice=loading("tomate.png")

def negatif(mat):   
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]= mat[i][j] =(255-mat[i][j][1],255-mat[i][j][2],255-mat[i][j][3])


negatif(matrice)
saving(matrice,"tomateNeg.png")

matrice=loading("tomate.png")

def symetrique(mat):   
    for l in mat:
        l.reverse()

symetrique(matrice)
saving(matrice,"tomateSym.png")