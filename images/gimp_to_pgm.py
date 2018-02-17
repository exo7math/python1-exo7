
##############################
# Conversion du format Gimp pgm
# vers notre format basique pgm
##############################

import os

def gimp_to_pgm(fichier):

    # Fichier à lire
    fic_in = open("input/"+fichier+".pgm","r")

    # Fichier à écrire
    nom, extension = os.path.splitext(fichier)
    nouv_nom = "input/"+nom + "_new"+".pgm"
    fic_out = open(nouv_nom,"w")


    i = 0    # Numéro de ligne
    j = 0  # Numéro de colonne
    
    nouv_ligne = ""
    
    for ligne in fic_in:
        if i == 0:
            fic_out.write("P2\n")   # Image en niveaux de gris

        elif i == 1:
            pass  
                              # Ne garde pas le commentaire 
        elif i == 2:                 # Garder les lignes/colonnes
            liste_ligne = ligne.split()
            nb_col = int(liste_ligne[0])
            nb_lig = int(liste_ligne[1])
            fic_out.write(ligne)  

        elif i == 3:     # Garder les niveaux
            fic_out.write(ligne)  

        else:
            ligne = ligne.split()[0]

            nouv_ligne = nouv_ligne + ligne + " "
                
            j = j + 1 

            if j == nb_col:
                nouv_ligne = nouv_ligne + "\n"
                fic_out.write(nouv_ligne)
                nouv_ligne = ""
                j = 0
        i = i + 1

    # Fermeture des fichiers
    fic_in.close()
    fic_out.close()
    return

##################################

# gimp_to_pgm("pi_gimp")
# gimp_to_pgm("chat_gimp")
# gimp_to_pgm("reveil_gimp")
gimp_to_pgm("surf_gimp")