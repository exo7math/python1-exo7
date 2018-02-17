
##############################
# Listes I
##############################


##############################
# Activité 4 - Arithmétique
##############################

## Question 1 ##

##############################
def facteurs_premiers(n):
    liste = []
    d = 2
    while d <= n:
        if n%d == 0:
            liste = liste + [d]
            n = n // d
        else:
            d = d + 1
    # if len(liste)==0:   # Cas d'un nb premier
    #     liste = [n]
    return liste


# Test
print("--- Facteurs premiers ---")
n = 2*2*2*3*7*7*11
print(n)
print(facteurs_premiers(2*2*2*3*7*7*11))


## Question 2 ##

##############################
def liste_premiers(n):
    liste = list(range(2,n))
    for d in range(2,n):
        for k in liste:
            if k%d == 0 and k != d:
                liste.remove(k)
    return liste

print("--- Liste des nombres premiers ---")
print(liste_premiers(100))

