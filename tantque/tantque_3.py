
##############################
# Tant que - Booléen - Arithmétiques
##############################


##############################
# Activité 3 - Diviseur, nombres premiers - Boucle while (suite)
##############################


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

def nombre_premier_apres(n):
    """ Cherche le prochain nombre premier après n """
    p = n
    while not est_premier(p):
        p = p + 1
    return p


# Test        
print("--- Premier nombre premier après un entier ---")
print(nombre_premier_apres(60))
print(nombre_premier_apres(100000))


##############################
## Question 2 ##

def nombres_jumeaux_apres(n):
    """ Trouve deux nombre premiers jumeaux après n """
    p = n
    q = p + 2
    while (not est_premier(p)) or (not est_premier(q)):
        p = p + 1
        q = p + 2
    return p,q


# Test    
print("--- Premiers nombres jumeaux après un entier ---")
print(nombres_jumeaux_apres(60))
print(nombres_jumeaux_apres(100000))


##############################
## Question 3 ##

def nombre_germain_apres(n):
    """ Trouve deux nombre premiers de Germain après n """
    p = n
    q = 2*p + 1
    while (not est_premier(p)) or (not est_premier(q)):
        p = p + 1
        q = 2*p + 1
    return p,q


# Test    
print("--- Premiers nombres premiers de Germain après un entier ---")
print(nombre_germain_apres(60))
print(nombre_germain_apres(100000))


