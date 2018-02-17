
##############################
# Chercher et remplacer
##############################


##############################
# Activité 1 - Chercher
##############################

## Question 1 ##

print("--- Avec 'in' ---")
chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "PAS"

if sous_chaine in chaine:
    print("Trouvé !")


## Question 2 ##

print("--- Avec find() ---")
position = chaine.find(sous_chaine)
print(position)
position = chaine.find("XYZ")
print(position)


## Question 3 ##


def chercher(chaine,sous_chaine):
    long_chaine = len(chaine)
    long_sous_chaine = len(sous_chaine)
    for i in range(long_chaine-long_sous_chaine+1):
        trouve = True
        for j in range(long_sous_chaine):
            if chaine[i+j] != sous_chaine[j]:
                trouve = False
                break
        if trouve == True:
            return i
    return None

# Test

print("--- A la main ---")

position = chercher(chaine,sous_chaine)
print(position)
position = chercher(chaine,"XYZ")
print(position)


##############################
# Activité 2 - Remplacer 
##############################


chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "PAS"
nouv_sous_chaine = "PLUS"


## Question 1 ##

print("--- Avec replace() ---")
nouv_chaine = chaine.replace(sous_chaine,nouv_sous_chaine)
print(nouv_chaine)


## Question 2 ##

#
# remplacer_une_fois() A la main en utilisant chercher()
def remplacer(chaine,sous_chaine,nouv_sous_chaine):
    pos = chercher(chaine,sous_chaine)

    if pos is not None:  # Si trouvé
        finpos = pos+len(sous_chaine)
        chaine = chaine[:pos]+nouv_sous_chaine+chaine[finpos:]

    return chaine

print("--- Remplacer : à la main ---")
nouv_chaine = remplacer(chaine,sous_chaine,nouv_sous_chaine)
print(nouv_chaine)

## Question 3 ##

#
# remplacer() remplace toutes les occurences


def remplacer_tout(chaine,sous_chaine,nouv_sous_chaine):

    pos = chercher(chaine,sous_chaine)
        
    while pos is not None:  # Tant que trouvé
        finpos = pos+len(sous_chaine)
        chaine = chaine[:pos]+nouv_sous_chaine+chaine[finpos:]
        pos = chercher(chaine,sous_chaine)

    return chaine

print("--- Remplacer tout : à la main ---")
chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "ETRE"
nouv_sous_chaine = "AVOIR" 
nouv_chaine = remplacer_tout(chaine,sous_chaine,nouv_sous_chaine)
print(nouv_chaine)



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
exp = "T.E"
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


##############################
# Activité 4 - Itérations
##############################


## Question 1 ##

 # Test

print("--- Une itération ---")
phrase = "01001110"
motif = "01"
nouv_motif = "10"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)

phrase = "01001110"
motif = "0011"
nouv_motif = "1100"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)

phrase = "01001110"
motif = "0011"
nouv_motif = "111000"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)


## Question 2 ##

# Constante globale du maximum d'itérations considérées
MAX_ITER = 1000


def iterations(phrase,motif,nouv_motif):
    i = 0
    while i <= MAX_ITER:
        nouv_phrase = remplacer(phrase,motif,nouv_motif)
        if phrase == nouv_phrase:
            return i, phrase
        else:
            phrase = nouv_phrase
            i = i+1
    return None


print("--- Itérations ---")
phrase = "000011011"
motif = "0011"
nouv_motif = "1100"
resultat = iterations(phrase,motif,nouv_motif)
print(resultat)



phrase = "000011011"
motif = "001"
nouv_motif = "11000"
resultat = iterations(phrase,motif,nouv_motif)
print(resultat)


## Rappel sur binaire ##


def decimal_vers_binaire(n,p):
    chaine_b = bin(n)  # Conversion en une chaîne écriture binaire
    chaine_b = chaine_b[2:]  # On enlève le préfixe

    # On rajoute des zéros au début si besoin
    nb_zeros = p - len(chaine_b)
    for i in range(nb_zeros):
        chaine_b = "0" + chaine_b

    return chaine_b

# Test
print(decimal_vers_binaire(33,8))

## Question 3 ##

def iteration_maximale(p,motif,nouv_motif):

    maxi_iter = 0
    phrase_maxi_iter = ""
    nouv_phrase_maxi_iter = ""

    for n in range(2**p):
        phrase = decimal_vers_binaire(n,p)
        resultat = iterations(phrase,motif,nouv_motif)
        #print(resultat)
        if resultat is None:
            return None, phrase
        else:
            nb_iter = resultat[0]
            if nb_iter > maxi_iter:
                maxi_iter = nb_iter 
                phrase_maxi_iter = phrase  
                nouv_phrase_maxi_iter = resultat[1]
    return maxi_iter, phrase_maxi_iter, nouv_phrase_maxi_iter


print("--- Itérations maximales ---")

# Exemple
motif = "0011"
nouv_motif = "111000"
print(iteration_maximale(4,motif,nouv_motif))

# Linéaire
motif = "0011"
nouv_motif = "110"
print("- Linéaire -")
print(iteration_maximale(10,motif,nouv_motif))

# Quadratique
motif = "01"
nouv_motif = "10"
print("- Quadratique -")
print(iteration_maximale(10,motif,nouv_motif))

# Exponentiel
motif = "01"
nouv_motif = "110"
print("- Exponentiel -")
print(iteration_maximale(10,motif,nouv_motif))

# Ne termine pas
motif = "01"
nouv_motif = "001"
# print(iteration_maximale(10,motif,nouv_motif))