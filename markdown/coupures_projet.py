
##############################
# Coupure d'une liste - Justification
##############################

from random import randint
longueurs_mots = [randint(1,20) for i in range(50)] 
#long_mots = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]


longueur_ligne = 100
longueur_espace = 1


################################################
def coupures_simples(long_mots,long_ligne):
    coupures = [0]
    i = 1

    while i < len(long_mots):
        somme = long_mots[i-1]

        while (i < len(long_mots)) and (somme <= long_ligne):
            somme = somme + long_mots[i]
            i = i + 1

        coupures = coupures + [i-1]

    coupures = coupures + [len(long_mots)+1]

    return coupures  


################################################
def afficher_coupures_simples(long_mots,coupures):
    print("\n--- Coupures sans espaces ---")
    print("longueurs des mots",long_mots)
    print("coupures",coupures)
    for i in range(len(coupures)-1):
        ligne = long_mots[coupures[i]:coupures[i+1]]
        somme = sum(ligne)
        print(i,"---",ligne,"--- somme = ",somme,"indices",coupures[i],coupures[i+1])

#coupures = coupures_simples(longueurs_mots,longueur_ligne)
#afficher_coupures_simples(longueurs_mots,coupures)


################################################
def coupures_espaces(long_mots,long_ligne):
    coupures = [0]
    i = 1

    while i < len(long_mots):
        somme = long_mots[i-1]

        while (i < len(long_mots)) and (somme <= long_ligne):
            somme = somme + longueur_espace + long_mots[i]
            i = i + 1
            
        if i < len(long_mots): 
            coupures = coupures + [i-1]

    coupures = coupures + [len(long_mots)]

    return coupures  




################################################
def afficher_coupures_espaces(long_mots,coupures):
    print("\n--- Coupures avec espaces ---")
    print("longueurs des mots",long_mots)
    print("coupures",coupures)
    for i in range(len(coupures)-1):
        ligne = long_mots[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne)-1       
        somme =  sum(ligne) + nb_espaces*longueur_espace      
        print(i,"---",ligne,"--- somme = ",somme,"indices",coupures[i],coupures[i+1])


# coupures = coupures_espaces(longueurs_mots,longueur_ligne)
# afficher_coupures_espaces(longueurs_mots,coupures)



################################################
def calcul_long_espaces(long_mots,coupures,long_ligne):
    long_espaces_ligne = []
    
    for i in range(len(coupures)-2):

        ligne = long_mots[coupures[i]:coupures[i+1] ] 
        nb_espaces = len(ligne)-1
        somme =  sum(ligne) + nb_espaces*longueur_espace
        restant = long_ligne - somme
        if nb_espaces > 0:
            nouvel_espace = longueur_espace + restant / nb_espaces
        else:
            nouvel_espace = longueur_espace
        long_espaces_ligne = long_espaces_ligne + [nouvel_espace]

    long_espaces_ligne = long_espaces_ligne + [longueur_espace] # Dernière ligne du paragraphe pas justifiée

    return long_espaces_ligne



################################################
def afficher_calcul_long_espaces(long_mots,coupures,long_ligne):
    long_espaces_ligne = calcul_long_espaces(long_mots,coupures,longueur_ligne)
    print("\n--- Coupures avec espaces ---")
    print("longueurs des mots",long_mots)
    print("coupures",coupures)
    for i in range(len(coupures)-1):
        ligne = long_mots[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne) - 1     
        somme =  sum(ligne) + nb_espaces*long_espaces_ligne[i]   

        print(i,"---",ligne,"--- somme = ",somme,"indices",coupures[i],coupures[i+1])
        print("longueur espace de cette ligne",long_espaces_ligne[i])


#coupures = coupures_espaces(longueurs_mots,longueur_ligne)
#afficher_calcul_long_espaces(longueurs_mots,coupures,longueur_ligne)




