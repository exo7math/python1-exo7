
##############################
# Fonctions - Idées
##############################

##############################
# Activité 1 - Introduction aux fonctions
##############################

## Question 1 ##

##################################################

# Fonction sans paramètre, sans sortie

def affiche_table_de_7():
    """Affiche la table de 7"""

    print("--- Table de 7 ---")
    for i in range(1,11):
        print(i,'x 7 =',str(i*7))

    return

# Test
# affiche_table_de_7()


##################################################
def affiche_bonjour():
    """Dit bonjour"""

    prenom = input("Comment t'appelles-tu ? ")
    print("Bonjour",prenom)

    return

# Test
# affiche_bonjour()



## Question 2 ##

##################################################

# Fonction avec paramètre, sans sortie

def affiche_une_table(n):
    """Affiche la table de n"""

    print("--- Table de",n,"---")
    for i in range(1,11):
        print(i,"x ",n,"=",str(i*n))

    return

# Test
# affiche_une_table(5)


##################################################
def affiche_salutation(formule):
    """Dit bonjour, bonsoir, au revoir..."""

    prenom = input("Comment t'appelles-tu ? ")
    print(formule,prenom)

    return

# Test
# affiche_salutation("Coucou")
  


## Question 3 ##

##################################################

# Fonction sans paramètre, avec sortie

##################################################
def demande_prenom_nom():
    """Demande et renvoie le prénom et le nom"""
    
    prenom = input("Quel est ton prénom ? ")
    nom = input("Quel est ton nom ? ")

    nom_complet = prenom + " " + nom.upper()

    return nom_complet

# Test
# identite = demande_prenom_nom()
# print(identite)



##############################
# Activité 2 - Fonctions
##############################

## Question 1 ##

##################################################

# Fonction avec paramètre, avec sortie

def binome_1(x):
    """Calcul 3x^2-7x+4"""

    resultat = 3*x**2 - 7*x + 4

    return resultat

# Test
for i in range(10):
    print("Valeur en ",i,"est",binome_1(i))



def binome_2(a,b,c,x):
    """Calcul ax^2+bx+c"""

    resultat = a*x**2 + b*x + c

    return resultat

# Test
a = 3 ; b = -1 ; c = 0
print("Binôme pour a,b,c =",a,b,c)
for i in range(10):
    print("Valeur en ",i,"est",binome_2(a,b,c,i))

## Question 2 ##

##################################################

# Fonction avec paramètre, avec sortie

##################################################
def conversion_euros_vers_dollar(montant):

    montant_dollar = 1.15 * montant

    return montant_dollar

# Test
x = 20
print(x,"euros valent", conversion_euros_vers_dollar(x),"dollars")



##################################################
def conversion_euros(montant,devise):
    
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





## Question 3 ##

##################################################
from math import *

def volume_cube(a):         
    return a**3

def volume_sphere(r):         
    return 4/3 * pi * r**3

def volume_cylindre(r,h):
    return pi * r**2 * h

def volume_boite(a,b,c):
    return a * b * c

##################################################


## Question 4 ##

def perimetre_aire_rectangle(a,b):
    p = 2*a+2*b
    A = a * b
    return p, A

def perimetre_aire_disque(r):
    p = 2 * pi * r
    A = pi * r**2
    return p, A


##############################
# Activité 3 - Turtue
##############################

## A FAIRE APRES LA FICHE "TORTUE"

## Question 1 ##

##############################

## Question 2 ##

##############################

## Question 3 ##


##############################
# Activité 4 - Fonctions
##############################

## Question 1 ##

##################################################

def reduction(age): 
    """Renvoie le pourcentage de réduction en fonction de l'âge"""

    if age <= 10:
        reduc = 50 
    elif age <= 18:
        reduc = 30
    elif age >= 60:
        reduc = 20
    else:
        reduc = 0

    return reduc

##################################################
def montant(tarif_normal,age):
    """Calcul le montant dû en fonction du tarif normal et de l'âge"""

    reduc = reduction(age)
    tarif = tarif_normal * (100-reduc)/100

    return tarif

# Test
montant_famille = montant(30,9) + 2*montant(20,16) + 2*montant(10,40)
print(montant_famille)


## Question 2 ##

##################################################

def calcul_est_exact(a,b,resultat):
    """Test si le résultat de a*b est correct"""

    reponse = a * b
    if reponse == resultat:
        return True
    else:
        return False

