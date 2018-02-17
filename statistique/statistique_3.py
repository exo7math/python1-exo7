##############################
# Statistique - Visualisation de données - tkinter
##############################


##############################
# Activité 3 - Calculs statistiques (bis)
##############################


##################################################
## Question 1 ##

from math import *
from random import *

def mediane(liste):
    """ Calcule la médiane des éléments
    Entrée : une liste de nombre
    Sortie : leur médiane """        
    liste_triee = sorted(liste)

    n = len(liste_triee)

    if n%2 == 0:   # n est pair
        indice_milieu = n//2
        med = (liste_triee[indice_milieu-1]+liste_triee[indice_milieu]) / 2
    else: 
        indice_milieu = (n-1)//2 
        med = liste_triee[indice_milieu]

    return med


# Test 
print("--- Médiane ---")
liste = [5,18,6,3]
print(liste)
print(mediane(liste))



##################################################
## Question 2 ##

def notes_vers_liste(effectif_notes):
    """ Convertit un effectif de notes en une liste de notes
    Entrée : une liste d'effectif de notes
    Sortie : la liste des notes """        
    liste = []
    for i in range(len(effectif_notes)):
        nb = effectif_notes[i]
        liste = liste + [i]*nb

    return liste


# Test 
print("--- Liste à partir d'un effectif ---")
effectif_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
# effectif_notes = [randint(1,5) for i in range(21)]
print(effectif_notes)
print(notes_vers_liste(effectif_notes))

def mediane_notes(effectif_notes):
    """ Calcule la médiane des notes
    Entrée : une liste d'effectif de notes
    Sortie : la médiane """   
    liste = notes_vers_liste(effectif_notes)
    med = mediane(liste)

    return med


# Test 
print("--- Médiane des notes ---")
effectif_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
print(effectif_notes)
print(mediane_notes(effectif_notes))



##################################################
## Question 3 ##

def calcule_quartiles(liste):
    """ Calcule les quartiles de la liste
    Entrée : une liste de nombre
    Sortie : leur quartile Q1, Q2=med, Q3 """        
    med = mediane(liste)

    liste_triee = sorted(liste)
    n = len(liste_triee)
    indice_milieu = n//2
    if n%2 == 0: # si n pair
        liste_inf = liste[:indice_milieu]
        liste_sup = liste[indice_milieu:]
    else: # n impair
        liste_inf = liste[:indice_milieu+1]
        liste_sup = liste[indice_milieu:]    
    Q1 =  mediane(liste_inf)
    Q3 =  mediane(liste_sup)

    return Q1, med, Q3


# Test 
print("--- Quartiles ---")
liste = [3,4,5,7,12,50,100]
print(liste)
print(calcule_quartiles(liste))


##################################################
def quartiles_notes(effectif_notes):
    """ Calcule les quartiles des notes
    Entrée : une liste d'effectif de notes
    Sortie : les quartiles """   
    liste = notes_vers_liste(effectif_notes)
    Q1,Q2,Q3 = calcule_quartiles(liste)

    return Q1, Q2, Q3


# Test 
print("--- Quartiles des notes ---")
effectif_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
print(effectif_notes)
print(quartiles_notes(effectif_notes))