
##############################
# Binaire - partie II
##############################

from binaire_I import *

##############################
# Activité 1 - Palindrome en binaire
##############################

## Question 1 ##

def est_palindrome_1(liste):

    p = len(liste)

    drapeau = True
    for i in range(p):
        if liste[i] != liste[p-1-i]:
            drapeau =  False

    return drapeau

# Version optimisée :
def est_palindrome_1_bis(liste):

    p = len(liste)

    for i in range(p//2):
        if liste[i] != liste[p-1-i]:
            return False

    return True


def est_palindrome_2(liste):
    liste_inverse = list(reversed(liste))
    return liste == liste_inverse


# Test 
print("--- Test d'un palindrome ---")
liste = [1,0,1,0,0,1,0,1]
print(est_palindrome_1(liste))
print(est_palindrome_1_bis(liste))
print(est_palindrome_2(liste))



## Question 2 ##


def cherche_palindrome_binaire(N):
    num = 0
    for n in range(N):
        liste_binaire = entier_vers_binaire(n)
        if est_palindrome_1(liste_binaire) == True:
            num = num + 1
            print(num,":",n,"=",entier_vers_binaire(n))
    return

# Test
print("--- Palindromes binaires ---")
cherche_palindrome_binaire(1000)

# Le 1000ème palindrome en binaire est :
#249903 = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]

## Question 3 ##

def cherche_palindrome_decimale(N):
    num = 0
    for n in range(N):
        liste_decimale = entier_vers_decimale(n)
        if est_palindrome_1(liste_decimale) == True:
            num = num + 1
            print(num,":",n)
    return

# Test
print("--- Palindromes avec décimales ---")
cherche_palindrome_decimale(1000)

# Le 1000ème palindrome en décimales est :
# 90009

## Question 4 ##

def cherche_bi_palindrome(N):
    num = 0
    for n in range(N):
        liste_binaire = entier_vers_binaire(n)        
        liste_decimale = entier_vers_decimale(n)
        if est_palindrome_1(liste_binaire) == True and est_palindrome_1(liste_decimale):
            num = num + 1
            print(num,":",n,"=",entier_vers_binaire(n))
    return

# Test
print("--- Bi-palindromes ---")
cherche_bi_palindrome(1000)

# Le 20ème bi-palindrome est 
#  585585 = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1]




##############################
# Activité 2 - Opérations logiques
##############################

## Question 1 ##

def OUeg(l1,l2):
    n = len(l1)    
    l = []
    for i in range(n):
        if l1[i]==1 or l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]

    return l


def ETeg(l1,l2):
    n = len(l1)
    l = []
    for i in range(n):
        if l1[i]==1 and l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]
    return l


def NON(l1):
    l = []
    for b in l1:
        if b==1:
            l = l + [0]
        else:
            l = l + [1]
    return l

# Test   
print("--- Opérations logiques (même longueur) ---")
l1 = [1,0,1,0,1,0,1]
l2 = [1,0,0,1,0,0,1]
print(l1)
print(l2)
print(OUeg(l1,l2))
print(ETeg(l1,l2))
print(NON(l1))


## Question 2 ##


# Rajouter des zéros non significatifs si besoins

def ajouter_zeros(liste,p):
    while len(liste)< p:
        liste = [0] + liste

    return liste

# Test 
print("--- Zeros non significatifs ---")
print(ajouter_zeros([1,0,1,1],8))


## Question 3 ##

# Opérations logiques avec des listes de tailles différentes

def OU(l1,l2):
    p = len(l1)
    q = len(l2)
    if p>q:
        ll2 = ajouter_zeros(l2,p)   
        return OUeg(l1,ll2)
    else:
        ll1 = ajouter_zeros(l1,q)
        return OUeg(ll1,l2)


def ET(l1,l2):
    p = len(l1)
    q = len(l2)
    if p>q:
        ll2 = ajouter_zeros(l2,p)   
        return ETeg(l1,ll2)
    else:
        ll1 = ajouter_zeros(l1,q)
        return ETeg(ll1,l2)


# Test   
print("--- Opérations logiques (cas général) ---")
l1 = [1,0,1,0,1,0,1]
l2 = [1,0,0,1,0,]
print(l1)
print(l2)
print(OU(l1,l2))
print(ET(l1,l2))


##############################
# Activité 3 - Loi de Morgan
##############################

## Question 1 ##

def tous_les_binaires(p):
          
    liste_p = []
    for n in range(2**p):
        liste_p = liste_p + [entier_vers_binaire(n)]
    return liste_p


# Test 
print("--- Tous les binaires ---")
print(tous_les_binaires(3))


## Question 2 ##

def toutes_les_listes(p):
    if p == 0: 
      return []
    if p == 1: 
      return [[0],[1]]  

    liste_p_1 = toutes_les_listes(p-1)

    liste_p = [ [0] + l for l in liste_p_1] + [ [1] + l for l in liste_p_1]

    return liste_p

# Test 
print("--- Toutes les listes ---")
print(toutes_les_listes(3))



## Question 3 ##

# Lois de Morgan


def test_loi_de_morgan(p):
    liste_tous = [ajouter_zeros(l,p) for l in tous_les_binaires(p)]
    #liste_tous = toutes_les_listes(p)    
    for l1 in liste_tous:
        for l2 in liste_tous:
            non_l1_ou_l2 = NON(OU(l1,l2))
            non_l1_et_non_l2 = ET(NON(l1),NON(l2))
            if non_l1_ou_l2 == non_l1_et_non_l2:
                print("Vrai")
                # pass
            else:
                print("Faux",l1,l2)

    return

# Test
print("--- Test loi de Morgan ---")
test_loi_de_morgan(2)

