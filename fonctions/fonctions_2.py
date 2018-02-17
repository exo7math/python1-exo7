
##############################
# Fonctions
##############################



##############################
# Activité 2 - Fonctions
##############################

##################################################
## Question 1 ##


# Fonction avec paramètre, avec sortie

def trinome_1(x):
    """ Calcule 3x^2-7x+4 """

    resultat = 3*x**2 - 7*x + 4

    return resultat


# Test
print("--- Trinôme ---")
for i in range(10):
    print("La valeur en x =",i,"est",trinome_1(i))


##################################################


def trinome_2(a,b,c,x):
    """ Calcule ax^2+bx+c """

    resultat = a*x**2 + b*x + c

    return resultat


# Test
a = 2 ; b = -1 ; c = 0
print("Trinôme pour a,b,c =",a,b,c)
for i in range(10):
    print("La valeur en x =",i,"est",trinome_2(a,b,c,i))



##################################################
## Question 2 ##


# Fonction avec paramètre, avec sortie

def conversion_euros_vers_dollars(montant):
    """ Calcule la valeur en dollars d'un montant donné en euros """

    montant_dollar = 1.15 * montant

    return montant_dollar


# Test
print("--- Devises ---")
x = 20
print(x,"euros valent", conversion_euros_vers_dollars(x),"dollars")


##################################################


def conversion_euros(montant,devise):
    """ Calcule la valeur dans une monnaie d'un montant donné en euros """

    if devise == "dollar":
        taux = 1.15
    if devise == "livre":
        taux = 0.81
    if devise == "yen":
        taux = 130
       
    montant_devise = montant * taux
 
    return montant_devise


# Test
x = 100
for madevise in ["yen","dollar","livre"]:
    print(x,"euros valent", conversion_euros(x,madevise),madevise)



##################################################
## Question 3 ##

from math import *

# Calculs de différents volumes

def volume_cube(a):         
    return a**3

def volume_boule(r):         
    return 4/3 * pi * r**3

def volume_cylindre(r,h):
    return pi * r**2 * h

def volume_boite(a,b,c):
    return a * b * c

# Test
print("--- Volumes ---")
print(volume_cube(3))
print(volume_boule(3))
print(volume_cylindre(2,5))
print(volume_boite(3,4,5))


##################################################
## Question 4 ##

def perimetre_aire_rectangle(a,b):
    """ Calcule le périmètre et l'aire 
    d'un rectangle de côtés a et b """

    p = 2*a+2*b
    A = a * b

    return p, A

def perimetre_aire_disque(r):
    """ Calcule le périmètre et l'aire 
    d'un disque de rayon r """

    p = 2 * pi * r
    A = pi * r**2

    return p, A

print("--- Périmètres et aires ---")
print(perimetre_aire_rectangle(4,5))
print(perimetre_aire_disque(3))


# Recherche expérimentale : comparaison périmètre/aire d'un disque

for rayon in range(0,30):
    perimetre, aire = perimetre_aire_disque(rayon/10)
    print(rayon/10, perimetre - aire)

# Conclusion expérimentale :
#   pour 0 < r < 2, le perimètre est strictement plus grand que l'aire
#   pour r = 2, le périmètre égale l'aire,
#   pour r > 2, le périmètre est strictement plus petit que l'aire 
