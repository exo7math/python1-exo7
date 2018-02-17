def coupures_espaces(long):
    """ Calcule les coupures des mots pour un alignement à gauche (avec espaces)
    Entrée : une suite de longueurs (une liste d'entiers)
    Sortie : la liste des indices où effectuer la coupure """

    coupures = [0]

    i = 1

    while i < len(long):
        somme = long[i-1]

        while (i < len(long)) and (somme <= longueur_totale):
            somme +=  longueur_espace + long[i]
            i += 1

        if somme > longueur_totale:
            coupures +=  [i-1]            

    coupures += [len(long)]

    return coupures  


################################################


def afficher_coupures_espaces():
    """ Test : affiche les coupures avec espaces """

    print("\n--- Coupures avec espaces ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_espaces(longueurs) 
    print("Coupures :",coupures)

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne)-1       
        somme =  sum(ligne) + nb_espaces*longueur_espace      
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_totale-somme,)

    return

# Test 
afficher_coupures_espaces()