
##############################
# Tant que - Booléen - Arithmétiques
##############################

##############################
# Idées
##############################

from math import *

##############################
# Idées 1 - Divisibilité, quotient, reste
##############################

##############################
def est_paire(n):
    reste = n % 2
    if reste == 0:
        return True
    else:
        return False

def est_paire_bis(n):
    return n % 2 == 0


##############################
def quotient_reste(a,b):
    q = a // b
    r = a % b
    print("Division de a =",a,"par b =",b)
    print("Le quotient vaut : q =",q)
    print("Le reste vaut : r =",r)
    if a == b*q +r:
        verif = True
    else:
        verif = False
    print("Vérification ok ?",verif)

    return q,r


##############################
def divise(a,b):
    if a % b ==0:
        return True
    else:
        return False



##############################
# Idées 2 - Diviseur, nombres premiers - Boucle while
##############################


##############################

def plus_petit_diviseur(n):
    d = 2
    while n % d != 0:
        d = d + 1
    return d

# Test 
print("--- Plus petit diviseur ---")
print(plus_petit_diviseur(7*13))

##############################

def est_premier_1(n):
    d = 2    

    while n % d != 0:
        d = d + 1

    if d == n:
        return True    
    else:
        return False


def est_premier_2(n):
    if n < 2:
        return False
    d = 2    

    while (n % d != 0) and (d**2 <= n):
        d = d + 1

    if d** 2 > n:
        return True    
    else:
        return False

def est_premier(n):
    return est_premier_2(n)


# Test        
print("--- Est premier ---")
print(est_premier_1(65537))
print(est_premier_2(65537))

for n in range(65000,66000):
    if est_premier_1(n) != est_premier_2(n):
        print("Problème avec n=",n)


##############################
import timeit
print(timeit.timeit("est_premier_1(97)", setup="from __main__ import est_premier_1", number=10000))
print(timeit.timeit("est_premier_2(97)", setup="from __main__ import est_premier_2", number=10000))


##############################
def premier_premier_apres(n):
    p = n
    while not est_premier(p):
        p = p + 1
    return p

# Test        
print("--- Premier nombre premier après un entier ---")
print(premier_premier_apres(1000))


##############################
def premiers_jumeaux_apres(n):
    p = n
    q = p + 2
    while (not est_premier(p)) or (not est_premier(q)):
        p = p + 1
        q = p + 2
    return p,q


# Test    
print("--- Premiers nombres jumeaux après un entier ---")
print(premiers_jumeaux_apres(1000))


##############################
def premiers_germains_apres(n):
    p = n
    q = 2*p + 1
    while (not est_premier(p)) or (not est_premier(q)):
        p = p + 1
        q = 2*p + 1
    return p,q


# Test    
print("--- Premiers nombres de Germain après un entier ---")
print(premiers_germains_apres(1000))



##############################
# Idées 3 - Conjecture de Goldbach
##############################


# Conjecture de Goldbach : 
# tout entier pair plus grand que 3 est la somme de deux nombres premiers


def nombre_solutions_goldbach(n):
    # Si entier pas pair, c'est terminé
    if n % 2 == 1:
        print("Attention ! Entier non pair.")
        return None

    nb_sol = 0

    for p in range(2,n//2+1):
        q = n - p
        if (q>p) and (est_premier(p)) and (est_premier(q)):
            print("n =",n,"somme de p =",p,", q = ",q)
            nb_sol = nb_sol + 1

    return nb_sol


# Test    
print("--- Conjecture de Goldbach ---")
print(nombre_solutions_goldbach(100))



##############################
# Idées 4 - Conjectures fausses
##############################

##############################
# Nombre de Fermat:


def contre_exemple_fermat():
    for n in range(6): 
        fermat = 2**(2**n)+1
        print(n,fermat,est_premier(fermat))
    return
# Test 
print("--- Test conjecture nombres de Fermat ---")
contre_exemple_fermat()




##############################

# Nombre d'entiers ayant 4 diviseurs par rapport à 8 diviseurs


def nombre_de_diviseurs_1(n):
    nb = 0
    for d in range(1,n+1):
        if n % d == 0:
            nb = nb + 1
    return nb

def nombre_de_diviseurs_2(n):
    nb = 2  # on compte déjà 1 et n
    for d in range(2,n//2+1):
        if n % d == 0:
            nb = nb + 1
    return nb

def nombre_de_diviseurs(n):
    return nombre_de_diviseurs_2(n)


def quatre_et_huit_diviseurs(nmin,nmax):
    nb_quatre = 0 
    nb_huit = 0
    for n in range(nmin,nmax):
        nb = nombre_de_diviseurs(n)
        if nb == 4:
            nb_quatre = nb_quatre + 1
        elif nb == 8:
            nb_huit = nb_huit + 1
    return nb_quatre, nb_huit


# Test 
print("--- Nombre de diviseurs ---")
print(nombre_de_diviseurs(100))
print(quatre_et_huit_diviseurs(1,100))
# print(quatre_et_huit_diviseurs(1,50000))
# print(quatre_et_huit_diviseurs(50000,100000))
# print(quatre_et_huit_diviseurs(100000,150000))
# print(quatre_et_huit_diviseurs(150000,200000))
#print(quatre_et_huit_diviseurs(200000,250000))


# Par tranche de 50 000
# T1 : 12073, 10957
# T2 : 11254, 11224
# T3 : 10995, 11229
# T4 : 10838, 11218
# T5 : 10690, 11260

# 4 diviseurs 12073+11254+10995+10838+10690   = 55850
# 8 diviseurs 10957+11224+11229+11218+11260   = 55888


##############################
# Goldbach 1752 : 
# tout entier impair n peut s'écrire sous la forme
# n = p + 2k^2
# avec p premier et k entier (éventuellement nul)

def test_conj_goldbach(n):
    maxk = ceil(sqrt(n/2))+1
    for k in range(maxk):
        p = n - 2 * k**2
        if est_premier(p):
            # print(n,p,k,n-p-2*k**2)
            return True    

    return False


def contre_exemple_goldbach(nmax):
    print("--- Début de la recherche ---")
    for m in range(1,nmax):
        n = 2 * m + 1
        if test_conj_goldbach(n) == False:
            print("Contre-exemple :",n)

    print("--- Fin de la recherche ---")
    return

# Test 
print("--- Test conj fausse Goldbach ---")
# for m in range(1,10):
#     test_conj_1(2*m+1)

print("cex",test_conj_goldbach(5777))
contre_exemple_goldbach(10000)


##############################
# Idées 5 - Conjectures fausses
##############################

##############################
# Conjecture 1211111... n'est jamais premier

def test_un_deux_un(kmax):
    n = 12
    for k in range(kmax):
        print(n,est_premier(n))
        n = 10*n + 1
    return

    # Test 
print("--- Test conj 121111.... jamais premier ---")

# N'aboutira pas
test_un_deux_un(10)


##############################
def est_presque_premier(n,k):
    if n < 2:
        return False
    d = 2    

    while (n % d != 0) and (d <= k):
        d = d + 1

    if d > k:
        return True    
    else:
        return False

def test_presque_un_deux_un(kmax):
    n = 12
    for k in range(kmax):
        if est_presque_premier(n,100000):
            print(k,'Presque premier',n)
        n = 10*n + 1
    return

    # Test 
print("--- Test conj 121111.... jamais presque premier ---")

# N'aboutira pas
test_presque_un_deux_un(10)