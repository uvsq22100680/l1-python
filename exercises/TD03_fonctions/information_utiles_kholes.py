Li=["titi",2,"toto"]
Li1=list(range(1,10))
print(Li)
print(Li1)

Li2=[0]*10
print(Li2)

#ajoute un élément
Li2.append(3)
print(Li2)

# deux méthodes pour supprimer un élément
del Li2[0]
print(Li2)

Li2.remove(3)
print(Li2)


#connaitre les termes d'une liste
L=[1,2,3,4]
for i in range(0,len(L)):
    print(L[i])

#somme d'une liste
l=[2,1,3,6]
s = 0
for i in range(0,len(l)):
    s = s + l[i]
print(s)



#moyenne d'une liste
s = 0
for i in range(0,len(L)+1):
    s = s + i
print(s/len(L))

#créer une liste de 0 à  20
N =[i for i in range(0,21)]
print(N)

#f(x)
def fct(x):
    r = x ** 2 + x + 5
    return r
print(fct(2))


#donne le type 
def info_type(n):
    return type(n)
print(info_type(0))


#créer jeu de carte dans liste
paquet = [i +1 for i in range(52)]
print(paquet)


#somme de deux nombres
def somme(a,b):
    return a+b
print(somme(1,2))

#max d'une liste
listeneymar =[1,2,3,4]
def getMax(listeneymar):
    return max(listeneymar)
print(getMax(listeneymar))
    
#somme éléments d'une liste
def sommeL(l):
    return sum(l)
print(sommeL(listeneymar))

#minnimun d'une liste
def getMin(l):
    return min(l)

