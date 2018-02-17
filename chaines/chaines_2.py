
##############################
# Chaînes de caractères - Analyse statistique d'un texte
##############################


##############################
# Activité 2 - Jeux de mots
##############################

## Question 1 ##

def distance_hamming(mot1,mot2):
    """ Calcule la distance de Hamming
    Entrée : deux mots de même longueur
    Sortie : la distance entre ces mots """

    distance = 0
    for i in range(len(mot1)):
        if mot1[i] != mot2[i]:
            distance = distance + 1

    return distance


# Test 
premier_mot = "JAPON"
second_mot = "SAVON"
dist = distance_hamming(premier_mot,second_mot)
print("La distance entre",premier_mot,"et",second_mot, "est",dist)



## Question 2 ##

def transforme_en_latin_cochon(mot):
    """ Transforme un mot en latin-cochon
    Entrée : un mot (une chaîne de caractères) 
    Sortie : le mot transformé en latin cochon s'il commence par une consonne. """

    premiere_lettre = mot[0]
    reste_mot = mot[1:len(mot)]

    if premiere_lettre not in ["A", "E", "I", "O", "U", "Y"]:
        latin_cochon = reste_mot + premiere_lettre + "UM"
    else:
        latin_cochon = mot

    return latin_cochon


# Test 
mot = "SALOPETTE"
latin = transforme_en_latin_cochon(mot)
print("Le mot",mot,"devient",latin,"!")


    
## Question 3 ##

def transforme_en_verlan(mot):
    """ Transforme un mot en verlan
    Entrée : un mot (une chaîne de caractères)
    Sortie : le mot transformé verlan """

    verlan = ""
    for carac in mot:
        verlan = carac + verlan

    return verlan


# Test 
mot = "BONJOUR"
verlan = transforme_en_verlan(mot)
print("Le mot",mot,"devient",verlan,"!")



## Question 4 ##

def est_un_palindrome(mot):
    """ Détermine si un mot est un palindrome
    Entrée : un mot (une chaîne de caractères)
    Sortie : vrai si le mot est un palindrome, faux sinon """

    verlan = transforme_en_verlan(mot)
    if mot == verlan:
        return True
    else: 
        return False


# Test 
mot = "KAYAK"
print("Le mot",mot,"est-il un palindrome ? : ",est_un_palindrome(mot))



