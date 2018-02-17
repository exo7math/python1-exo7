
##############################
# Listes I
##############################

##############################
# Cours 1 - Visualiser une liste

liste_carres = []   # On part d'un liste vide

for i in range(10):
    liste_carres.append(i**2)   # On ajoute un carré

print(liste_carres)

##############################
# Cours 4 - Visualiser une liste

import matplotlib.pyplot as plt

# liste1 = [3,5,9,8,0,3]
# liste2 = [4,7,7,2,8,9]
# plt.plot(liste1,color="red")
# plt.plot(liste2,color="blue")
# plt.grid()
# plt.show()

liste_x = [2, 3, 5, 7, 9]
liste_y = [4, 9,25,49,81]
plt.plot(liste_x,liste_y,color="red")
plt.grid()
plt.show()

