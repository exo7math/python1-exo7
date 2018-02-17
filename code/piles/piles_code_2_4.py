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