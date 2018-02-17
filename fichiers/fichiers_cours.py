
##############################
# Fichier
##############################

##############################
# Ecrire un fichier
##############################

# Création d'un fichier en écriture
fic = open("mon_fichier.txt","w")

# Première ligne
fic.write("Bonjour le monde\n")

# Deuxième ligne
ligne = "Coucou\n"
fic.write(ligne)

fic.close()

##############################
# Lire un fichier
##############################

fic = open("mon_fichier.txt","r")

for ligne in fic:
    print(ligne)

fic.close()