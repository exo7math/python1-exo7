
##############################
# Visualiseur de texte - Markdown
##############################


##############################
# Activité 1 - Afficher du texte
##############################

##################################################
## Question 1 ##

from tkinter import *
from tkinter.font import Font

# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Format de la page de texte
largeur = 700
hauteur = 500

# Couleurs
couleur_fond = "lightgray"
couleur_texte = "black"

# Cadre
canvas.create_rectangle(10,10,largeur,hauteur,width=2,fill=couleur_fond)

# Fontes
fonte_texte = Font(family="Times", size=12)
fonte_italique = Font(family="Times", slant="italic", size=12)
fonte_gras = Font(family="Times", weight="bold", size=12)
fonte_titre = Font(family="Times", weight="bold", size=20)
fonte_sous_titre = Font(family="Times", weight="bold", size=16)

# Test
# canvas.create_text(100,100, text="Vive les maths !",anchor=NW,font=fonte_titre,fill=couleur_texte)
# canvas.create_text(200,200, text="Vive Python !",anchor=NW,font=fonte_sous_titre,fill="red")
# root.mainloop()



##################################################
## Question 2 ##

def encadre_mot(mot,fonte):
    """ Encadre un mot
    Entrée : une chaîne et sa fonte
    Sortie : affichage du mot et d'un cadre (bounding box) """    

    # Affiche un texte
    mot_canvas = canvas.create_text(100,100, text=mot,anchor=NW,font=fonte,fill=couleur_texte)

    # Coordonnées du rectangle (x1,y1,x2,y2)
    x1,y1,x2,y2 = canvas.bbox(mot_canvas)
    # print(cadre)

    # Affichage du cadre
    canvas.create_rectangle(x1,y1,x2,y2,width=2)
 
    return

# Test 
# encadre_mot("Du texte avec Python",fonte_titre)
# root.mainloop()



##################################################
## Question 3 ##

def longueur_mot(mot,fonte):
    """ Longueur d'un mot
    Entrée : une chaîne et sa fonte
    Sortie : la longuer de ce mot """    

    # Affiche un texte invisible juste pour récupérer sa longueur
    mot_canvas = canvas.create_text(100,100, text=mot,anchor=NW,font=fonte,fill=couleur_fond)

    # En extraire les extrémités
    x1,y1,x2,y2 = canvas.bbox(mot_canvas)

    return x2 - x1


# Test 
# print("Longueur du mot 'Coucou' :",longueur_mot("Coucou",fonte_titre),"pixels")
# encadre_mot("Coucou",fonte_titre)
# root.mainloop()



##################################################
## Question 4 ##

def choix_fonte(mode,en_gras,en_italique):
    """ Renvoie une fonte selon les paramètres
    Entrée : un mode (texte ou liste, titre, sous-titre), gras ou pas, italique ou pas
    Sortie : la fonte """    

    if mode == "titre":
        fonte = fonte_titre
    elif mode == "sous_titre":
        fonte = fonte_sous_titre
    else:       # Mode texte ou liste
        if en_gras:
            fonte = fonte_gras
        elif en_italique:
            fonte = fonte_italique
        else:
            fonte = fonte_texte

    return fonte


# Test 
fonte = choix_fonte("texte",False,True)
canvas.create_text(100,100, text="Ceci est en italique",anchor=NW,font=fonte,fill=couleur_texte)
root.mainloop()

##################################################
