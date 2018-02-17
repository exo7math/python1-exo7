
##############################
# Listes II
##############################

##############################
# Activité 3 - Tableau à deux dimensions
##############################


## Question 1 ##

##############################
def somme_diagonale(tableau):
    n = len(tableau)
    somme = 0
    for i in range(n):
        somme = somme + tableau[i][i]
    return somme


## Question 2 ##

##############################
def somme_anti_diagonale(tableau):
    n = len(tableau)
    somme = 0
    for i in range(n):
        somme = somme + tableau[n-1-i][i]
    return somme


## Question 3 ##

##############################
def somme_tout(tableau):
    n = len(tableau)    
    somme = 0
    for i in range(n):
        for j in range(n):
            somme = somme + tableau[i][i]
    return somme


## Question 4 ##

##############################
def affiche_tableau(tableau):
    """
    Affiche un tableau carré à l'écran
    Entrée : un tableau de taille n x n
    Sortie : rien (affichage à l'écran)
    """    
    
    n = len(tableau)
    for i in range(n):
        for j in range(n):
            print('{:>3d}'.format(tableau[i][j]),end="")
        print()
    return




##############################
tableau = [ [1,2,3], [4,5,6], [7,8,9] ]

print("--- Somme diagonale ---")
print(somme_diagonale(tableau))

print("--- Somme anti-diagonale ---")
print(somme_anti_diagonale(tableau))

print("--- Somme tout ---")
print(somme_tout(tableau))

print("--- Affichage ---")
affiche_tableau(tableau)

