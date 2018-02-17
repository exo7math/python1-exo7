
##############################
# Listes II - Idées
##############################

from random import *


##############################
# Activité 3 - Rappels
##############################

##################################################
def affiche_tableau(tableau):
    """
    Affiche un carré à l'écran
    Entrée : un tableau de taille n x n
    Sortie : rien (affichage à l'écran)
    """    
    
    n = len(tableau)

    for i in range(n):
        for j in range(n):
            print('{:>3d}'.format(tableau[i][j])," ", end="")
        print()

    return

##############################
def somme_diagonale(tableau):
    n = len(tableau)
    somme = 0
    for i in range(n):
        somme = somme + tableau[i][i]
    return somme


##############################
def somme_anti_diagonale(tableau):
    n = len(tableau)
    somme = 0
    for i in range(n):
        somme = somme + tableau[n-1-i][i]
    return somme


##############################
# Activité 4 - Carrés magiques
##############################

## Question 1 ##

##############################

print("--- Carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre_3x3 = [ [4,9,2], [3,5,7], [8,1,6] ]
carre_4x4 = [ [1,14,15,4], [7,9,6,12], [10,8,11,5], [16,3,2,13] ]
print("--- Carré 3x3 ---")
affiche_tableau(carre_3x3)
print("--- Carré 4x4 ---")
affiche_tableau(carre_4x4)


## Question 2 ##

##############################
def est_carre_magique(carre):
    n = len(carre)
    total = n * (n**2 + 1) // 2

    if somme_diagonale(carre) != total:
        return False

    if somme_anti_diagonale(carre) != total:
        return False            

    for ligne in carre:
        if sum(ligne) != total:
            return False

    for j in range(n):
        somme = 0
        for i in range(n):
            somme = somme + carre[i][j]
        if somme != total:
            return False

    return True

print("--- Vérification carré magique ---")
print(est_carre_magique(carre_3x3))
print(est_carre_magique(carre_4x4))


## Question 3 ##

##############################
def carre_aleatoire(n):

    entiers = list(range(1,n**2+1))
    shuffle(entiers)
    carre = [ entiers[i*n:(i+1)*n] for i in range(n) ]
    return carre

print("--- Carré aléatoire ---")
carre = carre_aleatoire(4)
affiche_tableau(carre)
print(est_carre_magique(carre))


## Question 4 ##

##############################
def addition_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            nouv_carre[i][j] = carre[i][j] + k

    return nouv_carre



## Question 4 ##

##############################
def multiplication_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            nouv_carre[i][j] = carre[i][j] * k

    return nouv_carre

# Test 
print("--- Addition, multiplication de carrés magiques ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre = [ [4,9,2], [3,5,7], [8,1,6] ]
somme_carre = addition_carre(carre,-1)
produit_carre = multiplication_carre(carre,9)
affiche_tableau(carre)
affiche_tableau(somme_carre)
affiche_tableau(produit_carre)


## Question 5 ##

##############################
def homothetie_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(k*n)] for i in range(k*n)]   

    for i in range(k*n):
        for j in range(k*n):
            nouv_carre[i][j] = carre[i//k][j//k]

    return nouv_carre

# Test 
print("--- Homothétie carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
# carre = [ [4,9,2], [3,5,7], [8,1,6] ]
# grand_carre = homothetie_carre(carre,3)
# affiche_tableau(grand_carre)

grand_carre = homothetie_carre(carre_3x3,3)
affiche_tableau(grand_carre)

grand_carre = homothetie_carre(carre_4x4,2)
affiche_tableau(grand_carre)


## Question 6 ##

##############################
def addition_bloc_carre(grand_carre,petit_carre):

    N = len(grand_carre)
    n = len(petit_carre)
    # k = N//n

    nouv_carre = [[0 for j in range(N)] for i in range(N)]   

    for i in range(N):
        for j in range(N):
            nouv_carre[i][j] = grand_carre[i][j] + petit_carre[i%n][j%n]

    return nouv_carre

    # Test 
print("--- Addition de blocs - Carré magique ---")
petit_carre = [ [1,2], [3,4] ]
carre = [ [1,2,3], [4,5,6], [7,8,9] ]
grand_carre = homothetie_carre(carre,2)
nouv_grand_carre = addition_bloc_carre(grand_carre,petit_carre)
affiche_tableau(petit_carre)
print("---")
affiche_tableau(grand_carre)
print("---")
affiche_tableau(nouv_grand_carre)


## Question 7 ##

##############################
def produit_carres(carre1,carre2):
    n = len(carre1)
    # m = len(carre2)

    carre3a = addition_carre(carre2,-1)
    # print("---")
    # affiche_tableau(carre3a)
    carre3b = homothetie_carre(carre3a,n)
    # print("---")
    # affiche_tableau(carre3b)
    carre3c = multiplication_carre(carre3b,n**2)
    # print("---")
    # affiche_tableau(carre3c)    
    carre3d = addition_bloc_carre(carre3c,carre1)
    # print("---")
    # affiche_tableau(carre3d)

    return carre3d


#### Test ####
carre1 = [ [4,9,2], [3,5,7], [8,1,6] ]
carre2 = [ [4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13] ]
carre3 = produit_carres(carre1,carre2)
print("--- Produit carrés ---")
affiche_tableau(carre1)
print("---")
affiche_tableau(carre2)
print("---")
affiche_tableau(carre3)
print(est_carre_magique(carre3))


#### Produit non commutatif ####
carre4 = produit_carres(carre2,carre1)
print("--- Produit carrés ---")
affiche_tableau(carre1)
print("---")
affiche_tableau(carre2)
print("---")
affiche_tableau(carre4)
print(est_carre_magique(carre4))


#### Carré de taille 36 x 36 ####
carre5 = produit_carres(carre1,carre4)