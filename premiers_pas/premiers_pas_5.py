
##############################
# Premiers pas
##############################


##############################
# Activité 5 - Boucle "pour" (suite)
##############################

# Questions

# Q1
# Sommes des carrés
n = 20
somme = 0
for i in range(n+1):
    somme = somme + i**2
print(somme)


# Q2
# Produits
n = 19
produit = 1
for i in range(1,n+1,2):
    produit = produit * i
print(produit)


# Q3
# Tables de multiplications
for a in range(11):
    for b in range(11):
        print(a,"x",b,"=",a*b)