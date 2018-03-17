
##############################
# Graphes et combinatoire de Ramsey
##############################


##############################
# Activité 6 - Pour aller plus loin
##############################


from ramsey_1 import *
from ramsey_1 import contient_3_amis_fixes
from ramsey_1 import contient_3_etrangers_fixes
from ramsey_3 import decimal_vers_binaire
from ramsey_4 import sous_ensembles
from ramsey_4 import sous_ensembles_fixe

##############################
##############################



## Question 1 ##

# Sous-ensembles 
n = 6
k = 3
SS_ENS_3 = sous_ensembles_fixe(n,k)



##################################################
def graphe_contient_3(graphe):
    """Cherche si un graphe possède 3 amis ou 3 étrangers."""
  
    n = len(graphe)

    for sous_ens in SS_ENS_3:  
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


# Test de tous les graphes possible à n sommets
# Il y a 2^( (n-1)*n/2 )

def test_tous_graphes(n):

    N = ((n-1) * n)//2
    print("Nombre total de graphes :",2**N)

    for p in range( ((2**N) // 2)):
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
            print("Problème avec graphe p =",p)

    return

# Test
print("\n\n--- Preuve du théorème de Ramsey, n =",n,"---")
print("n = ",n)
print("--- Recherche de graphe ne vérifiant pas l'énonce...")
test_tous_graphes(n)
print("fin des calculs ---")
print("Si rien ne s'est affiché, c'est que c'est bon !")


# n = 6 : 0.5 secondes
# n = 7 : 20 secondes
# n = 8 : 2500 secondes = 40 min (extrapolation sur échantillon de 10^-2)
# n = 9 : 800 000 secondes = 9 jours (extrapolation sur échantillon de 10^-4)


## Question 2 ##

##################################################
##################################################

# Sous-ensembles 
n = 9
SS_ENS_3 = sous_ensembles_fixe(n,3)
SS_ENS_4 = sous_ensembles_fixe(n,4)

##################################################
def contient_4_amis_fixes(graphe,i,j,k,l):
    """Cherche si sommets i, j, k sont tous reliés entre eux comme amis"""
    if graphe[i][j] == 1 and graphe[i][k] == 1 and graphe[i][l] == 1 and graphe[j][k] == 1 and graphe[j][l] == 1 and graphe[k][l] == 1:
        return True
    else:
        return False

# Test de tous les graphes possible à n sommets
# pour savoir s'il existe 4 amis ou 3 étrangers


def graphe_contient_3_4(graphe):
    """Cherche si trois ou quatre sommets sont tous reliés entre eux"""

    n = len(graphe)

    # Cherche 3 étrangers
    for sous_ens in SS_ENS_3:  
        contient_3_etrangers = contient_3_etrangers_fixes(graphe,*sous_ens)
        if contient_3_etrangers == True:
            break

    # Si pas 3 étrangers, cherche 4 amis
    if contient_3_etrangers == False:
        for sous_ens in SS_ENS_4:  
            contient_4_amis = contient_4_amis_fixes(graphe,*sous_ens)
            if contient_4_amis == True:
                break
    else: 
        contient_4_amis = True # Peu importe vu que déjà 3 étrangers

    contient = contient_3_etrangers or contient_4_amis


    return contient



def ramsey_4_3(n):

    N = ((n-1) * n)//2
    print("Nombre total de graphes :",2**N)

    # for p in range(  ((2**N)) // 100000 ):
    for p in range( 1000000 ):    
        # Conversion binaire
        liste_binaire = decimal_vers_binaire(p,N)

        # print("p =",p,liste_binaire)

        graphe = [[0 for j in range(n)] for i in range(n)] 

        for j in range(0,n):
            for i in range(j+1,n):
                b = liste_binaire.pop()
                graphe[i][j] = b
                graphe[j][i] = b


        test = graphe_contient_3_4(graphe)
        if test == False:
            print("Problème avec graphe p =",p)

    return

# Test
print("\n\n--- Preuve du théorème de Ramsey avec 4 amis ou 3 étrangers, n =",n,"---")
print("n = ",n)
print("--- Recherche de graphe ne vérifiant pas l'énonce...")
ramsey_4_3(n)
print("fin des calculs ---")
print("Si rien ne s'est affiché, c'est que c'est bon !")


# n = 7, contre-exemples facile
# n = 8 contre-exemple par exemple p=111121101
# n = 9 est vrai ! Mais doit prendre 18 jours de calculs