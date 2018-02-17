
##############################
# Images dynamiques
##############################

import os   # pour les fichiers images


##############################
# Activité 1 - Photomaton
##############################



##############################
## Depuis autres fiches ##
def afficher_tableau(tableau):
    
    n = len(tableau)
    m = len(tableau[0])

    for i in range(n):
        for j in range(m):
            print('{:>3d}'.format(tableau[i][j])," ", end="")
        print()

    return


##############################
## Question 1 ##

def transformation(i,j,n):
    if i%2 == 0 and j%2 == 0:
        ii = i//2
        jj = j//2
    if i%2 == 0 and j%2 == 1:
        ii = i//2
        jj = (n+j)//2    
    if i%2 == 1 and j%2 == 0:
        ii = (n+i)//2
        jj = j//2
    if i%2 == 1 and j%2 == 1:
        ii = (n+i)//2
        jj = (n+j)//2    

    return ii,jj

## Test ##
print("--- Transformation du photomaton ---")
print(transformation(1,1,6))


##############################
## Question 2 ##

def photomaton(tableau):
    n = len(tableau)
    nouv_tableau = [[0 for j in range(n)] for i in range(n)]   

    for i in range(n):
        for j in range(n):
            ii, jj = transformation(i,j,n)
            nouv_tableau[ii][jj] = tableau[i][j]

    return nouv_tableau

## Test ##
print("--- Transformation du photomaton ---")
tableau = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
tableau_transforme = photomaton(tableau)
afficher_tableau(tableau)
print("---")
afficher_tableau(tableau_transforme)


##############################
## Question 3 ##
def photomaton_iterer(tableau,k):
    n = len(tableau)
    tab = [[tableau[i][j] for j in range(n)] for i in range(n)]

    for i in range(k):
        tab = photomaton(tab)

    return tab


## Test ##
print("--- Itération de la transformation du photomaton ---")
tableau = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
afficher_tableau(tableau)
for k in range(1,10):
    tableau_itere = photomaton_iterer(tableau,k)
    # Pas très malin, car repart du début à chaque fois
    print("--- k =",k,"---")
    afficher_tableau(tableau_itere)



##############################
# Activité 2 - Conversion tableau/image
##############################


##############################
## Question 1 ##
def tableau_vers_image(tableau,nom_image):

    # Création d'un fichier en écriture
    nom_fichier = "output/" + nom_image + ".pgm"
    fic = open(nom_fichier,"w")

    # Entete
    fic.write("P2\n")  # Image en niveaux de gris

    nb_lig = len(tableau)
    nb_col = len(tableau[0])

    fic.write(str(nb_col) + " " + str(nb_lig) + "\n")
    niveaux = 255
    fic.write(str(niveaux) + "\n")    

    for i in range(nb_lig):
        ligne = ""
        for j in range(nb_col):
            coul = tableau[i][j]
            ligne = ligne + str(coul) + " "    
        ligne = ligne + "\n"

        # Ecriture dans le fichier
        fic.write(ligne)

    # Fermeture du fichier
    fic.close()

    return


## Test ##
print("--- Tableau vers image ---")
tableau =  [[128, 192, 128, 192, 128], [224, 0, 228, 0, 224], [228, 228, 228, 228, 228], [224, 64, 64, 64, 224], [192, 192, 192, 192, 192]]
tableau_vers_image(tableau,"test")  


##############################
## Question 2 ##

def image_vers_tableau(nom_image):

    # Création d'un fichier en écriture
    nom_fichier = "input/" + nom_image + ".pgm"
    fic = open(nom_fichier,"r")

    i = 0    # Numéro de ligne
    for ligne in fic:
        if i == 1:     # Garder les 2 premières lignes
            liste_ligne = ligne.split()
            nb_col = int(liste_ligne[0])
            nb_lig = int(liste_ligne[1])

            tableau = [[ 0 for j in range(nb_col)] for i in range(nb_lig)]
        elif i > 2:
            liste = ligne.split()
            for j in range(nb_col):
                tableau[i-3][j] = int(liste[j])

        i = i + 1

    # Fermeture du fichier
    fic.close()

    return tableau

print("--- Image vers tableau ---")

