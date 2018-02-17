
##############################
# Listes II
##############################

from random import *


##############################
# Activité 2 - Somme fixée 
##############################

##############################


from random import *
liste_20 = [randint(1,99) for i in range(20)]
liste_20 = [16, 2, 85, 27, 9, 45, 98, 73, 12, 26, 46, 25, 26, 49, 18, 99, 10, 86, 7, 42]
print(liste_20)


liste_200 = [randint(1,99) for i in range(200)]
print(liste_200)

## Question 1 ##

##############################
# Trouver deux élément consécutifs dont la somme vaut 100

def somme_deux_consecutifs_100(liste):
    n = len(liste)
    for i in range(n-1):
        if liste[i]+liste[i+1] == 100:
            # print(i,i+1,liste[i],liste[i+1])
            return True
    return False


## Question 2 ##

##############################
# Trouver deux élément différents dont la somme vaut 100
def somme_deux_100(liste):
    n = len(liste)
    for i in range(n-1):
        for j in range(i+1,n):
            if liste[i]+liste[j] == 100:
                # print(i,j,liste[i],liste[j])
                return True
    return False


## Question 3 ##

##############################
# Suite de termes consécutifs qui font 100
def somme_suite_100(liste):
    n = len(liste)
    for i in range(n):
        somme = 0
        j = i
        while somme < 100 and j < n:
            somme = somme  + liste[j]
            j = j + 1
        if somme == 100:
            # print(i,j-1,liste[i:j])
            return True
    return False

##############################
print("--- Somme deux consécutifs ---")
print(somme_deux_consecutifs_100(liste_20))
print(somme_deux_consecutifs_100(liste_200))

print("--- Somme deux qcq ---")
print(somme_deux_100(liste_20))
print(somme_deux_100(liste_200))

print("--- Somme suites ---")
print(somme_suite_100(liste_20))
print(somme_suite_100(liste_200))

## Question 3 ##

##############################
# Idées proba : Quelle long donne prob > 1/2 

##############################
def proba_1(n,N):
    nb = 0
    for k in range(N):
        liste_n = liste_n = [randint(1,99) for i in range(n)]
        trouve = somme_deux_consecutifs_100(liste_n)
        if trouve:
            nb += 1
    return nb/N


##############################
def proba_2(n,N):
    nb = 0
    for k in range(N):
        liste_n = liste_n = [randint(1,99) for i in range(n)]
        trouve = somme_deux_100(liste_n)
        if trouve:
            nb += 1
    return nb/N


##############################
def proba_3(n,N):
    nb = 0
    for k in range(N):
        liste_n = liste_n = [randint(1,99) for i in range(n)]
        trouve = somme_suite_100(liste_n)
        if trouve:
            nb += 1
    return nb/N




print("--- Proba deux consécutifs ---")
# Proba ~ 1/2 pour longueur n ~ 67
print(proba_1(67,10000))

print("--- Proba deux ---")
# Proba ~ 1/2 pour longueur n ~ 12
print(proba_2(12,10000))

print("--- Proba suite ---")
# Proba ~ 1/2 pour longueur n ~ 42
print(proba_3(42,10000))