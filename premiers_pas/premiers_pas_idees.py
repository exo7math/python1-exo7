
##############################
# Premiers pas - Hello world!
##############################

##############################
# Activité 1 - Nombres
##############################

##############################
# Cours

# Afficher une phrase
print("Bonjour le monde !")

# Addition
5+7
print(5+7)

# Multiplication
print(6*7)

print(3*(12+5))

print(3*1.5)

# Puissance

print(3**2)

print(10**-3)

# Division réelle

print(14/4)

print(1/3)

# Division entière et modulo

print(14//4)

print(14%4)



##############################
# Questions

# Q1 - Nombre de secondes dans un siècle
print(100 * 365 * 24 * 60 * 60)

# Q2 A partir dans quand plus grand qu'un milliard
print((1+2)*(3+4)*(5+6)*(7+8)*(9+10)*(11+12)*(13+14)*(14+15))

# Trois derniers chiffres de 123456789 * 123456789 * ...
print(123456789 ** 7)


# Premier 1/n avec période 7
print(1/7)
print(1/239)


# Trouver un nb connaissant deux divisions et un reste
# for n in range(1175,1190):
#     print(n,n//11,n//13,n%7)

print(1182//11)
print(1182//13)
print(1182%7)







##############################
# Activité 2 - Variables
##############################


##############################
# Cours

# C1 - variables
a = 3  # Une variable
b = 5  # Une autre variable

print("La somme vaut",a+b)   # Affiche la somme
print("Le produit vaut",a*b) # Affiche le produit

c = b**a     # Nouvelle variable...
print(c)     # ... qui s'affiche


# C2 - aire d'un triangle
base = 8
hauteur = 3
surface = base * hauteur / 2
print(surface)
# print(Surface)  # !! Erreur !!


# C3 - ajout
S = 1000
S = S + 100
S = S + 200
S = S - 50
print(S)

##############################

# Q1 - Surfaces - Volumes

# Trapèze : bien nommé les choses
b, B, h = 3, 5, 4
surface = (b + B) * h / 2
print("La surface vaut",surface)

# Boîtes
L, l, h = 10,8,3
volume = L * l * h
print(volume)

# Boules
PI = 3.14
R = 10
volume = 4/3 * PI * R**3
print(volume)


# Q2 - Remettre dans l'ordre de sorte qu'à la fin x = 46
x = 7
y = 2*x
y = y - 1
x = x + 3*y 
print(x)


# Q3 - intérêts de 10%
S = 1000
S = S * 1.1
S = S * 1.1
S = S * 1.1


# Q4 - Bon choix afin d'échanger a et b

# Mauvais
a = 11
b = 9
a = b
b = a
print(a,b)

# Mauvais
a = 11
b = 9
c = b
a = b
b = c
print(a,b)

# Mauvais
a = 11
b = 9
c = a
a = c
c = b
b = c

print(a,b)

# Bon
a = 11
b = 9
c = a
a = b
b = c
print(a,b)



##############################
# Activité 3 - Utiliser des fonctions
##############################


##############################
# Cours

# C1 - fonctions

print("Coucou")

x = float("+1.234567")
print(x)


# C2 - module math

from math import *

x = sqrt(2)
print(x)
print(x**2)

# C3 - fonction trigo

angle = pi/2
print(angle)
print(sin(angle))


# C4 - décimal vers entier

x = 3.6
print(round(x))
print(floor(x))
print(ceil(x))


##############################

# Q1 - pgcd

print(gcd(13*121,13*122))

a = 101*103
b = 102*103
print(a,b)
ppcm = a * b // gcd(a,b)
print(ppcm)


# Q2 - valeur absolue

x = 3.8
print(abs(x**2-15))
print(round(2*x))
print(floor(3*x))
print(ceil(4*x))


# Q3 - angle

angle = pi/7
x = cos(angle)**2 + sin(angle)**2
print(x)



##############################
# Activité 4 - Boucle "pour"
##############################

##############################
# Cours

# C1 - Boucle "for"

for i in range(10):
    print(i*i)


# C2 - Boucle "for"
somme = 0
for i in range(20):
    somme = somme + i
print(somme)


# C3
print(list(range(10,20)))
print(list(range(10,20,2)))   


# C4 - Imbrication de boucles
for x in [10,20,30,40,50]:
    for y in [3,7]:
        print(x+y)

##############################


# Q1 - Cubes

for i in range(101):
    print(i**3)

for i in range(10,21):
    print(i**4)

for i in range(0,101,5):
    print(sqrt(i))


# Q2 - Puissances de 2

for k in range(1,11):
    print(2**k)


# Q3 - Minimum d'une fonction par balayage

for i in range(101):
    x = i/100
    y = x**3 - x**2 - 1/4*x + 1
    print(x,y)


# Q4 - Aire d'un disque qui vaut 100

for i in range(50):
    R = i/10
    V = 4/3 * 3.14 * R**3
    print(R,S)    



##############################
# Activité 5 - Boucle "pour" (suite)
##############################

# Q1 - Sommes des carrés

n = 20
somme = 0
for i in range(n+1):
    somme = somme + i**2
print(somme)


# Q2 - Produits

produit = 1
for i in range(1,20,2):
    produit = produit * i
print(produit)


# Q3 - Tables de multiplications

for a in range(11):
    for b in range(11):
        print(a,"x",b,"=",a*b)