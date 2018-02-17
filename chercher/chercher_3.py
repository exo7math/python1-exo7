
##############################
# Chercher et remplacer
##############################


##############################
# Activité 3 - Regex - Expressions rationnelles 
##############################


## Question 1 ##


from re import *

def python_regex_chercher(chaine,exp):
    trouve = search(exp,chaine)
    if trouve:
        return trouve.group(), trouve.start(), trouve.end()
    else:
        return None

# Test
print("--- Avec regex search() ---")
chaine = "ETRE OU NE PAS ETRE"
exp = "P.S"
print(python_regex_chercher(chaine,exp))

exp = "E..E"
print(python_regex_chercher(chaine,exp))

exp = "[OT]U"
print(python_regex_chercher(chaine,exp))

exp = "[MN]..P[AI]S"
print(python_regex_chercher(chaine,exp))


## Question 2 ##

# Le joker "."

def regex_chercher_joker(chaine,exp):

    long_chaine = len(chaine)
    long_exp = len(exp)

    for i in range(long_chaine-long_exp+1):
        trouve = True
        for j in range(long_exp):
            if exp[j] != "." and chaine[i+j] != exp[j]:
                trouve = False
                break
        if trouve == True:
            return chaine[i:i+long_exp],i,i+long_exp
    return None

# Test
print("--- regex joker ---")
chaine = "ETRE OU NE PAS ETRE"
exp = "T.E"
print(regex_chercher_joker(chaine,exp))

## Question 3 ##

# Le choix "[AB]", voir [ABC]

def genere_choix(exp):
    liste_exp = [""]
    mode_choix = False
    for c in exp:
        if c == "[": 
            mode_choix = True
            old_liste_exp = list(liste_exp)
            nouv_list_exp = []
        elif c == "]":
            mode_choix = False
            liste_exp = nouv_list_exp
        else:
            if mode_choix == False:  # Mode normal
                liste_exp = [ l + c for l in liste_exp]
            else:  # Mode choix   
                nouv_list_exp = nouv_list_exp + [ l + c for l in old_liste_exp]      

    return liste_exp

# Test
print("--- regex choix ---")
exp = "ET[XYZ]RE[UVW]"
print(genere_choix(exp))


def regex_chercher_choix(chaine,exp):
    liste_exp = genere_choix(exp)
    for mon_exp in liste_exp:
        resultat = python_regex_chercher(chaine,mon_exp)
        if resultat is not None:
            return resultat

    return None


# Test
print("--- regex choix ---")
chaine = "ETRE OU NE PAS ETRE"
exp = "P[ABC]S"
print(regex_chercher_choix(chaine,exp))


## Question 4 ##

# La négation [^A] voir [^AB]

