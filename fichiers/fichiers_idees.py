
##############################
# Fichier
##############################

from math import *
from random import *
import matplotlib.pyplot as plt

import os


##############################
# Activité 1 - Ecrire un fichier
##############################

## Question 1 ##

def ecrire_fichier_notes():

    # Création d'un fichier en écriture
    nom_fichier = "notes.txt"
    fic = open(nom_fichier,"w")

    # Listes nom
    liste_prenoms = ["Gargamel","Robin","Hermione","Arsène","Alice"]
    liste_noms = ["Skywalker","Lupin","Voldemort","Tchoupi",]

    for i in range(10):
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
# afficher_ventes()



##############################
# Activité 3 - Images
##############################


## Question 1 ##

def ecrire_fichier_image_nb():

    # Création d'un fichier en écriture
    nom_fichier = "image_nb.pbm"
    fic = open(nom_fichier,"w")

    # Entete
    fic.write("P1\n")  # Image noir et blanc
    nb_col = 100
    nb_lig = 50
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")


    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            # coul = randint(0,1)     # 0 et 1 au hasard
            coul = (i+j)//50 % 2
            ligne = ligne + str(coul) + " "
        ligne = ligne + "\n"

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return
# Test

print("--- Fichier 'image.pbm' ---")
ecrire_fichier_image_nb()

## Question 2 ##

def ecrire_fichier_image_gris():

    # Création d'un fichier en écriture
    nom_fichier = "image_gris.pgm"
    fic = open(nom_fichier,"w")

    # Entete
    fic.write("P2\n")  # Image en niveaux de gris
    nb_col = 200
    nb_lig = 200
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")    

    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            coul = (i**2 + j**2) % 256   # un niveau de gris en fonction de i et j
            ligne = ligne + str(coul) + " "    
        ligne = ligne + "\n"

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return

# Test

print("--- Fichier 'image.pgm' ---")
ecrire_fichier_image_gris()


## Question 3 ##

def ecrire_fichier_image_coul():

    # Création d'un fichier en écriture
    nom_fichier = "image_coul.ppm"
    fic = open(nom_fichier,"w")

    # Entete
    fic.write("P3\n")  # Image en couleurs
    nb_col = 100
    nb_lig = 100
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")    

    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            R = (i*j) % 256   # niveau de rouge
            V = i % 256        # niveau de vert
            B = (i+j) % 256   # niveau de bleu            

            ligne = ligne + str(R) + " " + str(V) + " "  + str(B) + "   "  
        ligne = ligne + "\n"

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return

# Test

print("--- Fichier 'image.ppm' ---")
ecrire_fichier_image_coul()




## Question 4 ##

def inverser_couleurs_nb(fichier):

    # Fichier à lire
    fic_in = open(fichier,"r")

    # Fichier à écrire
    nom, extension = os.path.splitext(fichier)
    nouv_nom = nom + "_inverse"+extension 
    fic_out = open(nouv_nom,"w")


    i = 0    # Numéro de ligne
    for ligne in fic_in:

        if i<2:     # Garder les 2 premières lignes
            fic_out.write(ligne)  
        else:
            liste = ligne.split()
            nouv_ligne = ""
            for l in liste:
                if l == "1":
                    nouv_ligne = nouv_ligne + "0 "
                else:
                    nouv_ligne = nouv_ligne + "1 "

            nouv_ligne = nouv_ligne + "\n"
            fic_out.write(nouv_ligne)

        i = i + 1

    # Fermeture des fichiers
    fic_in.close()
    fic_out.close()
    return

print("--- Inversion des noirs et blancs ---")
inverser_couleurs_nb("image_nb.pbm")


## Question 4 ##


def formule_couleur_vers_gris(R,V,B):
    gris = round(0.21*R + 0.72*V + 0.07*R)
    return gris

def couleurs_vers_gris(fichier):

    # Fichier à lire
    fic_in = open(fichier,"r")

    # Fichier à écrire
    nom, extension = os.path.splitext(fichier)
    nouv_nom = nom + "_gris"+".pgm"
    fic_out = open(nouv_nom,"w")


    i = 0    # Numéro de ligne
    for ligne in fic_in:
        if i == 0:
            fic_out.write("P2\n")  # Image en niveaux de gris
        elif i == 1 or i == 2:     # Garder les lignes 2 et 3
            fic_out.write(ligne)  
        else:
            liste = ligne.split()
            nouv_ligne = ""

            j = 0  # Numéro de colonne
            while j < len(liste):
                R = int(liste[j])
                V = int(liste[j+1])
                B = int(liste[j+2])
                gris = formule_couleur_vers_gris(R,V,B)
                nouv_ligne = nouv_ligne + str(gris) + " "
                
                j = j + 3

            nouv_ligne = nouv_ligne + "\n"
            fic_out.write(nouv_ligne)

        i = i + 1

    # Fermeture des fichiers
    fic_in.close()
    fic_out.close()
    return

