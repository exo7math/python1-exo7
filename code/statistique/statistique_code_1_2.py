def calcul_moyenne(liste):
    """ Calcule la moyenne des éléments
    Entrée : une liste de nombres
    Sortie : leur moyenne """    
    
    nbliste = len(liste)

    if nbliste == 0:
        moyenne = 0
    else:
        moyenne = calcul_somme(liste) / nbliste 

    return moyenne

# Test 
liste = [5,18,6,3]
print("--- Moyenne ---")
print(liste)
print(calcul_moyenne(liste))