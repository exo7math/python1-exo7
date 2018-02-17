
##############################
# Jeu de la vie
##############################


##############################
# Rappels - Activité 1
##############################

from vie_1 import *

n, p = 5, 8;
tableau = [[0 for j in range(p)] for i in range(n)] 

# Clignotant
tableau[2][2] = 1
tableau[2][3] = 1
tableau[2][4] = 1


##############################
# Activité 3 - Evolution
##############################


##################################################
## Question 1 ##

def nombre_voisins(i,j,tab):
    """ Calcule le nb de voisins de la cellule(i,j)
    Entrée : une cellule dans un tableau à deux dimension
    Sortie : le nb de cellules voisines """ 

    nb = 0
    # Voisin en haut à gauche
    if (i>0) and (j>0) and (tab[i-1][j-1] != 0):
        nb += 1
    # Voisin juste au-dessus
    if (i>0) and (tab[i-1][j] != 0):
        nb += 1
    # Voisin en haut à droite
    if (i>0) and (j<p-1) and (tab[i-1][j+1] != 0):
        nb += 1
    # Voisin juste à gauche
    if (j>0) and (tab[i][j-1] != 0):
        nb += 1
    # Voisin juste à droite
    if (j<p-1) and (tab[i][j+1] != 0):
        nb += 1
   # Voisin en bas à gauche
    if (i<n-1) and (j>0) and (tab[i+1][j-1] != 0):
        nb += 1
    # Voisin juste en-dessous
    if (i<n-1) and (tab[i+1][j] != 0):
        nb += 1
    # Voisin en bas à droite
    if (i<n-1) and (j<p-1) and (tab[i+1][j+1] != 0):
        nb += 1

    return nb

# Test
print("--- Nombre de voisins ---")
print(nombre_voisins(1,1,tableau))
print(nombre_voisins(2,1,tableau))
print(nombre_voisins(3,1,tableau))
print(nombre_voisins(2,0,tableau))
print(nombre_voisins(2,2,tableau))
print(nombre_voisins(3,3,tableau))

##################################################

def voir_voisins(tab):
    """ Affiche le nb de voisins à l'écran
    Entrée : un tableau à deux dimension
    Sortie : rien (affichage à l'écran) """    

    for i in range(n):
        for j in range(p):
            print(nombre_voisins(i,j,tab), end='')
        print()

    return


# Test
print("--- Position de départ ---")
voir_tableau(tableau)
print("--- Nombre de voisins (tableau) ---")
voir_voisins(tableau)


##################################################
## Question 2 ##

def evolution(tab):
    """ Calcule l'évolution en un jour
    Entrée : un tableau à deux dimension
    Sortie : un tableau à deux dimension """    

    nouv_tab = [[0 for j in range(p)] for i in range(n)]

    for j in range(p):
        for i in range(n):
            # Cellule vivante ou pas ?
            if tab[i][j] != 0:
                cellule_vivante = True
            else:
                cellule_vivante = False

            # Nombres de voisins
            nb_voisins = nombre_voisins(i,j,tab)

            # Règle du jeu de la vie
            if cellule_vivante == True and (nb_voisins == 2 or nb_voisins == 3):
                nouv_tab[i][j] = 1
            if cellule_vivante == False and nb_voisins == 3:
                nouv_tab[i][j] = 1          

    return nouv_tab


# Test
print("--- Position de départ ---")
voir_tableau(tableau)
print("--- Nombre de voisins ---")
voir_voisins(tableau)
print("--- Après évolution ---")
tableau = evolution(tableau)
voir_tableau(tableau)



