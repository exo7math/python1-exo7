
##############################
# Jeu de la vie
##############################

##############################
# Activité 1 - Tableau
##############################


##################################################
## Question 1 ##

n, p = 5, 8;
tableau = [[0 for j in range(p)] for i in range(n)] 

# Clignotant
tableau[2][2] = 1
tableau[2][3] = 1
tableau[2][4] = 1


##################################################
## Question 2 ##

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

