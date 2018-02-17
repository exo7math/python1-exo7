
##############################
# Tant que - Booléen - Arithmétiques
##############################

##############################
# Cours 2 - break
##############################




##############################
# Exemple 1

# Compte à rebours
n = 10
while True:     # Boucle infinie
    print(n)
    n = n - 1
    if n<0:
        break   # Arrêt immédiat

# Mieux (avec un drapeau)
n = 10
termine = False
while not termine:
    print(n)
    n = n - 1   
    if n<0:
        termine = True

# Encore mieux (en reformulant)
n = 10
while n >= 0:
    print(n)
    n = n - 1

##############################
# Exemple 2

# Racine carrée entière
n = 777
for i in range(100):
    if i**2 >= n:
        break
print(i-1)


# Mieux
n = 777
i = 0 
while (i**2 < n)  and (i < 100):
    i = i + 1
print(i-1) 


##############################
# Exemple 3

from math import *

# Racines carrées des éléments d'une liste
liste = [3,7,0,10,-1,12]
for element in liste:
    if element < 0:
        break
    print(sqrt(element))


# Mieux avec try/except
liste = [3,7,0,10,-1,12]
for element in liste:
    try: 
        print(sqrt(element))
    except:
        print("Attention, je ne sais pas calculer la racine de",element)







  