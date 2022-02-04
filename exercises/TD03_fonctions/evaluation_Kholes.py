def liste_decroissante(n):
    l=[]
    while n >= 1 :
        print(n)
        l.append(n)
        n -=1
    return l
print(liste_decroissante(5))


liste_morpion =[[1,0,0],[1,0,0], [1,0,0]]

def verifie_colonne(liste_morpion,n) :
    liste = [liste_morpion[0][n]+liste_morpion[1][n]+liste_morpion[2][n]]
    print (liste)
    
    if liste[0][n] == 6:
        print(" 3 croix")
        return 2
    elif liste[n] == 3:
        print("3  cercle")
        return  1
    else:
        print('rien')
        return -1

print(verifie_colonne(liste_morpion,2))

print("en vacance")


    
    

    
    
    
    
        
    



    



