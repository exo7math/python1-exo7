
##############################
# Binaire - partie I
##############################

##############################
# Activité 1 - Decimale vers entier
##############################

## Question 1 ##

def decimale_vers_entier_1(liste_decimale):
    nombre = 0
    p = len(liste_decimale)
    for i in range(p):
        d = liste_decimale[p-1-i]
        nombre = nombre + d*10**i

    return nombre

## Question 1bis ##


def decimale_vers_entier_2(liste_decimale):
    nombre = 0
    i = 0
    for d in reversed(liste_decimale):
        nombre = nombre + d*10**i
        i = i + 1

    return nombre

# Test
print("--- Ecriture décimale vers entier ---")
liste = [1,2,3,4]
print(decimale_vers_entier_1(liste))
print(decimale_vers_entier_2(liste))


##############################
# Activité 2 - Binaire vers entier
##############################



## Question 1 ##

def binaire_vers_entier_1(liste_binaire):
    nombre = 0
    p = len(liste_binaire)
    for i in range(p):
        if liste_binaire[p-1-i] == 1:
            nombre = nombre + 2**i

    return nombre

## Question 1bis ##

def binaire_vers_entier_2(liste_binaire):
    nombre = 0
    i = 0
    for b in reversed(liste_binaire):
        if b == 1:
            nombre = nombre + 2**i
        i = i + 1

    return nombre



## Question 2 ##

def binaire_vers_entier_bis(liste_binaire):
    nombre = 0
    for b in liste_binaire:
        if b == 0:
            nombre = nombre*2
        else:
            nombre = nombre*2 + 1

    return nombre



# Test
print("--- Ecriture binaire vers entier ---")
liste = [1,1,0,1,1,0,0,1]
print(binaire_vers_entier_1(liste))
print(binaire_vers_entier_2(liste))
print(binaire_vers_entier_bis(liste))


## Question 3 (à virer) ##

# Utilise bin() [pas très fantastique]

def liste_vers_chaine(liste_binaire):
    liste_chaine = [str(b) for b in liste_binaire]
    chaine = "".join(liste_chaine)
    chaine = "0b" + chaine  
    return chaine  

def binaire_vers_entier_4(liste_binaire):
    
    chaine = liste_vers_chaine(liste_binaire)
    nombre = int(chaine,2)

    return nombre  

# print("--- Ecriture binaire vers entier avec bin() ---")
# liste = [1,1,0,1,1,0,0,1]
# print(liste_vers_chaine(liste))
# print(binaire_vers_entier_4(liste))



##############################
# Activité 3 - Ecriture décimale
##############################


def entier_vers_decimale(n):
    if n==0: return [0]
    liste_decimale = []
    while n != 0:
        liste_decimale = [n%10] + liste_decimale
        n = n//10
    return liste_decimale


# Test
print("--- Entier vers écriture décimale ---")
n = 1234
liste = entier_vers_decimale(n)
entier = decimale_vers_entier_1(liste)
print(n)
print(liste)
print(entier)



##############################
# Activité 4 - Ecriture binaire
##############################


def entier_vers_binaire(n):
    if n==0: return [0]
    liste_binaire = []
    while n != 0:
        liste_binaire = [n%2] + liste_binaire
        n = n//2
    return liste_binaire

# Test
print("--- Entier vers écriture binaire ---")
n = 1234
liste = entier_vers_binaire(n)
entier = binaire_vers_entier_1(liste)
print(n)
print(liste)
print(entier)

