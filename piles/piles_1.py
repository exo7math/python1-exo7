
##############################
# Piles - Calculatrice polonaise
##############################


##############################
# Activité 1 - Opération sur la pile
##############################


# "pile" est une variable globale

## Question 1 ##

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


## Question 2 ##

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


## Question 3 ##

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

