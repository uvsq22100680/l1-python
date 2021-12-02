def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste =[]
    
    while n != 1 :
        if n %2==0:
            n=n//2
            print(n)
            liste.append(n)
        else: 
            n=3*n+1
            print(n)
            liste.append(n)
            
    
    return liste

print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    a = syracuse(n_max)
    if 1 in a :
        return True    
    
        
print(testeConjecture(10000))


