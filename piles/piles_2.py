
##############################
# Piles - Calculatrice polonaise
##############################

##############################
# Rappels - Activité 1
##############################

def empile(element):
    global pile
    pile = pile + [element]
    return None

def depile():
    global pile
    sommet = pile[len(pile)-1]
    pile = pile[0:len(pile)-1]
    return sommet   

def pile_est_vide():
    if len(pile) == 0:
        return True
    else:
        return False

##############################
# Activité 2 - Manipulation de la pile
##############################

## Question 1 ##

print("--- Manipulation ---")
pile = []
empile(5)
empile(7)
empile(2)
empile(4)
print(pile)
depile()
empile(8)
empile(1)
empile(3)
print(pile)
val =  depile()
print('Valeur :',val)

## Question 2 ##

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


## Question 3 ##

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


## Question 4 ##

def avant_dernier():
    """ Renvoie l'avant-dernier élément en bas de la pile
    Entrée : rien
    Sortie : l'avant-dernier élément
    Action : vide la pile """
    
    dernier = None
    avant_dernier = None  

    while not pile_est_vide():
        avant_dernier = dernier  # Le dernier devient avant-dernier
        dernier = depile()       # Nouveau dernier
    
    return avant_dernier


# Tests
pile = [4,5,6,13]
print('L\'avant-dernier élément de',pile,'est',avant_dernier())

pile = [4,6]
print('L\'avant-dernier élément de',pile,'est',avant_dernier())

pile = [6]
print('L\'avant-dernier élément de',pile,'est',avant_dernier())

pile = []
print('L\'avant-dernier élément de',pile,'est',avant_dernier())

