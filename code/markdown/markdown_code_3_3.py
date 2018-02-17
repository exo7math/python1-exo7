def calcul_longueur_espaces(long,coupures):
    """ Calcule les longueurs des espaces pour justification
    Entrée : une suite de longueurs avec les coupures
    Sortie : la longueurs des espaces pour chaque ligne """

    longueur_espaces_ligne = []
    
    for i in range(len(coupures)-2):

        ligne = long[coupures[i]:coupures[i+1] ] 
        nb_espaces = len(ligne)-1
        somme =  sum(ligne) + nb_espaces*longueur_espace
        restant = longueur_totale - somme
        
        if nb_espaces > 0:
            nouvel_espace = longueur_espace + restant / nb_espaces
        else:
            nouvel_espace = longueur_espace

        longueur_espaces_ligne += [nouvel_espace]

    # Dernière ligne du paragraphe pas justifiée
    longueur_espaces_ligne += [longueur_espace] 

    return longueur_espaces_ligne


################################################


def afficher_calcul_longueur_espaces():
    """ Test : affiche les longueurs des espaces """

    print("\n--- Coupures avec espaces et justification ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_espaces(longueurs) 
    print("Coupures :",coupures)

    longueur_espaces_ligne = calcul_longueur_espaces(longueurs,coupures)
    print("Longueur des espaces de chaque ligne :",[float("{0:0.2f}".format(l)) for l in longueur_espaces_ligne])

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne) - 1     
        somme =  sum(ligne) + nb_espaces*longueur_espaces_ligne[i]   

        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_totale-somme,)
        print("Longueur espace de cette ligne",longueur_espaces_ligne[i])

    return


# Test
afficher_calcul_longueur_espaces()