
##############################
# Tant que
##############################


##############################
# Activité 7 - Racine carrée
##############################

##################################################
## Question 1 ##


from math import *   

def calcul_racine_1(n):
    """ Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière """    

    racine_reelle = sqrt(n)
    racine = floor(racine_reelle)

    return racine


# Test 
print("--- Racine carrée (1) ---")
print(calcul_racine_1(10))
print(calcul_racine_1(36))
print(calcul_racine_1(56892))



##################################################
## Question 2 ##

def calcul_racine_2(n):
    """ Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière """    

    racine = 0
    while racine*racine <= n:
        racine = racine + 1

    return racine - 1


# Test 
print("--- Racine carrée (2) ---")
print(calcul_racine_2(10))
print(calcul_racine_2(36))
print(calcul_racine_2(56892))


##################################################
## Question 3 ##

def calcul_racine_3(n):
    """ Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière """    

    a = 1
    b = n
    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
    return min(a,b)


# Tests
print("--- Racine carrée (3) ---")
print(calcul_racine_3(10))
print(calcul_racine_3(36))
print(calcul_racine_3(56892))


##################################################

def affichage_calcul_racine_3(n):
    """ Affiche les étapes du calcul de la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière """    

    a = 1
    b = n
    i = 0
    print("--- Racine de",n,"---")
    print("i =",i," ;  a = ",a," ;  b = ",b)

    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
        i = i +1
        print("i =",i," ;  a = ",a," ;  b = ",b)
    print("Racine carrée entière de",n,"égal",min(a,b))

    return min(a,b)


# Tests
affichage_calcul_racine_3(10)
affichage_calcul_racine_3(1664)


##################################################
# Test 

# print("--- Test ---")
# for i in range(1,1000000):
#     # print(i)
#     if calcul_racine_1(i) != calcul_racine_3(i):
#         print('Attention : problème',i)   
# print('Fin test')


##################################################
## Variante Question 3 ##

def calcul_racine_4(n):
    """
    Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière
    """    

    un = n
    un1 = (un + n//un) // 2

    while un1 < un:
        un = un1
        un1 = (un + n//un) // 2

    return un

# Test 
print("--- Racine carrée (4) ---")
print(calcul_racine_4(10))
print(calcul_racine_4(36))
print(calcul_racine_4(56892))

