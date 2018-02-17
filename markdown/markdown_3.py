

##############################
# Visualiseur de texte - Markdown
##############################


##############################
# Activité 3 - Justification
##############################



################################################
## Question 1 ##

from random import randint

# longueurs = [randint(5,15) for i in range(103)] 
# longueurs = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]
longueurs = [8, 11, 9, 14, 8, 8, 15, 10, 14, 11, 15, 15, 5, 12, 9, 9, 15, 10, 14, 5, 12, 8, 8, 13, 10, 11, 8, 13, 7, 5, 6, 11, 7, 7, 13, 6, 6, 9, 8, 12, 5, 8, 7, 6, 6, 15, 13, 11, 7, 12]

longueur_ligne = 100
longueur_espace = 1

def coupures_simples(long):
    """ Calcule les coupures des mots pour un alignement à gauche (sans espaces)
    Entrée : une suite de longueurs (une liste d'entiers)
    Sortie : la liste des indices où effectuer la coupure """

    coupures = [0]

    i = 1
    while i < len(long):
        somme = long[i-1]

        while (i < len(long)) and (somme <= longueur_ligne):
            somme +=  long[i]
            i += 1

        if somme > longueur_ligne:
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
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme =",somme,"Reste =",longueur_ligne-somme,)

    return

# Test
afficher_coupures_simples()



################################################
## Question 2 ##

def coupures_espaces(long):
    """ Calcule les coupures des mots pour un alignement à gauche (avec espaces)
    Entrée : une suite de longueurs (une liste d'entiers)
    Sortie : la liste des indices où effectuer la coupure """

    coupures = [0]

    i = 1

    while i < len(long):
        somme = long[i-1]

        while (i < len(long)) and (somme <= longueur_ligne):
            somme +=  longueur_espace + long[i]
            i += 1

        if somme > longueur_ligne:
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
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_ligne-somme,)

    return

# Test 
afficher_coupures_espaces()



################################################
## Question 3 ##

def calcul_longueur_espaces(long,coupures):
    """ Calcule les longueurs des espaces pour justification
    Entrée : une suite de longueurs avec les coupures
    Sortie : la longueurs des espaces pour chaque ligne """

    longueur_espaces_ligne = []
    
    for i in range(len(coupures)-2):

        ligne = long[coupures[i]:coupures[i+1] ] 
        nb_espaces = len(ligne)-1
        somme =  sum(ligne) + nb_espaces*longueur_espace
        restant = longueur_ligne - somme
        
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

        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_ligne-somme,)
        print("Longueur espace de cette ligne",longueur_espaces_ligne[i])

    return


# Test
afficher_calcul_longueur_espaces()




