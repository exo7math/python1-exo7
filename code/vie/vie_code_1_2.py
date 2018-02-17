def voir_tableau(tab):
    """ Affiche un tableau à l'écran
    Entrée : un tableau à deux dimension
    Sortie : rien (affichage à l'écran) """    

    for i in range(n):
        for j in range(p):
            print(tab[i][j], end="")
        print()

    return


# Test 
voir_tableau(tableau)

