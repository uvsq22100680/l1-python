# Liste des capitales européennes
capitales = ["Paris", "Berlin", "Madrid", "Athènes", "Zagreb", "Rome", "Amsterdam"]
print(capitales, type(capitales))

# Liste d'entiers
entiers = [5, 0, 17, 42, 23]
print(entiers)

# Liste mixte
mixte = [7, "tennis", True, 5.3, [2, 3]]

#fonction len()
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La liste contient", len(liste), "éléments.")

len([5.3, -0.1, 4.5, 7.7])

chaine = 'abracadabra'
print(len(chaine))

#Accéder aux éléments liste

liste = ["bus", "voiture", "vélo", "trotinette"]

print(liste[0])
print(liste[2])
print(liste[len(liste)-1])
print(liste[-1])

#modifier ou ajouter des éléments dans une liste
capitales = ["Paris", "Berlin", "Madrid", "Athènes", "Zagreb", "Rome", "Amsterdam"]
print(capitales)

capitales[2] = "Copenhague"
print(capitales)


#chaine de caractère et liste
s = "Hello world"
print(s[0], s[-1], len(s), max(s))
s2 = s + s
print(s2)

#chaines de caractères ne sont pas mutables
#s[0] = "x"
s_res = "x" + s[1:]
print(s_res)
#certaines méthodes ne s'appliquent qu'aux listes qu'aux chaines de caracrères
#s.append("x")

#liste = ["a", "b", "c"]
#s2 = s.upper()
#print(s2)
#liste2 = liste.upper()

#liste = list(s)
#print(liste)
#s2 = "".join(liste)
#print(s2)

#copie d'une liste il le faut jamais utiliser = pour copier une liste ils sont la meme memoire
L1 = [1, 2, 3, 4, 5, 6]
L2 = L1

L2.append(7)
print(len(L1)) 

#liste en paramètre d'une fct

def f(liste, entier, chaine):
    "la liste étant mutable elle est modifié si ell est passé en argument"
    liste[0] += 1
    entier += 1
    chaine = "b"

L, i, s = [2], 5, "a"
f(L, i, s)
print(L, i, s)


#liste imbriquées

L = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(L[0])
print(L[1])
print(L[2][1])

#calcul de la somme de la liste L
somme = 0

for i in range(len(L)):
    for j in range(len(L[i])):
        somme += L[i][j]

print("La somme de tous les éléments de la liste vaut :", somme)

L = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

#autre facon plus élégante calcul de la somme de la liste L
somme = 0
for liste in L:
    for e in liste:
        somme += e
print("La somme de tous les éléments de la liste vaut :", somme)

#matrice
m = 3
n = 4
L = []
for i in range(m):
    L.append([0]*n)
print(L)


import copy
L1 = [[1, 2],[3, 4]]
L2 = copy.deepcopy(L1)
L2[0][0] = 0
print(L1)

#questions 1

def f(u, v):
    u = v

l1 = [1, 2]
l2 = [3, 4]
f(l1, l2)
print(l1)

#question 2
def f(x):
    x[0] = x[1]
    
u = [[1], [2]]
f(u)
print(u[0])

#question 3

v = [4, 7, 2]
w = [v, v]
w[-1][-1] = 0
print(v[2])

#question 4
v = [0]
v.append(v)
print(v[1])