from random import randint

# longueurs = [randint(5,15) for i in range(103)] 
# longueurs = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]
longueurs = [8, 11, 9, 14, 8, 8, 15, 10, 14, 11, 15, 15, 5, 12, 9, 9, 15, 10, 14, 5, 12, 8, 8, 13, 10, 11, 8, 13, 7, 5, 6, 11, 7, 7, 13, 6, 6, 9, 8, 12, 5, 8, 7, 6, 6, 15, 13, 11, 7, 12]

longueur_totale = 100
longueur_espace = 1

def coupures_simples(long):
    """ Calcule les coupures des mots pour un alignement à gauche (sans espaces)
    Entrée : une suite de longueurs (une liste d'entiers)
    Sortie : la liste des indices où effectuer la coupure """

    coupures = [0]

    i = 1
    while i < len(long):
        somme = long[i-1]

        while (i < len(long)) and (somme <= longueur_totale):
            somme +=  long[i]
            i += 1

        if somme > longueur_totale:
            coupures +=  [i-1]

    coupures += [len(long)]

    return coupures  


################################################


def afficher_coupures_simples():
    """ Test : affiche les coupures simples """

    print("\n--- Coupures sans espaces ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_simples(longueurs)   
    print("coupures",coupures)

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        somme = sum(ligne)
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme =",somme,"Reste =",longueur_totale-somme,)

    return

# Test
afficher_coupures_simples()