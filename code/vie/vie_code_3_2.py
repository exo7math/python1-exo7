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