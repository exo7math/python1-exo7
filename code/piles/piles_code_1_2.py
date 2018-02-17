def depile():
    """ Lit l'élément au sommet de la pile et l'enlève
    Entrée : rien
    Sortie : l'élément du sommet
    Action : la pile contient un élément de moins """

    global pile

    sommet = pile[len(pile)-1]
    pile = pile[0:len(pile)-1]

    return sommet


# Test
print("--- Dépiler ---")
pile = [4,5,6]
print('Pile avant :',pile)
val = depile()
print('Valeur dépilée :',val,'\nPile après :',pile)