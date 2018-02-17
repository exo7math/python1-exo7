
##############################
# Listes II - Cours
##############################

##############################
# C1 - Trancher de listes

maliste = [7,2,4,5,3,10,9,8,]
print(maliste[3:5])
print(maliste[3:])
print(maliste[:6])
print(maliste[-1])
#print(maliste[::2])


##############################
# C2 - Liste par compréhension

maliste = [1,2,3,4,5,6,7,6,5,4,3,2,1]
liste_doubles = [ 2*x for x in maliste ]
liste_carres = [ x**2 for x in maliste ]
liste_partielle = [x for x in maliste if x > 2]

print(liste_doubles)
print(liste_carres)
print(liste_partielle)


##############################
# C3 - Liste de listes

tableau = [ [2,14,5], [3,5,7], [15,19,4], [8,6,5] ]
print(tableau[0])
print(tableau[1])
print(tableau[0][0])
print(tableau[0][1])
print(tableau[2][1])


