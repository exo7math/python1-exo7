def calcul_somme(liste):
    """ Calcule la somme des éléments
    Entrée : une liste de nombres
    Sortie : leur somme """    

    somme = 0
    for x in liste:
        somme = somme + x
    return somme

# Test 
liste = [5,18,6,3]
print("--- Somme ---")
print(liste)
print(calcul_somme(liste))
print(sum(liste))