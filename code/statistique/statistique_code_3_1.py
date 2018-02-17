from math import *
from random import *

def calcul_mediane(liste):
    """ Calcule la médiane des éléments
    Entrée : une liste de nombre
    Sortie : leur médiane """        
    liste_triee = sorted(liste)

    n = len(liste_triee)

    if n%2 == 0:   # n est pair
        indice_milieu = n//2
        mediane = (liste_triee[indice_milieu-1]+liste_triee[indice_milieu]) / 2
    else: 
        indice_milieu = (n-1)//2 
        mediane = liste_triee[indice_milieu]

    return mediane

# Test 
print("--- Médiane ---")
liste = [5,18,6,3]
print(liste)
print(calcul_mediane(liste))