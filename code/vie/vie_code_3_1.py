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