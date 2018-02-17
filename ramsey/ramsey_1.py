
##############################
# Graphes et combinatoire de Ramsey
##############################


##############################
# Activité 1 - Définition et amis/étrangers
##############################

## Question 1 ##

##################################################

# Exemple 1
n = 3
exemple_graphe_1 = [[0 for j in range(n)] for i in range(n)] 
exemple_graphe_1[0][1] = 1; exemple_graphe_1[1][0] = 1
exemple_graphe_1[0][2] = 1; exemple_graphe_1[2][0] = 1

# Exemple 2
n = 4

exemple_graphe_2 = [[0 for j in range(n)] for i in range(n)] 

exemple_graphe_2[0][2] = 1; exemple_graphe_2[2][0] = 1 
exemple_graphe_2[0][3] = 1; exemple_graphe_2[3][0] = 1
exemple_graphe_2[1][2] = 1; exemple_graphe_2[2][1] = 1


# Exemple 3
n = 5

exemple_graphe_3 = [[0 for j in range(n)] for i in range(n)] 

exemple_graphe_3[0][2] = 1; exemple_graphe_3[2][0] = 1 
exemple_graphe_3[0][3] = 1; exemple_graphe_3[3][0] = 1
exemple_graphe_3[1][2] = 1; exemple_graphe_3[2][1] = 1
exemple_graphe_3[1][4] = 1; exemple_graphe_3[4][1] = 1
exemple_graphe_3[3][4] = 1; exemple_graphe_3[4][3] = 1 

# Exemple 4
n = 6

exemple_graphe_4 = [[0 for j in range(n)] for i in range(n)] 

exemple_graphe_4[3][2] = 1; exemple_graphe_4[2][3] = 1; 
exemple_graphe_4[1][2] = 1; exemple_graphe_4[2][1] = 1
exemple_graphe_4[3][4] = 1; exemple_graphe_4[4][3] = 1
exemple_graphe_4[4][1] = 1; exemple_graphe_4[1][4] = 1
exemple_graphe_4[0][2] = 1; exemple_graphe_4[2][0] = 1
exemple_graphe_4[5][0] = 1; exemple_graphe_4[0][5] = 1
exemple_graphe_4[5][1] = 1; exemple_graphe_4[1][5] = 1
exemple_graphe_4[0][3] = 1; exemple_graphe_4[3][0] = 1


# Exemple cours 
n = 4

exemple_graphe_cours_1 = [[0 for j in range(n)] for i in range(n)] 

exemple_graphe_cours_1[0][2] = 1; exemple_graphe_cours_1[2][0] = 1 
exemple_graphe_cours_1[1][3] = 1; exemple_graphe_cours_1[3][1] = 1

## Question 2 ##

##################################################
def voir_graphe(graphe):
    """
    Affiche un graphe à l'écran
    Entrée : un graphe comme tableau à deux dimension
    Sortie : rien (affichage à l'écran)
    """    
    
    n = len(graphe)

    for j in range(n):
        for i in range(n):
            print(graphe[i][j], end="")
        print()

    return

# Test 
if __name__ == '__main__':
    print("--- Matrice du graphe ---")
    print("--- Exemple 1 ---")
    voir_graphe(exemple_graphe_1)
    print("--- Exemple 2 ---")
    voir_graphe(exemple_graphe_2)
    print("--- Exemple 3 ---")
    voir_graphe(exemple_graphe_3)
    print("--- Exemple 4 ---")
    voir_graphe(exemple_graphe_4)

    print("--- Cours 1 ---")
    voir_graphe(exemple_graphe_cours_1)    

##################################################
##################################################
# Test si un graphe est contient
# 3 amis/étranger dont les positions sont données


##################################################
def contient_3_amis_fixes(graphe,i,j,k):
    """Cherche si sommets i, j, k sont tous reliés entre eux comme amis"""
    if graphe[i][j] == 1 and graphe[i][k] == 1 and graphe[j][k] == 1:
        return True
    else:
        return False

##################################################
def contient_3_etrangers_fixes(graphe,i,j,k):
    """Cherche si sommets i, j, k sont tous reliés entre eux comme étrangers"""
    if graphe[i][j] == 0 and graphe[i][k] == 0 and graphe[j][k] == 0:
        return True
    else:
        return False        

# Test
if __name__ == '__main__':
    print("--- Sous-graphe fixé de 0 et de 1 ---")
    print(contient_3_amis_fixes(exemple_graphe_4,1,3,4))
    print(contient_3_etrangers_fixes(exemple_graphe_4,1,3,4))

