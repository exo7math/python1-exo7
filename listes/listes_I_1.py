
##############################
# Listes I
##############################


##############################
# Cours 1

maliste = [11,13,17,19]
maliste.append(23)
maliste.append(29)
print(maliste[5])
len(maliste)


##############################
# Activité 1 - Intérêts
##############################

## Question 1 ##

##############################
def interets_simples(S0,p,n):
    liste = [S0]
    interets = S0 * p/100
    S = S0
    for i in range(n):
        S = S + interets
        liste.append(S)
    return liste


# Test
print("--- Intérêts simples ---")
liste_interets_simples = interets_simples(1000,10,12)
print(liste_interets_simples)
print(liste_interets_simples[11])



## Question 2 ##

##############################
def interets_composes(S0,p,n):
    liste = [S0]
    S = S0
    for i in range(n):
        interets = S * p/100
        S = S + interets
        liste.append(S)
    return liste


# Test
print("--- Intérêts composés ---")
liste_interets_composes = interets_composes(1000,7,12)
print(liste_interets_composes)
print(liste_interets_composes[11])

