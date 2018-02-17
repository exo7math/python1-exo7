
##############################
# Graphes et nombre de Ramsey R(3)
##############################



##################################################
# Un graphe 

n = 5

# Un exemple
exemple_graphe = [[0 for j in range(n)] for i in range(n)] 

exemple_graphe[3][2] = 1; exemple_graphe[2][3] = 1; 
exemple_graphe[1][2] = 1; exemple_graphe[2][1] = 1




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
# print("--- Matrice du graphe ---")
voir_graphe(exemple_graphe)

##################################################
##################################################
# A faire : conversion entier vers bianire avec padding
# sans faire "format"
# modele = '{:0'+str(n)+'b}'
# binaire = modele.format(p)
# liste_binaire = [int(b) for b in list(binaire)]

##################################################
##################################################
# Génère tous les sous-ensembles

##################################################
def sous_ensembles(n):
    """Trouve tous les sous-ensembles d'un ensemble à n éléments"""

    tous_sous_ens = []

    for p in range(2**n):

        # binaire = list(bin(i)[2:])
        # binaire = '{:08b}'.format(i)        
        modele = '{:0'+str(n)+'b}'
        binaire = modele.format(p)
        liste_binaire = [int(b) for b in list(binaire)]
        #print(liste_binaire)

        sous_ens = []
        for j in range(n):
            if liste_binaire[n-j-1] == 1:
                sous_ens = sous_ens + [j]

        tous_sous_ens = tous_sous_ens + [sous_ens]

    return tous_sous_ens

# Test 
print("--- Sous-ensembles ---")
print(sous_ensembles(n))


##################################################
def sous_ensembles_fixe(n,k):
    return [sous_ens for sous_ens in sous_ensembles(n) if len(sous_ens)==k]


# Test (suite)
print("--- Sous-ensembles à 3 éléments ---")

k = 3
sous_ensembles_n_k = sous_ensembles_fixe(n,k)
print(sous_ensembles_n_k)


##################################################
##################################################
# Test si un graphe est valide ou pas
# pour les 3 amis/étranger


##################################################
def graphe_contient_3_position(graphe,b,i,j,k):
    """Cherche si sommets i, j, k sont tous reliés entre eux b=0 ou b=1"""
    if graphe[i][j] == b and graphe[i][k] == b and graphe[j][k] == b:
        return True
    else:
        return False

# Test
print("--- Sous-graphe complet fixé de 0 et de 1 ---")
print(graphe_contient_3_position(exemple_graphe,0,1,2,3))
print(graphe_contient_3_position(exemple_graphe,1,1,2,3))


##################################################
def graphe_contient_3(graphe):
    """Cherche si trois sommets sont tous reliés entre eux"""
  
    for sous_ens in sous_ensembles_n_k:
        #print(sous_ens)
        contient_3_zero = graphe_contient_3_position(graphe,0,*sous_ens)
        contient_3_un = graphe_contient_3_position(graphe,1,*sous_ens)
        contient = contient_3_zero or contient_3_un
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
print("--- Sous-graphe complet de 0 et de 1 ---") 
print(graphe_contient_3(exemple_graphe))

##################################################



##################################################
##################################################
# Calcul de tous les graphes possible à n sommets
# Il y a 2^( (n-1)*n/2 )

def test_tous_graphes(n):

    N = ((n-1) * n)//2
    print("Nombre total de graphes :",2**N)

    for p in range(2**N):


        modele = '{:0'+str(N)+'b}'
        binaire = modele.format(p)
        liste_binaire = [int(b) for b in list(binaire)]

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

print("\n\n--- Test global ---")
print("n = ",n)
test_tous_graphes(n)
print("Si aucun pb, c'est que c'est bon !")



# n = 6 : 0.5 secondes
# n = 7 : 33 secondes
# n = 8 : 5000 secondes = 1h30 (extrapolation sur échantillon de 10^-2)
# n = 9 : 1 560 000 = 18 jours (extrapolation sur échantillon de 10^-4)