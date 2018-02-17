
##############################
# Graphes et combinatoire de Ramsey
##############################


##############################
# Activité 4 - Sous-ensembles
##############################

from ramsey_3 import decimal_vers_binaire


##############################
##############################



## Question 1 ##


# Génère tous les sous-ensembles

##################################################
def sous_ensembles(n):
    """Trouve tous les sous-ensembles de l'ensemble à n éléments [0,1,2,...n-1]"""

    tous_sous_ens = []

    for p in range(2**n):

        # Conversion binaire
        liste_binaire = decimal_vers_binaire(p,n)
        #print(liste_binaire)

        sous_ens = []
        for j in range(n):
            # if liste_binaire[n-j-1] == 1:  
            if liste_binaire[j] == 1:                
                sous_ens = sous_ens + [j]

        tous_sous_ens = tous_sous_ens + [sous_ens]

    return tous_sous_ens

# Test 
if __name__ == '__main__':
    print("--- Sous-ensembles ---")
    n = 3
    SS_ENS = sous_ensembles(n) 
    print("Pour n = ",n)
    print("Nombre de sous-ensembles = ",len(SS_ENS))
    print(SS_ENS)


## Question 2 ##

##################################################
def sous_ensembles_fixe(n,k):
    tous_sous_ens_fixe = []
    for sous_ens in sous_ensembles(n):
        if len(sous_ens) == k:
            tous_sous_ens_fixe = tous_sous_ens_fixe + [sous_ens]
    return tous_sous_ens_fixe

# Test (suite)
if __name__ == '__main__':
    print("--- Sous-ensembles à 3 éléments ---")

    n = 6
    k = 3
    SS_ENS_3 = sous_ensembles_fixe(n,k)
    print("Pour n = ",n," k = ",k)
    print("Nombre de sous-ensembles à 3 éléments = ",len(SS_ENS_3))
    print(SS_ENS_3)






