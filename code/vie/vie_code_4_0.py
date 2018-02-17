# Clignotant
def clignotant():
    """ Définition du clignotant """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[4][7] = 1
    tableau[4][8] = 1
    tableau[4][9] = 1
    canvas.delete("all")   
    afficher_lignes()   
    afficher_tableau(tableau)
    return


# Vaisseau
def vaisseau():
    """ Définition du vasseau spatial """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[3][4] = 1
    tableau[3][5] = 1
    tableau[3][6] = 1
    tableau[2][6] = 1
    tableau[1][5] = 1
    canvas.delete("all")    
    afficher_lignes()   
    afficher_tableau(tableau)
    return


# Pentadecathlon
def pentadecathlon():
    """ Définition du pentadecathlon """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[6][4] = 1
    tableau[6][5] = 1
    tableau[6][7] = 1
    tableau[6][8] = 1    
    tableau[6][9] = 1
    tableau[6][10] = 1
    tableau[6][12] = 1
    tableau[6][13] = 1  
    tableau[5][6] = 1
    tableau[7][6] = 1
    tableau[5][11] = 1
    tableau[7][11] = 1 
    canvas.delete("all")      
    afficher_lignes()                    
    afficher_tableau(tableau)
    return