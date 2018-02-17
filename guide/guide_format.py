
##############################
# Guide - Mise en formae
##############################

# Alignement à gauche
print('{:10}'.format('Test'))

# Alignement à droite
print('{:>10}'.format('Test'))

# Centré
print('{:^10}'.format('Test'))



# Entier
print('{:d}'.format(456))

# Entier sur longueur fixée
print('{:6d}'.format(456))

# Entier avec 0 non significatifs
print('{:06d}'.format(456))



# Nombre flottant
print('{:f}'.format(3.141592653589793))

# Flottant avec nb de chiffesd après la virgules
print('{:.8f}'.format(3.141592653589793))

# Nombre flottant sur longueur fixée
print('{:8.4f}'.format(3.141592653589793))

# Flottant avec 0 non significatifs
print('{:08.4f}'.format(3.141592653589793))