test_tableau = image_vers_tableau("test") 
print(test_tableau)
afficher_tableau(test_tableau)


##############################
## Depuis la fiche "Fichiers" ##
## Permet d'avoir un exemple de fichier

def ecrire_fichier_image_gris():

    # Création d'un fichier en écriture
    nom_fichier = "input/image_gris.pgm"
    fic = open(nom_fichier,"w")

    # Entete
    fic.write("P2\n")  # Image en niveaux de gris
    nb_col = 256
    nb_lig = 256
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
# ecrire_fichier_image_gris()


##############################
# Activité 1bis - Photomaton
##############################

##############################
## Question 4 ##

def photomaton_images(nom_image,kmax):
    tableau = image_vers_tableau(nom_image)
    tableau_vers_image(tableau,nom_image+"_photo_"+str(0)) # image initiale

    n = len(tableau)
    tab = [[tableau[i][j] for j in range(n)] for i in range(n)]

    for k in range(1,kmax+1):
        tab = photomaton(tab)
        tableau_vers_image(tab,nom_image+"_photo_"+str(k))

    return

## Test ##
# photomaton_images("image_gris",8)
# photomaton_images("pi_gimp_new",8)
# photomaton_images("chat_gimp_new",8)



##############################
# Activité 3 - Transfomation du boulanger
##############################

##############################
## Question 1 ##

def boulanger_etirer(tableau):
    n = len(tableau)
    nouv_tableau = [[0 for j in range(2*n)] for i in range(n//2)]   

    for i in range(n//2):
        for j in range(2*n):
            if j%2 == 0:
                nouv_tableau[i][j] = tableau[2*i][j//2]
            else:
                nouv_tableau[i][j] = tableau[2*i+1][j//2]

    return nouv_tableau


print("--- Boulanger : étirer tableau ---")
tableau = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
tableau_etire = boulanger_etirer(tableau)
afficher_tableau(tableau)
print("---")
afficher_tableau(tableau_etire)


##############################
## Question 2 ##

def boulanger_replier(tableau):
    n = 2*len(tableau)

    nouv_tableau = [[0 for j in range(n)] for i in range(n)]  

    # partie haute
    for i in range(n//2):
        for j in range(n):
            nouv_tableau[i][j] = tableau[i][j]

     # partie basse
    for i in range(n//2,n):
        for j in range(n):
            nouv_tableau[i][j] = tableau[n//2 - i - 1][2*n-1-j]             

    # for i in range(n//2):
    #     for j in range(n):
    #         nouv_tableau[n-i-1][j] = tableau[i][2*n-1-j]  
    

    return nouv_tableau    

print("--- Boulanger : replier tableau ---")
tableau_replie = boulanger_replier(tableau_etire)
afficher_tableau(tableau_etire)
print("---")
afficher_tableau(tableau_replie)


##############################
## Question 3 ##

def boulanger_iterer(tableau,k):
    n = len(tableau)
    tab = [[tableau[i][j] for j in range(n)] for i in range(n)]

    for i in range(k):
        tabb = boulanger_etirer(tab)
        tab = boulanger_replier(tabb)

    return tab


print("--- Boulanger : itérer tranformation tableau ---")
tableau = [ [1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16] ]
afficher_tableau(tableau)
for k in range(1,10):
    tableau_itere = boulanger_iterer(tableau,k)
    print("--- k =",k,"---")
    afficher_tableau(tableau_itere)

 

##############################
## Question 4 ##

def boulanger_images(nom_image,kmax):

    tableau = image_vers_tableau(nom_image)
    tableau_vers_image(tableau,nom_image+"_boul_"+str(0)) # image initiale

    n = len(tableau)
    tab = [[tableau[i][j] for j in range(n)] for i in range(n)]

    for k in range(1,kmax+1):
        tabb = boulanger_etirer(tab)
        tab = boulanger_replier(tabb)
        tableau_vers_image(tab,nom_image+"_boul_"+str(k))

    return

## Test ## 
# boulanger_images("image_gris",17)
# boulanger_images("pi_gimp_new",17)
# boulanger_images("chat_gimp_new",17)
# boulanger_images("reveil_gimp_new",17)
# boulanger_images("surf_gimp_new",15)
