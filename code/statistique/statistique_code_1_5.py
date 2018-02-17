def calcul_ecart_type(liste):
    """ Calcule l'écart-type des éléments
    Entrée : une liste de nombres
    Sortie : leur écart-type """    

    ecart_type = sqrt(calcul_variance(liste))

    return ecart_type


# Test 
print("--- Ecart-type ---")
liste = [6,8,2,10]
print(liste)
print(calcul_ecart_type(liste))