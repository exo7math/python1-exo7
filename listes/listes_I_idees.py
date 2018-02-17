
##############################
# Listes I - Idées
##############################


##############################
# Cours 1

maliste = [11,13,17,19]
maliste.append(23)
maliste.append(29)
print(maliste[5])


##############################
# Activité 1 - Intérêts
##############################

## Question 1 ##

##############################
def interets_simples(S0,p,n):
    liste = [S0]
    interets = S0 * p/100
    S = S0
    for i in range(n):
        S = S + interets
        liste.append(S)
    return liste


# Test
print("--- Intérêts simples ---")
liste_interets_simples = interets_simples(1000,10,12)
print(liste_interets_simples)
print(liste_interets_simples[11])



## Question 2 ##

##############################
def interets_composes(S0,p,n):
    liste = [S0]
    S = S0
    for i in range(n):
        interets = S * p/100
        S = S + interets
        liste.append(S)
    return liste


# Test
print("--- Intérêts composés ---")
liste_interets_composes = interets_composes(1000,7,12)
print(liste_interets_composes)
print(liste_interets_composes[11])

liste_interets_composes = interets_composes(1000,10,3)
print(liste_interets_composes)

##############################
# Cours 2

maliste = []
maliste = maliste + ["Un"]
maliste = ["Deux"] + maliste
len(maliste)
maliste[1:5]


##############################
# Activité 2 - Manipulation
##############################

## Question 1 ##

##############################
def rotation(liste):
    n = len(liste)
    new_liste = [liste[n-1]] + liste[0:n-1]
    return new_liste

# Test
print("--- Rotation ---")
print(rotation([1,2,3,4]))


## Question 2 ##

##############################
def inverser(liste):
    new_liste = []
    for element in liste:
        new_liste = [element] + new_liste
    return new_liste

# Test
print("--- Inverse ---")
print(inverser([1,2,3,4]))


## Question 3 ##

##############################
def supprimer_rang(liste,rang):
    n = len(liste)
    new_liste = liste[0:rang]+liste[rang+1:n]
    return new_liste

# Test
print("--- Supprimer rang ---")
print(supprimer_rang([8,7,6,5,4],2))

## Question 4 ##

##############################
def supprimer_element(liste,element):
    new_liste = []
    for x in liste:
        if x != element:
            new_liste = new_liste + [x]
    return new_liste

# Test
print("--- Supprimer élément ---")
print(supprimer_element([8,7,4,6,5,4],4))


# Autre idées utiliser remove()
print("--- remove() ---")
liste = [2,5,3,8,5]
print(liste)
liste.remove(5)
print(liste)
liste.remove(5)
print(liste)


# Voir aussi "del"


##############################
# Cours 3 - Tri à bulles

maliste = []
maliste = maliste + ["Un"]
maliste = ["Deux"] + maliste
len(maliste)
maliste[1:5]


##############################
# Activité 3 - Tri à bulle
##############################

def trier(liste):
    n = len(liste)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if liste[j+1] < liste[j]:
                el = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = el


    return liste

# Test
print("--- Tri à bulles ---")
print(trier([13,11,7,4,6,8,12,6]))


##############################
# Activité 4 - Arithmétique
##############################

## Question 1 ##

##############################
def facteurs_premiers(n):
    liste = []
    d = 2
    while d <= n:
        if n%d == 0:
            liste = liste + [d]
            n = n // d
        else:
            d = d + 1
    # if len(liste)==0:   # Cas d'un nb premier
    #     liste = [n]
    return liste


# Test
print("--- Facteurs premiers ---")
n = 2*2*2*3*7*7*11
print(n)
print(facteurs_premiers(2*2*2*3*7*7*11))


## Question 2 ##

##############################
def liste_premiers(n):
    liste = list(range(2,n))
    for d in range(2,n):
        for k in liste:
            if k%d == 0 and k != d:
                liste.remove(k)
    return liste

print("--- Liste des nombres premiers ---")
print(liste_premiers(100))


##############################
# Cours 4 - Visualiser une liste

import matplotlib.pyplot as plt

liste1 = [3,5,9,8,0,3]
liste2 = [4,7,7,2,8,9]
plt.plot(liste1,color="red")
plt.plot(liste2,color="blue")
plt.grid()
plt.show()



##############################
# Activité 5 - Tir balistique
##############################

import matplotlib.pyplot as plt
from math import *

def tir_parabolique(x,v,alpha):
    g = 9.81
    alpha = 2*pi/360*alpha  # angle en radians
    y = -1/2 * g / (v * cos(alpha))**2 * x**2  +  tan(alpha) * x
    return y

def liste_trajectoire(xmax,n,v,alpha):
    liste = []
    epsilon = xmax/n
    for i in range(n+1):
        x = i * xmax/n  
        y = tir_parabolique(x,v,alpha)
        liste.append(y)
    return liste

tir30 = liste_trajectoire(270,100,50,30)
tir45 = liste_trajectoire(270,100,50,45)
tir60 = liste_trajectoire(270,100,50,60)
plt.plot(tir30,color="blue")
plt.plot(tir45,color="red")
plt.plot(tir60,color="green")
plt.grid()
plt.show()
