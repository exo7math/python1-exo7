
##############################
# Fonctions - Idées
##############################

##############################
# Activité 1 - Introduction aux fonctions
##############################

##################################################
## Question 1 ##


# Fonction sans paramètre, sans sortie

def affiche_table_de_7():
    """ Affiche la table de 7 """

    print("--- Table de 7 ---")
    for i in range(1,11):
        print(i,"x 7 =",str(i*7))

    return


# Test
affiche_table_de_7()


##################################################


def affiche_bonjour():
    """ Dit bonjour """

    prenom = input("Comment t'appelles-tu ? ")
    print("Bonjour",prenom)

    return


# Test
affiche_bonjour()



##################################################
## Question 2 ##


# Fonction avec paramètre, sans sortie

def affiche_une_table(n):
    """ Affiche la table de n """

    print("--- Table de",n,"---")
    for i in range(1,11):
        print(i,"x",n,"=",str(i*n))

    return


# Test
affiche_une_table(5)


##################################################


def affiche_salutation(formule):
    """ Dit bonjour, bonsoir, au revoir... """

    prenom = input("Comment t'appelles-tu ? ")
    print(formule,prenom)

    return


# Test
affiche_salutation("Coucou")
  


##################################################
## Question 3 ##


# Fonction sans paramètre, avec sortie

def demande_prenom_nom():
    """ Demande et renvoie le prénom et le nom """
    
    prenom = input("Quel est ton prénom ? ")
    nom = input("Quel est ton nom ? ")

    nom_complet = prenom + " " + nom.upper()

    return nom_complet


# Test
identite = demande_prenom_nom()
print("Identité :",identite)


