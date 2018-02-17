
##############################
# Premiers pas
##############################


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
# Questions

# Q1
# pgcd
print(gcd(13*121,13*122))

a = 101*103
b = 102*103
print(a,b)
ppcm = a * b // gcd(a,b)
print(ppcm)


# Q2
# Valeur absolue
x = 3.85
print(abs(x**2-15))
print(round(2*x))
print(floor(3*x))
print(ceil(4*x))


# Q3
# Angle
angle = pi/7
x = cos(angle)**2 + sin(angle)**2
print(x)

