
#multiplication
def multiplication(a,b):
    m = a * b
    return m
print(multiplication(3,4))

#table de multiplication
def table_multiplication(a):
    l = [i * a for i in range(0,11)]
    return l
print(table_multiplication(5))

#renvoie des étoiles
def etoiles(n):
    n = n * "*"
    return n
print(etoiles(5))

#revoie f(x)
def f(x):
    for x in range(0,21):
            a=100*x-4*x**2+2
            print(a)
    return a

#calcul la population selon une évolution définie
def calculpopulation(x):
    for i in range(0,11):
        x = x * 1.03
        print(x)
    return x
print(calculpopulation(4000))

#revoie le discriminant
def discriminant(a, b, c):
   
    a = input("enter une valeur pour a")
    b = input("enter une valeur pour b")
    c = input("entrer une valeur pour c")
    delta = int(b) ** 2 - 4 * int(a) * int(c)
    return delta

 #somme d'un nombre à un d'autre   
def calcul(a,b):
    s = 0
    for i in range(a,b):
        s= s+i
    return s
print((calcul(0,101)))

#revoie un nombre à la puissance 3
def cube(x):
    return x**3
print(cube(2))


import math

#renvoie volume de la sphère
def volumeSphere(rien):
    v = (4* math.pi * cube(2))/3
    return v
print(volumeSphere(1))

def mafonction(x):
    a = 2*(cube(x))+x-5
    return a
print(mafonction(2))

#renvoie  ce que vous saississez
def dire(a):
    a =input("saississez votre prénom")
    return a

#exercice1 sujet 60
def ma_fct(n):
    liste =[]
    p = 0
    i = 0
    while i != n:
        a=[2**p + 2**p -1]
        liste.append(a)
        i+=1
        p+=1
    return liste
print(ma_fct(4))

#exercice2 sujet 60
liste_imbrique = [[1,2,3],[4,5,6],[7,8,9]]
print(liste_imbrique)

def fctliste(liste_imbrique) :
    lr = [liste_imbrique[0][0]+liste_imbrique[1][0]+liste_imbrique[2][0],liste_imbrique[0][1]+liste_imbrique[1][1]+liste_imbrique[2][1],liste_imbrique[0][2]+liste_imbrique[1][2]+liste_imbrique[2][2]]
    return lr
print(fctliste(liste_imbrique))

    
#elemine les termes en double
def elimine2(L):
  for e in L:
    if L.count(e)>1:
      for i in range(L.count(e)-1):
        L.remove(e)
  return

  #renvoie les solution de l'équation

def solution(a):
    pass # à faire
    return a

def inverser_liste(p)
    reversed()

