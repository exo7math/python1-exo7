# "pile" est une variable globale

def empile(element):
    """  Ajoute un élément au sommet de la pile
    Entrée : un objet
    Sortie : rien
    Action : la pile contient un élément en plus """

    global pile     # Pour pouvoir modifier la pile

    pile = pile + [element]

    return None


# Test
print("--- Empiler ---")
pile = [4,5,6]
print('Pile avant :',pile)
empile(7)
print('Pile après :',pile)