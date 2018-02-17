
##############################
# Statistique - Visualisation de données - tkinter
##############################


##############################
# Activité 1 - Calculs statistiques
##############################

from math import *

##################################################
## Question 1 ##

def somme(liste):
    """ Calcule la somme des éléments
    Entrée : une liste de nombres
    Sortie : leur somme """    

    som = 0
    for x in liste:
        som = som + x
    return som


# Test 
print("--- Somme ---")
liste = [5,18,6,3]
print(liste)
print(somme(liste))
print(sum(liste))


##################################################
## Question 2 ##

def moyenne(liste):
    """ Calcule la moyenne des éléments
    Entrée : une liste de nombres
    Sortie : leur moyenne """    
    
    nbliste = len(liste)

    if nbliste == 0:
        moy = 0
    else:
        moy = somme(liste) / nbliste 

    return moy


# Test 
print("--- Moyenne ---")
liste = [5,18,6,3]
print(liste)
print(moyenne(liste))



##################################################
## Question 3 ##

def minimum(liste):
    """ Calcule le minimum des éléments
    Entrée : une liste de nombres
    Sortie : leur minimum """    
    
    if len(liste) == 0:
        return None

    mini = liste[0]
    for i in range(1,len(liste)):
        if liste[i] < mini:
            mini = liste[i]

    return mini


# Test 
print("--- Minimum ---")
liste = [6,8,2,10]
print(liste)
print(minimum(liste))
print(min(liste))


##################################################
def maximum(liste):
    """ Calcule le maximum des éléments
    Entrée : une liste de nombres
    Sortie : leur maximum """    
    
    if len(liste) == 0:
        return None

    maxi = liste[0]
    for i in range(1,len(liste)):
        if liste[i] > maxi:
            maxi = liste[i]

    return maxi


# Test 
print("--- Maximum ---")
liste = [6,8,2,10]
print(liste)
print(maximum(liste))
print(max(liste))



##################################################
## Question 4 ##

def variance(liste):
    """ Calcule la variance des éléments
    Entrée : une liste de nombres
    Sortie : leur variance """    

    if len(liste) == 0:
        return 0
 
    moy = moyenne(liste)

    somme_carres = 0
    for x in liste:
        somme_carres = somme_carres + (x-moy)**2
    
    var = somme_carres / len(liste)

    return var


# Test 
print("--- Variance ---")
liste = [6,8,2,10]
print(liste)
print(variance(liste))


##################################################
## Question 5 ##

def ecart_type(liste):
    """ Calcule l'écart-type des éléments
    Entrée : une liste de nombres
    Sortie : leur écart-type """    

    eca = sqrt(variance(liste))

    return eca


# Test 
print("--- Ecart-type ---")
liste = [6,8,2,10]
print(liste)
print(ecart_type(liste))


##################################################
## Question 6 ##


temp_brest = [6.4,6.5,8.5,9.7,11.9,14.6,15.9,16.3,15.1,12.2,9.2,7.1]
temp_strasbourg = [0.9,2.4,6.1,9.7,13.8,17.2,19.2,18.6,15.7,10.7,5.3,2.1]


print(moyenne(temp_brest))
print(moyenne(temp_strasbourg))
print(ecart_type(temp_brest))
print(ecart_type(temp_strasbourg))

