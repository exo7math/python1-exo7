
##############################
# Chercher et remplacer
##############################


##############################
# Rappel de l'activité 1 - Chercher 
##############################

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

##############################
# Rappel de l'activité 2 - Remplacer 
##############################

def remplacer(chaine,sous_chaine,nouv_sous_chaine):
    pos = chercher(chaine,sous_chaine)

    if pos is not None:  # Si trouvé
        finpos = pos+len(sous_chaine)
        chaine = chaine[:pos]+nouv_sous_chaine+chaine[finpos:]

    return chaine


##############################
# Activité 4 - Itérations
##############################


## Question 1 ##

 # Test

print("--- Une itération ---")

print("-- Ex 1 --")
phrase = "01001110"
motif = "01"
nouv_motif = "10"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)

print("-- Ex 2 --")
phrase = "01001110"
motif = "0011"
nouv_motif = "1100"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)

print("-- Ex 3 --")
phrase = "01001110"
motif = "0011"
nouv_motif = "111000"
nouv_phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
print(nouv_phrase)

print("-- Ex 4 --")
phrase = "0001"
motif = "01"
nouv_motif = "1100"
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)



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
print("-- Ex 1 --")
phrase = "000011011"
motif = "0011"
nouv_motif = "1100"
resultat = iterations(phrase,motif,nouv_motif)
print(resultat)

phrase = "000011011"
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)
phrase = remplacer(phrase,motif,nouv_motif)
print(phrase)

print("-- Ex 2 --")

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
motif = "01"
nouv_motif = "100"
print(iteration_maximale(4,motif,nouv_motif))


## Question 4 ##


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
nouv_motif = "1100"
print("- Ne se termine pas -")
print(iteration_maximale(4,motif,nouv_motif))



