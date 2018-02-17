def calcul_min(liste):
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


def calcul_max(liste):
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
liste = [6,8,2,10]
print("--- Minimim --- Maximum ---")
print(liste)
print(calcul_min(liste))
print(min(liste))
print(calcul_max(liste))
print(max(liste))
