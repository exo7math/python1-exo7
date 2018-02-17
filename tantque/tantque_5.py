
##############################
# Tant que - Booléen - Arithmétiques
##############################


##############################
# Activité 5 - Nombres ayant 4 ou 8 diviseurs
##############################


# Conjecture : entre 1 et N, il y a toujours plus d'entiers ayant 
# 4 diviseurs que d'entier ayant 8 diviseurs

##############################
## Question 1 ##

def nombre_de_diviseurs_1(n):
    """ Nombre de diviseurs de n (y compris 1  et n) """
    nb = 0
    for d in range(1,n+1):
        if n % d == 0:
            nb = nb + 1
    return nb


def nombre_de_diviseurs_2(n):
    """ Nombre de diviseurs de n (y compris 1  et n) """    
    nb = 2  # on compte déjà 1 et n
    for d in range(2,n//2+1):
        if n % d == 0:
            nb = nb + 1
    return nb


# On garde la méthode la plus efficace
def nombre_de_diviseurs(n):
    return nombre_de_diviseurs_2(n)


# Test 
print("--- Nombre de diviseurs ---")
print(nombre_de_diviseurs(100))


##############################

## Question 2 ##

def quatre_et_huit_diviseurs(Nmin,Nmax):
    nb_quatre = 0 
    nb_huit = 0
    for n in range(Nmin,Nmax):
        nb = nombre_de_diviseurs(n)
        if nb == 4:
            nb_quatre = nb_quatre + 1
        if nb == 8:
            nb_huit = nb_huit + 1
    return nb_quatre, nb_huit


# Test 
print("--- Nombre ayant 4 puis 8 diviseurs ---")
print(quatre_et_huit_diviseurs(1,100))


##############################

## Question 3 ##

# Recherche de contre-exemple à la conjecture
# Il faut prendre N assez grand par exempel 
# entre 1 et N = 250000 il y a plus d'entiers 
# ayant 8 diviseurs que 4 diviseurs


# Par tranche de 50 000 (les calculs sont longs !)

# print(quatre_et_huit_diviseurs(1,50000))
# print(quatre_et_huit_diviseurs(50000,100000))
# print(quatre_et_huit_diviseurs(100000,150000))
# print(quatre_et_huit_diviseurs(150000,200000))
# print(quatre_et_huit_diviseurs(200000,250000))

# Tranche 1 : 12073, 10957
# Tranche 2 : 11254, 11224
# Tranche 3 : 10995, 11229
# Tranche 4 : 10838, 11218
# Tranche 5 : 10690, 11260

# 4 diviseurs 12073+11254+10995+10838+10690   = 55850
# 8 diviseurs 10957+11224+11229+11218+11260   = 55888

