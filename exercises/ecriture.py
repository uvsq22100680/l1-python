fic=open("result.txt", "w")
for i in range(4):
    fic.write(str(i))

ligne = fic.readline()
val = ligne.split()

print(val[0])
fic.close()
