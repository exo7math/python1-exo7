
##############################
# Listes II - Idées
##############################

from random import *

##############################
# Cours


##############################
# Activité 1 - Manipulation de liste et listes par compréhension
##############################

##############################
def multiplier(liste,k):
    return [k*x for x in liste]

##############################
def puissance(liste,k):
    return [x**k for x in liste]

##############################
def addition(liste1,liste2):
    liste_add = []
    for i in range(len(liste1)):
        liste_add.append(liste1[i]+liste2[i])
    return liste_add

##############################
def non_zero(liste):
    return [x for x in liste if x != 0]

##############################
def paires(liste):
    return [x for x in liste if x % 2 == 0]


# Test
print(addition([1,2,3],[4,5,6]))
print(non_zero([1,0,2,3,0,4,5,0]))
print(paires([1,0,2,3,0,4,5,0]))




##############################
# Activité 2 - Somme fixée 
##############################

# Trouver deux élément différents dont la somme vaut 100
def somme_deux_100(liste):
    n = len(liste)
    for i in range(n):
        for j in range(i+1,n):
            if liste[i]+liste[j] == 100:
                print(i,j,liste[i],liste[j])
                return True
    return False


# Suite de termes cosnécutifs qui font 100
def somme_suite_100(liste):
    n = len(liste)
    for i in range(n):
        somme = 0
        # A finir
    return False

# Suite maximale de k termes cosnécutifs avec un seul passage

from random import *
# liste_100 = [randint(1,50) for i in range(20)]
liste_100 = [4, 37, 22, 32, 4, 39, 40, 38, 42, 50, 42, 47, 16, 4, 50, 25, 5, 11, 47, 14]
print(liste_100)
print(somme_deux_100(liste_100))

# Idées proba : Quelle long donne prob > 1/2 




##############################
# Activité 3 - Tableau à deux dimensions
##############################


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


tableau = [ [1,2,3], [4,5,6], [7,8,9] ]
print(somme_diagonale(tableau))
print(somme_anti_diagonale(tableau))


##############################
def somme_tout(tableau):
    somme = 0
    for ligne in tableau:
        for x in ligne:
            somme = somme  + x
    return somme

print(somme_tout(tableau))



##############################
# Activité 4 - Carrés magiques
##############################

##################################################
def affiche_carre(carre):
    """
    Affiche un carré à l'écran
    Entrée : un carré comme tableau à deux dimension
    Sortie : rien (affichage à l'écran)
    """    
    
    n = len(carre)

    for i in range(n):
        for j in range(n):
            print('{:>3d}'.format(carre[i][j])," ", end="")
        print()

    return


# Test 
print("--- Carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre = [ [4,9,2], [3,5,7], [8,1,6] ]
affiche_carre(carre)


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

print(est_carre_magique(carre))

##############################
def carre_aleatoire(n):

    entiers = list(range(1,n**2+1))
    shuffle(entiers)
    carre = [ entiers[i*n:(i+1)*n] for i in range(n) ]
    return carre

carre = carre_aleatoire(4)
affiche_carre(carre)


# def proba_carre_magique(n,N):
#     nb_magiques = 0
#     for k in range(N):
#         carre = carre_aleatoire(n)
#         if est_carre_magique(carre):
#             affiche_carre(carre)
#             nb_magiques += 1
#     return nb_magiques/N

# print("--- Proba carrés magiques ---")
# print(proba_carre_magique(4,1000))



##############################
def addition_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            nouv_carre[i][j] = carre[i][j] + k

    return nouv_carre
    
##############################
def multiplication_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            nouv_carre[i][j] = carre[i][j] * k

    return nouv_carre

# Test 
print("--- Carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre = [ [4,9,2], [3,5,7], [8,1,6] ]
somme_carre = addition_carre(carre,-1)
produit_carre = multiplication_carre(carre,9)
affiche_carre(carre)
affiche_carre(somme_carre)
affiche_carre(produit_carre)




##############################
def homothetie_carre(carre,k):

    n = len(carre)
    nouv_carre = [[0 for j in range(k*n)] for i in range(k*n)]   

    for i in range(k*n):
        for j in range(k*n):
            nouv_carre[i][j] = carre[i//k][j//k]

    return nouv_carre

    # Test 
print("--- Carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre = [ [4,9,2], [3,5,7], [8,1,6] ]
grand_carre = homothetie_carre(carre,3)
affiche_carre(grand_carre)


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
print("--- Carré magique ---")
# carre = [ [1,2,3], [4,5,6], [7,8,9] ]
carre = [ [4,9,2], [3,5,7], [8,1,6] ]
grand_carre = homothetie_carre(carre,2)
nouv_grand_carre = addition_bloc_carre(grand_carre,[[1,2],[3,4]])
print("---")
affiche_carre(grand_carre)
print("---")
affiche_carre(nouv_grand_carre)


##############################
def produit_carres(carre1,carre2):
    n = len(carre1)
    N = len(carre2)

    carre3a = addition_carre(carre2,-1)
    # print("---")
    # affiche_carre(carre3a)
    carre3b = homothetie_carre(carre3a,n)
    # print("---")
    # affiche_carre(carre3b)
    carre3c = multiplication_carre(carre3b,n**2)
    # print("---")
    # affiche_carre(carre3c)    
    carre3d = addition_bloc_carre(carre3c,carre1)
    # print("---")
    # affiche_carre(carre3d)

    return carre3d

carre1 = [ [4,9,2], [3,5,7], [8,1,6] ]
carre2 = [ [4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13] ]
carre3 = produit_carres(carre1,carre2)
print("--- Produit carrés ---")
affiche_carre(carre1)
print("---")
affiche_carre(carre2)
print("---")
affiche_carre(carre3)
print(est_carre_magique(carre3))
