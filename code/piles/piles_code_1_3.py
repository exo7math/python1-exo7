def pile_est_vide():
    """ Détermine si la pile est vide ou pas
    Entrée : rien
    Sortie : vrai/faux
    Action : ne modifie pas la pile """

    if len(pile) == 0:
        return True
    else:
        return False


# Tests
print("--- Tester si pile vide ---")

# Test 1
pile = [4,5,6]
vide = pile_est_vide()
print(pile,'pile vide ?',vide)

# Test 2
pile = []
vide = pile_est_vide()
print(pile,'pile vide ?',vide)