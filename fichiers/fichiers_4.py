
##############################
# Fichier
##############################

from math import *
import os


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