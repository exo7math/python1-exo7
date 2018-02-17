def calcul_variance(liste):
    """ Calcule la variance des éléments
    Entrée : une liste de nombres
    Sortie : leur variance """    

    if len(liste) == 0:
        return 0
 
    moyenne = calcul_moyenne(liste)

    somme_carres = 0
    for x in liste:
        somme_carres = somme_carres + (x-moyenne)**2
    
    variance = somme_carres / len(liste)

    return variance

# Test 
liste = [6,8,2,10]
print("--- Variance ---")
print(liste)
print(calcul_variance(liste))