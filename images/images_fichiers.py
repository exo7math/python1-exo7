
##############################
# Fichier
##############################

import os

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
    nb_col = 300
    nb_lig = 200
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")


    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            coul = (i+j)//10 % 2
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
    nb_col = 200
    nb_lig = 200
    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")    

    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            R = (i*j) % 256   # niveau de rouge
            V = i % 256        # niveau de vert
            B = (i+j)//3 % 256   # niveau de bleu            

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
inverser_couleurs_nb("simple_nb.pbm")


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