def test_multiplication(a,b,lang):
    if lang == "francais":
        question = "Combien vaut le produit a x b ?"
        reponse_juste = "Bravo !"
        reponse_fausse = "Eh non !"
    elif lang == "anglais":
        question = "How much is the product a x b?"
        reponse_juste = "Well done!"
        reponse_fausse = "It's wrong!"

    print("a =",a)
    print("b =",b)
    resultat = int(input(question))

    if calcul_est_exact(a,b,resultat):
        print(reponse_juste)
    else:
        print(reponse_fausse)

    return

# Test
test_multiplication(6,7,"anglais")



##############################
# Activité 5 - Egalité expérimentale
##############################


## Question 1 ##

##################################################
def valeur_absolue(x):
    if x >= 0:
        return x
    else:
        return -x

##################################################
def valeur_absolue_moins(x):
    return valeur_absolue(-x)

##################################################
def racine_du_carre(x):
    return sqrt(x**2)
    
##################################################
def egalite_experimentale_1(f,g):
    for i in range(-100,101):
        if f(i) != g(i):
            return False
    return True

# Test
print("--- Egalité experimentale, une variable ---")
print(egalite_experimentale_1(valeur_absolue,valeur_absolue_moins))
print(egalite_experimentale_1(valeur_absolue,racine_du_carre))

## Question 2 ##

##################################################
def f1(a,b):
    return (a+b)**2

##################################################
def f2(a,b):
    return a**2 + 2*a*b + b**2

##################################################
def f3(a,b):
    return (a-b)^3

##################################################
def f4(a,b):
    return a**3 - a**2*b  - a * b**2 + b**3

##################################################
def f5(a,b):
    return a**3 - a**2*b  + a * b**2 - b**3

################################################
def egalite_experimentale_2(f,g):
    for i in range(-100,101):
        for j in range(-100,101):
            if f(i,j) != g(i,j):
                return False
    return True

# Test
print("--- Egalité experimentale, deux variables ---")
print(egalite_experimentale_2(f1,f2))
print(egalite_experimentale_2(f3,f4))
print(egalite_experimentale_2(f3,f5))


## Question 3 ##

################################################
def sincos(x):
    return sin(x)**2 + cos(x)**2

################################################
def un(x):
    return 1

##################################################

precision = 0.00001   # = 10**-5
def egalite_experimentale_3(f,g):
    for i in range(-100,101):
        if abs(f(i) - g(i))> precision :
            return False
    return True

# Test
print("--- Egalité experimentale approchée ---")
print(egalite_experimentale_1(sincos,un))
print(sin(3)**2+cos(3)**2)
print(egalite_experimentale_3(sincos,un))


# Test avec d'autres inégalités, exemples :
# sin(2x) = 2 sin(x)cos(x)
# cos(pi/2 - x) = sin(x)
# et qq unes fausses ...

# Une égalité fausse mais experimentalement vraie
 ################################################
def g1(x):
    return sin(pi*x)

################################################
def g2(x):
    return 0

print(egalite_experimentale_3(g1,g2))  # toujours égal pour i =-100,...,+100
print(g1(1/2))  # et pourtant g1(0.5) n'est pas nul

##############################
# Activité 6 - Racine carrée
##############################

## Question 1 ##

##################################################

from math import *
rac = sqrt(56892)
print(rac)
print(floor(rac))
print(ceil(rac))

## Question 2 ##

##################################################
def calcul_racine_1(nombre):
    """
    Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière
    """    

    racine = 0
    while racine*racine <= nombre:
        racine = racine + 1

    return racine - 1

# Test 
# print("--- Racine carrée ---")
# print(calcul_racine_1(9))
# print(calcul_racine_1(10))
# print(calcul_racine_1(56892))


## Question 3 ##

##################################################
def calcul_racine_2(n):
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
# print("--- Racine carrée ---")
# print(calcul_racine_2(5))
# print(calcul_racine_2(10))
# print(calcul_racine_2(56892))

# print('test')
# for i in range(1,1000000):
#     # print(i)
#     if floor(sqrt(i)) != calcul_racine_2(i):
#         print('pb',i)   
# print('fin test')

##################################################
def calcul_racine_3(n):
    """
    Calcule la racine carrée entière d'un nombre
    Entrée : un entier
    Sortie : la racine carrée entière
    """    

    a = 1
    b = n
    while abs(a-b) > 1:
        a = (a+b)//2
        b = n//a
    return min(a,b)

# Test 
# print("--- Racine carrée ---")
# print(calcul_racine_3(3))
# print(calcul_racine_3(10))
# print(calcul_racine_3(56892))

# # print('test')
# # for i in range(1,1000000):
# #     # print(i)
# #     if floor(sqrt(i)) != calcul_racine_3(i):
# #         print('pb',i)   
# # print('fin test')