
##############################
# Fonctions
##############################


##############################
# Activité 5 - Egalité expérimentale
##############################

from math import *

##################################################
## Question 1 ##

def valeur_absolue(x):
    if x >= 0:
        return x
    else:
        return -x


##################################################
# def valeur_absolue_moins(x):
#     return valeur_absolue(-x)


##################################################
def racine_du_carre(x):
    return sqrt(x**2)
    

##################################################
def egalite_experimentale_1(f,g):
    """ Teste si deux fonctions sont expérimentalement égales """
    for i in range(-100,101):
        if f(i) != g(i):
            return False
    return True

# Test
print("--- Egalité experimentale, une variable ---")
# print(egalite_experimentale_1(valeur_absolue,valeur_absolue_moins))  # Vrai
print(egalite_experimentale_1(valeur_absolue,racine_du_carre))       # Vrai


##################################################
## Question 2 ##

def F1(a,b):
    return (a+b)**2


##################################################
def F2(a,b):
    return a**2 + 2*a*b + b**2


##################################################
def F3(a,b):
    return (a-b)**3


##################################################
def F4(a,b):
    return a**3 - 3*a**2*b  - 3*a * b**2 + b**3


##################################################
def F5(a,b):
    return a**3 - 3*a**2*b  + 3*a * b**2 - b**3


################################################
def egalite_experimentale_2(F,G):
    """ Teste si deux fonctions de deux variables sont expérimentalement égales """

    for i in range(-100,101):
        for j in range(-100,101):
            if F(i,j) != G(i,j):
                # print(i,j,F(i,j),G(i,j))
                return False
    return True

# Test
print("--- Egalité experimentale, deux variables ---")
print(egalite_experimentale_2(F1,F2))   # Vrai
print(egalite_experimentale_2(F3,F4))   # Faux
print(egalite_experimentale_2(F3,F5))   # Vrai


################################################
## Question 3 ##

def sincos(x):
    return sin(x)**2 + cos(x)**2


################################################
def un(x):
    return 1


##################################################

precision = 0.00001   # = 10**-5  

def egalite_experimentale_3(f,g):
    """ Teste si deux fonctions sont expérimentalement égales 
    en autorisant une marge d'erreur """   

    for i in range(-100,101):
        if abs(f(i) - g(i))> precision :
            return False
    return True

# Test
print("--- Egalité experimentale approchée ---")
print(egalite_experimentale_1(sincos,un))  # Faux !! Mais pourtant devrait être vrai !
print(sin(3)**2+cos(3)**2)         #  Explication : Python ne renvoie par exactement 1 
print(egalite_experimentale_3(sincos,un))  # Vrai !


# Test avec d'autres inégalités, exemples :
# sin(2x) = 2 sin(x)cos(x)
# cos(pi/2 - x) = sin(x)
# et qq unes fausses ...


################################################
# Une égalité fausse mais experimentalement vraie

def g1(x):
    return sin(pi*x)

################################################

def g2(x):
    return 0

print("--- Une égalité fausse mais experimentalement vraie ---")
print(egalite_experimentale_3(g1,g2))  # Vrai (on a toujours égalité pour i entier)
print(g1(1/2))  # et pourtant g1(0.5) n'est pas nul, donc l'égalité n'est pas vrai en général
