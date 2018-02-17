def pile_contient(element):
    """  Détermine si la pile contient l'élément
    Entrée : rien
    Sortie : vrai/faux
    Action : modifie la pile """
    
    while not pile_est_vide():
        el = depile()
        if el == element:
            return True    # Si on trouve l'élément c'est bon

    return False     # On arrive au bas sans trouver l'élément


# Tests
print("--- Test si pile contient 7 ---")

# Test 1
pile = [4,5,6]
print(pile,'pile contient 7 ?',pile_contient(7))

# Test 2
pile = [4,7,12,99]
print(pile,'pile contient 7 ? ',pile_contient(7))