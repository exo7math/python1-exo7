
##############################
# Bitcoin
##############################


##############################
# Activité 1 - Preuve de travail
##############################

from time import *

# p = 101  # Un petit nombre premier
# p = 1097
# p = 10651
# p = 100109
# p = 1300573
p = 15486869 # Un moyen nombre premier
# p = 179426321  
# p = 2276856017 # Un grand nombre premier
# p = 32416187567


## Question 1 ##

def verification(x,y):
    xcarre = (x ** 2) % p
    if xcarre == y:
        return True
    else:
        return False


# Test
print("--- Vérification x^2 = y modulo p ---")      




debut_chrono = time()

x = 6543210
# y = (x**2) % p; print(y)
y = 8371779  
print(verification(x,y))

fin_chrono = time()
total_chrono = fin_chrono - debut_chrono
print("Temps de calcul (en secondes) :",total_chrono)


## Question 2 ##

def racine(y):
    for x in range(p):
        res = (x ** 2 - y) % p
        if res == 0:
            return x
    return None


# Test
print("--- Recherche de x tq x^2 = y modulo p ---")  

debut_chrono = time()

y = 8371779
x = racine(y)
print(x, (x**2-y) % p)

fin_chrono = time()
total_chrono = fin_chrono - debut_chrono
print("Temps de calcul (en secondes) :",total_chrono)


## Question 3 ##

def racine_approchee(y,marge):
    for x in range(p):
        res = (x ** 2 - y) % p
        if res <= marge:
            return x        
    return None


print("--- Recherche approchée de x tq x^2 = y modulo p ---")  

debut_chrono = time()

y = 8371779
marge = 20
x = racine_approchee(y,marge)
print("x =",x, "erreur =",(x**2-y) % p)

fin_chrono = time()
total_chrono = fin_chrono - debut_chrono
print("Temps de calcul :",total_chrono)



## Pour l'intro ##

p = 15486869
y = 12345 ** 2
print(y % p)
x = racine(y)
print(x, (x**2-y) % p)