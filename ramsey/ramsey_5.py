
##############################
# Graphes et combinatoire de Ramsey
##############################


##############################
# Activité 5 - Preuve n=6
##############################


from ramsey_1 import *
from ramsey_1 import contient_3_amis_fixes
from ramsey_1 import contient_3_etrangers_fixes
from ramsey_3 import decimal_vers_binaire
from ramsey_4 import sous_ensembles
from ramsey_4 import sous_ensembles_fixe

##############################
##############################

# Sous-ensembles 
n = 6
k = 3
SS_ENS_6_3 = sous_ensembles_fixe(n,k)

## Question 1 ##

##################################################
def graphe_contient_3(graphe):
    """Cherche si trois sommets sont tous reliés entre eux"""
  
    n = len(graphe)

    #for sous_ens in SS_ENS_6_3:  # Pour n=6, k=3
    for sous_ens in sous_ensembles_fixe(n,3):  # Pour n quelconque 
        #print(sous_ens)
        contient_3_amis = contient_3_amis_fixes(graphe,*sous_ens)
        contient_3_etrangers = contient_3_etrangers_fixes(graphe,*sous_ens)
        contient = contient_3_amis or contient_3_etrangers
        if contient == True:
            break

    # Affichage
    # if contient == True:
    #     print("Validé par l'exemple:",sous_ens)
    # else:
    #     print("Problème")
    # if contient == False:
    #     print("Problème")
    #     voir_graphe(graphe)

    return contient

 # Test
# Un exemple


if __name__ == '__main__':
    print("--- Test conjecture un seul graphe ---")
    print("--- Exemple 1 ---")
    print(graphe_contient_3(exemple_graphe_1))
    print("--- Exemple 2 ---")
    print(graphe_contient_3(exemple_graphe_2))
    print("--- Exemple 3 ---")
    print(graphe_contient_3(exemple_graphe_3))
    print("--- Exemple 4 ---")
    print(graphe_contient_3(exemple_graphe_4))

## Question 2 ##

##################################################
##################################################
# Calcul de tous les graphes possible à n sommets
# Il y a 2^( (n-1)*n/2 )
def voir_tous_graphes(n):

    N = ((n-1) * n)//2
    print("Nombre total de graphes :",2**N)

    for p in range(2**N):
        # Conversion binaire
        liste_binaire = decimal_vers_binaire(p,N)

        print("p =",p,liste_binaire)

        graphe = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = liste_binaire.pop()
                graphe[i][j] = b
                graphe[j][i] = b

        voir_graphe(graphe)

    return

 # Test
# n = 4
# print("--- Affiche tous les graphes possibles ---")
# print("n = ",n)
# voir_tous_graphes(n)

## Question 3 ##

##################################################
##################################################
# Test de tous les graphes possible à n sommets
# Il y a 2^( (n-1)*n/2 )

def test_tous_graphes(n):

    N = ((n-1) * n)//2
    print("Nombre total de graphes :",2**N)

    for p in range(2**N):
        # Conversion binaire
        liste_binaire = decimal_vers_binaire(p,N)

        # print("p =",p,liste_binaire)

        graphe = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = liste_binaire.pop()
                graphe[i][j] = b
                graphe[j][i] = b

        # voir_graphe(graphe)
        test = graphe_contient_3(graphe)
        if test == False:
            print("Problème avec",p)

    return

# Test
n = 6
print("\n\n--- Preuve du théorème de Ramsey, n = 6 ---")
print("n = ",n)
print("--- Recherche de graphe ne vérifiant pas l'énonce...")
test_tous_graphes(n)
print("fin des calculs ---")
print("Si rien ne s'est affiché, c'est que c'est bon !")







