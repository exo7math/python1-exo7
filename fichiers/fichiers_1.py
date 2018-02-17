
##############################
# Fichier
##############################

from random import *


##############################
# Activité 1 - Ecrire un fichier
##############################

## Question 1 ##

def ecrire_fichier_notes():

    # Création d'un fichier en écriture
    nom_fichier = "notes.txt"
    fic = open(nom_fichier,"w")

    # Listes nom
    liste_prenoms = ["Gargamel","Robin","Hermione","Arsène","Alice","James","Tintin"]
    liste_noms = ["Skywalker","Lupin","Voldemort","Tchoupi","Bond","Tartuffe","Dubois"]

    for i in range(7):
        prenom = choice(liste_prenoms)
        nom = choice(liste_noms)
        notes = str(randint(10,40)/2) + " " + str(randint(10,40)/2) + " " + str(randint(10,40)/2)
        ligne = prenom + " " + nom + " " + notes + "\n"

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return

# Test

print("--- Fichier 'notes.txt' ---")
ecrire_fichier_notes()


## Question 2 ##

def ecrire_fichier_moyennes():

    # Fichier à lire
    fichier_notes = "notes.txt"
    fic_in = open(fichier_notes,"r")

    # Fichier à écrire
    fichier_moyennes = "moyennes.txt"
    fic_out = open(fichier_moyennes,"w")

    for ligne in fic_in:
        liste = ligne.split()
        moyenne = (float(liste[2])+float(liste[3])+float(liste[4]))/3
        #moyenne_str = str(moyenne)
        moyenne_str = '{0:.2f}'.format(moyenne)
        nouv_ligne = liste[0] + " " + liste[1] + " " + moyenne_str + "\n"
        fic_out.write(nouv_ligne)

    # Fermeture des fichiers
    fic_in.close()
    fic_out.close()
    return

print("--- Fichier 'moyenne.txt' ---")
ecrire_fichier_moyennes()




