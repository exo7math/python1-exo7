
##############################
# Chaînes de caractères - Analyse statistique d'un texte
##############################


##############################
# Activité 1 - Pluriels
##############################

## Question 1 ##

mot = "chat"
pluriel = mot + "s"
print("Mon mot : ",mot)
print("Au pluriel : ",pluriel)


## Question 2 ##

# mot = "chat"
mot = "souris"

derniere_lettre = mot[len(mot)-1]

if derniere_lettre == "s":
    pluriel = mot
else:
    pluriel = mot + "s"

print("Mon mot : ",mot)
print("Au pluriel : ",pluriel)


## Question 3 ##

# mot = "chat"
# mot = "souris"
mot = "journal" 

derniere_lettre = mot[len(mot)-1]
avant_derniere_lettre = mot[len(mot)-2]

if derniere_lettre == "s":
    pluriel = mot
elif avant_derniere_lettre == "a" and derniere_lettre == "l":
    debut_mot = mot[0:len(mot)-2]
    pluriel = debut_mot + "aux"
else:
    pluriel = mot + 's'

print("Mon mot : ",mot)
print("Au pluriel : ",pluriel)



## Question 4 ##


# C'est mieux avec une fonction !

def met_au_pluriel(mot):
    """ Met un mot au pluriel.
    Entrée : un mot
    Sortie : le mot au pluriel (sauf exceptions) """

    derniere_lettre = mot[len(mot)-1]
    avant_derniere_lettre = mot[len(mot)-2]

    if derniere_lettre == "s":
        pluriel = mot
    elif avant_derniere_lettre == "a" and derniere_lettre == "l":
        debut_mot = mot[0:len(mot)-2]
        pluriel = debut_mot + "aux"
    else:
        pluriel = mot + "s"

    return pluriel


# Test 
#mot = input("Dis moi un mot : ")
#pluriel = met_au_pluriel(mot)
#print("Son pluriel est :",pluriel)


## Question 5 ##

def affiche_conjugaison(verbe):
    """ Conjugue au présent.
    Entrée : un verbe du premier groupe
    Sortie : affiche la conjugaison au présent"""

    debut_verbe = verbe[0:len(verbe)-2]
    fin_verbe = verbe[len(verbe)-2:len(verbe)]

    if fin_verbe == "er":
        print("Je " + debut_verbe + "e\n")
        print("Tu " + debut_verbe + "es\n")  
        print("Il/elle " + debut_verbe + "e\n")
        print("Nous " + debut_verbe + "ons\n")
        print("Vous " + debut_verbe + "ez\n")
        print("Ils/elles " + debut_verbe + "ent\n")
    else:
        print("Ce n'est pas un verbe du premier groupe !")

    return


# Test 
verbe = input("Donne-moi un verbe du premier groupe : ")
affiche_conjugaison(verbe)





     
