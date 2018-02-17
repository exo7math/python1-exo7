
##############################
# Tant que - Booléen - Arithmétiques
##############################


##############################
# Activité 4 - Conjecture(s) de Goldbach
##############################

from math import *

##############################
# Rappel : activité 2

def est_premier(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n):
        d = d + 2

    if d ** 2 > n:
        return True    
    else:
        return False

##############################
##############################


##############################
## Question 1 ##

# La (vraie) conjecture de Goldbach (1742) : 
# tout entier pair plus grand que 3 est la somme de deux nombres premiers

def nombre_solutions_goldbach(n):
    """ Calcule le nb de décompositions n = p + q avec
    n pair ; p, q premiers et q >= p """

    # Si entier pas pair, c'est terminé
    if n % 2 == 1:
        print("Attention ! Entier non pair.")
        return None

    nb_sol = 0

    for p in range(2,n//2+1):
        q = n - p
        if (q>=p) and (est_premier(p)) and (est_premier(q)):
            print("n =",n,"somme de p =",p,", q = ",q)
            nb_sol = nb_sol + 1

    return nb_sol


# Test    
print("--- Conjecture de Goldbach ---")
print(nombre_solutions_goldbach(100))

def test_conjecture_goldbach(nmax):
    """ Vérifie la validité de la conjecture de Goldbach
    pour les entiers pairs de 4 jusqu'à nmax """

    print("Début du test")
    for n in range(4,nmax,2):
        if nombre_solutions_goldbach(n) == 0:
            print("Problème avec n = ",n)
    print("Fin du test")
    return


# Test    
print("--- Conjecture de Goldbach ---")
# test_conjecture_goldbach(10000)


##############################
## Question 2 ##

# Goldbach 1752 : 
# tout entier impair n peut s'écrire sous la forme
# n = p + 2k^2
# avec p premier et k entier (éventuellement nul)

def existe_decomposition_goldbach(n):
    """ Teste si n impair peut se décomposer n = p + 2k^2
    avec p premier et k entier """

    maxk = ceil(sqrt(n/2))+1
    for k in range(maxk):
        p = n - 2 * k**2
        if est_premier(p):
            # print(n,p,k,n-p-2*k**2)
            return True    
    return False


def contre_exemple_goldbach(nmax):
    """ Cherche un contre-exemple à la seconde conjecture de Goldbach """
    print("--- Début de la recherche ---")
    for m in range(1,nmax):
        n = 2 * m + 1
        if existe_decomposition_goldbach(n) == False:
            print("Contre-exemple :",n)

    print("--- Fin de la recherche ---")
    return

# Test 
print("--- Test conjecture fausse de Goldbach ---")
print("Avec 5777 : ",existe_decomposition_goldbach(5777))
contre_exemple_goldbach(10000)



