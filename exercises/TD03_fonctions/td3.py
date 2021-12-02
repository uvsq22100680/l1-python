#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
import time
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    temps = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3] * 1
    return temps
    
temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // 86400
    reste = seconde % 86400
    
    heures = reste // 3600
    reste = reste % 3600
    
    minutes = reste // 60
    seconde_reste = reste % 60

    return(jours, heures, minutes ,seconde_reste)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici



def afficheTemps(temps):
    if temps[0]> 1 :
        print(temps[0], "jours")
    else:
        print(temps[0], "jour")
    if temps[1]> 1 :
        print(temps[1], "heures")
    else:
        print(temps[1], "heure")
    if temps[2]> 1 :
        print(temps[2], "minutes")
    else:
        print(temps[2], "minute")
    if temps[3]> 1 :
        print(temps[3], "secondes")
    else:
        print(temps[3], "seconde")

afficheTemps((1,0,14,23))  

def demandeTemps():
    global temps
    
    temps = [int(input("jours")), int(input("heure")), int(input("minutes")) ,int(input("seconde"))]

    return(temps)

def sommeTemps(temps1,temps2):
    jours = temps[0] + temps[0]
    heures = temps[1] + temps[1]
    minutes = temps[2]+ temps[2]
    secondes = temps[3] + temps[3]
    somme = jours + heures + minutes + secondes
    return(somme)
sommeTemps((2,3,4,25),(5,22,57,1))

def tempsEnDate(temps):
    annee = 1970 + temps[0] // 365
    numero_jour = 1 + temps[0] % 365
    return(annee, numero_jour, temps[1], temps[2], temps[3])

def afficheDate(date = -1):
    #paramètre date est optionnel, considère que la date vaut -1 si affichedate() n'a pas de paramètre
    if date == -1:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("jour", date[1], "de l'année", date[0], "à", date[2], date[3], date[4])
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

def bisextile(jour):
    annee = 1970
    compteur = 0
    while jour > 365 :
        if annee % 4 == 0 and  annee % 100 != 0 or annee % 400 == 0:
            jour -= 366
            compteur +=1
        else:
            jour -= 365
        annee += 1
    return compteur
        
bisextile(20000)

def nombreBisextile(jour):
    pass

def tempsEnDateBisextile(temps):
    jours = temps[0]
    jours = jours - nombreBisextile(jours)
    return tempsEnDate((jours, temps[1], temps[2], temps[3]))
   
temps = ((1000000000))
afficheDate(tempsEnDateBisextile(temps))