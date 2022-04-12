fic = open("notes.txt", "r")
fic2 = open("moyenne", "w")
for ligne in fic :
    l = ligne.split()
    moyenne = int((int(l[1]) + int(l[2]) + int(l[3])) / 3)
    l.append(moyenne)
    for i in range(len(l)):
        fic2.write(str(l[i])+" ")
    fic2.write("\n")
fic.close()
fic2.close()