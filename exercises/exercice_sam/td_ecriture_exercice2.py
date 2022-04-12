
import random

def nb_lignes(nom_fichier):
    fichier = open(nom_fichier,"r")
    l=0
    for ligne in fichier:
        l +=1
    return l



def ecrit_liste_mots(n):
    fic1 = open("words.txt","r")
    fic2 = open("words+str(n).txt","w") 
    while(True):
        new_line = fic1.readlines()
        if(new_line == ""):
            break
        if(len(new_line)== n+1):
            fic2.write(new_line)
    fic1.close()
    fic2.close()



def melange_mots(nom_fichier):
    fichier1 = open(f"{nom_fichier}.txt", "r")
    fichier2 = open(f"{nom_fichier}.mel", "w")
    mots1 = fichier1.readlines()
    random.shuffle(mots1)
    fichier1.close()
    for mot in mots1:
        fichier2.write(mot)
    fichier2.close()

def compare_mots(m1, m2):
    liste=[]
    l1 = list(m1)
    l2 = list(m2)
    for i in range(len(l1)):
        if l1[i]in m2:
            if l1[i] == l2[i]:
                liste.append(1)
            else:
                liste.append(2)
        else:
            liste.append(0)
        

    return liste   



print(compare_mots("salutatie","bienvenue"))
                     

def compare_mots(m1, m2):
    m1=m1.strip("\n")
    n=len(m1)
    profil=[-1]*n
    copy_m2=list(m2)
    for i in range(0,n):
        if(m1[i]==m2[i]):
            profil[i]=1
            copy_m2.remove(m1[i])
    for i in range(0,n):
        if(profil[i]==-1):
            if(m1[i] in copy_m2):
                profil[i]=2
                copy_m2.remove(m1[i])
            else:
                profil[i]=0
    return profil

print(compare_mots("vve","eve"))

#https://github.com/Joseph