print("--- Couleurs vers niveaux de gris ---")
couleurs_vers_gris("image_coul.ppm")





##############################
# Activité 4 - Distances entre les villes
##############################

from math import *

## Question 1 ##

def distance_xy(x1,y1,x2,y2):
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )

## Question 2 ##

def fichier_distances_xy(fichier):
    # Fichier à lire
    fic_in = open(fichier,"r")

    liste_villes = []

    for ligne in fic_in:
        liste_villes = liste_villes + [ligne.split()]
        
    # Fermeture du fichier
    fic_in.close()

    # Fichier à écrire
    nom, extension = os.path.splitext(fichier)
    nouv_nom = nom + "_distances"+".txt"
    fic_out = open(nouv_nom,"w")

    ligne = '{:>10s}'.format("")
    for v in liste_villes: 
        nom = v[0]
        ligne = ligne + '{:>10s}'.format(nom) +" "

    fic_out.write(ligne + "\n")

    for v1 in liste_villes:
        nom1 = v1[0]
        x1 = float(v1[1])
        y1 = float(v1[2])

        ligne = '{:10s}'.format(nom1)

        for v2 in liste_villes:
            nom2 = v2[0]
            x2 = float(v2[1])
            y2 = float(v2[2])

            d = distance_xy(x1,y1,x2,y2)

            ligne = ligne + '{:10d}'.format(round(d)) + " "

        fic_out.write(ligne + "\n")

    return

print("--- Villes xy ---")
fichier_distances_xy("villes_xy.txt")


## Question 3 ##

def degres_vers_radians(a):
    return 2*pi*a/360

def distance_approx_lat_long(lat1,long1,lat2,long2):
    R = 6371  # rayon (moyen) de la Terre
    x = (long2-long1)*cos( (lat1+lat2)/2 )
    y = lat2-lat1
    d = R * sqrt( x**2 + y**2 )
    return d

# Test 
Paris = (48.853,2.350)
Paris_radians = (degres_vers_radians(Paris[0]),degres_vers_radians(Paris[1]))

New_York = (40.713,-74.006)
New_York_radians = (degres_vers_radians(New_York[0]),degres_vers_radians(New_York[1]))

print("--- Distances approchées Terre ---")
d = distance_approx_lat_long(*Paris_radians,*New_York_radians)
print(d)


def distance_lat_long(lat1,long1,lat2,long2):
    R = 6371  # rayon (moyen) de la Terre
    a = (sin((lat2-lat1)/2))**2 + cos(lat1)*cos(lat2)*(sin((long2-long1)/2))**2
    d = 2 * R * atan2(sqrt(a),sqrt(1-a))
    return d

# Test 
print("--- Distances exactes Terre ---")
d = distance_lat_long(*Paris_radians,*New_York_radians)
print(d)


## Question 3 ##

def fichier_distances_lat_long(fichier):
    # Fichier à lire
    fic_in = open(fichier,"r")

    liste_villes = []

    for ligne in fic_in:
        liste_villes = liste_villes + [ligne.split()]
        
    # Fermeture du fichier
    fic_in.close()

    # Fichier à écrire
    nom, extension = os.path.splitext(fichier)
    nouv_nom = nom + "_distances"+".txt"
    fic_out = open(nouv_nom,"w")

    ligne = '{:>12s}'.format("")
    for v in liste_villes:
        print(v) 
        nom = v[0]
        ligne = ligne + '{:>12s}'.format(nom) +" "

    fic_out.write(ligne + "\n")

    for v1 in liste_villes:
        nom1 = v1[0]
        lat1 = degres_vers_radians(float(v1[1]))
        long1 = degres_vers_radians(float(v1[2]))

        ligne = '{:12s}'.format(nom1)

        for v2 in liste_villes:
            nom2 = v2[0]
            lat2 = degres_vers_radians(float(v2[1]))
            long2 = degres_vers_radians(float(v2[2]))

            d = distance_lat_long(lat1,long1,lat2,long2)

            ligne = ligne + '{:12d}'.format(round(d)) + " "

        fic_out.write(ligne + "\n")

    return

print("--- Villes lat_long ---")
fichier_distances_lat_long("villes_lat_long.txt")