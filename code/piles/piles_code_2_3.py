def somme_pile():
    """ Calcule la somme de la pile
    Entrée : rien
    Sortie : la somme
    Action : vide la pile """
    
    somme = 0
    while not pile_est_vide():
        element = depile()
        somme = somme + element

    return somme


# Test
print("--- Somme des valeurs de la pile ---")
pile = [4,5,6]
print('La somme de',pile,'est ',somme_pile())