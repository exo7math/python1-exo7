
##############################
# Tant que - Booléen - Arithmétiques
##############################


##############################
# Activité 2 - Diviseur, nombres premiers - Boucle while
##############################


##############################
## Question 1 ##

def plus_petit_diviseur(n):
    """ Cherche le plus petit diviseur de n """
    d = 2
    while n % d != 0:
        d = d + 1
    return d


# Test 
print("--- Plus petit diviseur ---")
print(plus_petit_diviseur(7*13))


##############################
## Question 2 ##

def est_premier_1(n):
    """ Teste si n est un nombre premier """

    d = 2    

    while n % d != 0:
        d = d + 1

    if d == n:
        return True    
    else:
        return False


# Test        
print("--- Est premier (1) ---")
print(est_premier_1(97))


##############################
## Question 3 ##

# Nombre de Fermat

def contre_exemple_fermat():
    for n in range(6): 
        fermat = 2**(2**n)+1
        print(n,fermat,est_premier_1(fermat))
    return  

# Test 
print("--- Test conjecture nombres de Fermat ---")
contre_exemple_fermat()


##############################
## Question 4 ##

def est_premier_2(n):
    """ Teste si n est un nombre premier """

    if n < 2:
        return False

    d = 2    

    while (n % d != 0) and (d**2 <= n):
        d = d + 1

    if d** 2 > n:
        return True    
    else:
        return False


# Test        
print("--- Est premier (2) ---")
print(est_premier_2(97))


##############################
## Question 4 ##


def est_premier_3(n):
    """ Teste si n est un nombre premier """

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


 # Test        
print("--- Est premier (3) ---")
print(est_premier_3(97))
       

##############################

## Question 5 ##

# Calcul les temps d'éxécution moyens des différents fonction est_premier()

import timeit
print(timeit.timeit("est_premier_1(97)", setup="from __main__ import est_premier_1", number=10000))
print(timeit.timeit("est_premier_2(97)", setup="from __main__ import est_premier_2", number=10000))
print(timeit.timeit("est_premier_3(97)", setup="from __main__ import est_premier_3", number=10000))


##############################
# On garde la plus efficace !

def est_premier(n):
    return est_premier_3(n)