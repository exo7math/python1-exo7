
##############################
# Test - tkinter - 
##############################

from tkinter import *
from tkinter.font import Font

from coupures_projet import *


##################################################
##################################################


# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Format de la page de texte
largeur = 500
hauteur = 400
indentation = 30 # Pour les listes
espace_entre_lignes = 18
longueur_espace = 7
longueur_ligne = largeur


# Couleurs
couleur_fond = "white" #"lightgray"
couleur_texte = "black"

# Cadre
#canvas.create_rectangle(10,10,largeur,hauteur,width=2,fill=couleur_fond)

# Fontes
fonte_texte = Font(family="Times", size=12)
fonte_italique = Font(family="Times", slant="italic", size=12)
fonte_gras =  Font(family="Times", weight="bold", size=12)
fonte_titre = Font(family="Times", weight="bold", size=20)
fonte_sous_titre = Font(family="Times", weight="bold", size=16)


##################################################
def choix_fonte(mode,en_gras,en_italique):
    if mode == "titre":
        fonte = fonte_titre
    elif mode == "sous_titre":
        fonte = fonte_sous_titre
    else:       # Mode "texte" ou "liste"
        if en_gras:
            fonte = fonte_gras
        elif en_italique:
            fonte = fonte_italique
        else:
            fonte = fonte_texte

    return fonte




##################################################
def formater_paragraphe(par):

    # Déterminataion du mode
    if par[0:2] == "##":       # Sous_titre
        mode = "sous_titre"
        par = par[2:]          # Supprime les ##
    elif par[0] == "#":        # Titre 
        mode = "titre"
        par = par[1:]          # Supprime le #
    elif par[0] == "+":
        mode = "liste"
        par = u'\u2022' + par[1:]    # Remplace le "+" par un rond
    else:
        mode = "texte"


    liste_format_mots = []

    # Gras / italique
    en_gras = False
    en_italique = False

    for mot in par.split():
        if mot == "**":  # Bascule gras / pas gras
            en_gras = not(en_gras) 
            mot = ""           

        if mot == "*":       # Bascule italique / pas italique
            en_italique = not(en_italique)          
            mot = "" 

        if mot != "":
            liste_format_mots += [[mot,mode,en_gras,en_italique]]

    return liste_format_mots


# Test 

#print(formater_paragraphe("# Titre Hello World"))
#print(formater_paragraphe("## Sous titre Hello"))
#print(formater_paragraphe("Hello"))
#print(formater_paragraphe("Hello ** GRAS **   * Italique *  ** TRES GRAS ** Rien  * Très italique * ** SUPER GRAS **"))
# print(formater_paragraphe("+ Pomme"))
# print(formater_paragraphe("+ Poire"))


##################################################
def longueur_un_mot(mot,fonte):

    # Affiche un texte invisible juste pour récupérer sa longueur
    mot_canvas = canvas.create_text(100,100, text=mot,anchor=SW,font=fonte,fill=couleur_fond)

    # En ectraire les extrémités
    xdeb = canvas.bbox(mot_canvas)[0]    
    xfin = canvas.bbox(mot_canvas)[2] 
    return xfin - xdeb


# Test 
#print("longueur du mot 'Coucou' :",longueur_un_mot("Coucou",fonte_texte))


##################################################
def longueurs_mots(liste_format_mots):
    long_mots = []
    for mot,mode,en_gras,en_italique in liste_format_mots:
         fonte = choix_fonte(mode,en_gras,en_italique)
         long_mots += [longueur_un_mot(mot,fonte)]

    return long_mots



# liste_format_mots = formater_paragraphe("Hello WORLD ** Gras **")
# long_mots = longueurs_mots(liste_format_mots)
# print(liste_format_mots)
# print(long_mots)


##################################################
def afficher_paragraphe(par,posy):

    liste_format_mots = formater_paragraphe(par)
    long_mots = longueurs_mots(liste_format_mots)

    coupures = coupures_espaces(long_mots,longueur_ligne)
    long_espaces_ligne = calcul_long_espaces(long_mots,coupures,longueur_ligne)

 
    # Début de la ligne
    if (len(liste_format_mots)>0) and (liste_format_mots[0][1] == "liste"):
        indent = indentation  # Décalage 
    else:
        indent = 10   # Début de la ligne

    coupures = coupures_espaces(long_mots,longueur_ligne-indent)
    long_espaces_ligne = calcul_long_espaces(long_mots,coupures,longueur_ligne-indent)


    posx = indent

    for j in range(len(coupures)-1):
        ligne = long_mots[coupures[j]:coupures[j+1]]


        for i in range(coupures[j],coupures[j+1]):
            mot,mode,en_gras,en_italique = liste_format_mots[i]
            fonte = choix_fonte(mode,en_gras,en_italique)

            # Affiche le mot (visible)
            mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=SW,font=fonte,fill=couleur_texte)

            posx = posx + long_mots[i] + long_espaces_ligne[j]

        posx = indent
        posy = posy + espace_entre_lignes

    return posy

# Tests
# afficher_paragraphe("Titre Hello World AAAAA AAA "*11,100)
# afficher_paragraphe("## Sous_titre Hello !"*5,150)
# afficher_paragraphe("Hello !"*30,200)
# afficher_paragraphe("Hello ! ** GRAS **   * Italique *  ** TRES GRAS ** Rien  * Très italique * ** SUPER GRAS **",300)
# afficher_paragraphe("+ Pomme etc "*20,350)
# afficher_paragraphe("+ Poire ou peche "*10,400)
# root.mainloop()

##################################################




  


##################################################
def afficher_fichier(nom):

    # Ouvrir le fichier
    fichier = open(nom,"r") 
    liste_paragraphes = fichier.readlines()
    fichier.close()

    posy = 50

    # Traiter chaque paragraphe
    for par in liste_paragraphes:
        newposy = afficher_paragraphe(par,posy)
        posy = newposy #+ espace_entre_lignes
    
    root.mainloop()

    return


# Tests
afficher_fichier("markdown1.md")

##################################################
##################################################
##################################################
##################################################

