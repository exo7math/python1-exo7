
##############################
# Fichier
##############################

from random import *
import matplotlib.pyplot as plt

##############################
# Activité 2 - 
##############################

## Question 1 ##

def fichier_ventes():

    # Création d'un fichier en écriture
    nom_fichiers = "ventes.csv"
    fic = open(nom_fichiers,"w")

    # Listes nom
    liste_produits = ["Vélo VTT","Planche de surf","Chaussures de courses","Raquette de badminton","Ballon de volley"]

    # Lignes du haut
    fic.write("Meilleures ventes de la société 'Pentathlon'\n\n")
    fic.write(",2013,2014,2015,2016,2017,2018\n\n")

    for produit in liste_produits:
        
        # Génération des chiffres de vente au hasard
        ventes = ""
        for i in range(6):
            ventes = ventes + "," + str(randint(50,100)*10)

        ligne = produit + ventes  + "\n" 

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return

print("--- Fichier 'ventes.csv' ---")
fichier_ventes()


## Question 2 ##

def afficher_ventes():

    # Fichier à lire
    fichier_ventes = "ventes.csv"
    fic_in = open(fichier_ventes,"r")

    num_ligne = 0
    for ligne in fic_in:
        if num_ligne > 3: # on oublie les lignes de titres
            liste = ligne.split(",")
            donnees = [float(x) for x in liste[1:]]
            plt.plot(donnees)

        num_ligne += 1

    # Fermeture des fichiers
    fic_in.close()

    # Affichage
    plt.grid()
    plt.show()

    return

print("--- Affichages graphique de 'ventes.csv' ---")
afficher_ventes()

