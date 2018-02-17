
##############################
# Premiers pas
##############################


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
aire = base * hauteur / 2
print(aire)
# print(Aire)  # !! Erreur !!


# C3 - ajout

S = 1000
S = S + 100
S = S + 200
S = S - 50
print(S)


##############################
# Questions

# Q1

# Aires - Volumes

# Trapèze : bien nommé les choses
B, b, h = 7, 4, 3
aire = (B + b) * h / 2
print("L'aire vaut",aire)

# Boîtes
L, l, h = 10,8,3
volume = L * l * h
print(volume)

# Boules
PI = 3.14
R = 10
aire = PI * R**2
print(aire)


# Q2 
# Remettre dans l'ordre de sorte qu'à la fin x = 46
x = 7
y = 2*x
y = y - 1
x = x + 3*y 
print(x)


# Q3
# Intérêts de 10%
S = 1000
S = S * 1.1
S = S * 1.1
S = S * 1.1


# Q4 

# Bon choix afin d'échanger a et b

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

