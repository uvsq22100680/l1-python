liste = [1,2,30,4]
print(liste)
print(max(liste))

liste.append(3)
print(liste)

liste[4]=1
print(liste)

c = "attention"
print(c.upper())

print(c.split())
l2 = list(liste)
print(l2)
l1 = [1,2,"e"]

l2 = list(l1)
l2.append(2)
print(l1)
print(l2)


chaine ="jesuiofjhiurshfisf"
print(type(l1))
print("la variable contient", len(chaine),"éléments")
print()

liste = ["bus", "voiture", "vélo", "trotinette"]
print(liste)


text = ['Python', 'is', 'a', 'fun', 'programming', 'language']


print(' '.join(text))


s = [i for i in range(10)]
print(s)

t = [0] * 100
for i in range(100):
    if i%3:
        t[i] = i
    else:
        t[i] = -i
print(t[98], t[99])


print(((3*15)+(3*12)+(1*20)//7))