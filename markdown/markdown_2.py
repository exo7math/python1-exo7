
##############################
# Visualiseur de texte - Markdown
##############################


##############################
# Activité 2 - Afficher du markdown
##############################


from tkinter import *
from tkinter.font import Font


##############################
# A garder de l'activité 1
##############################

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
fonte_gras =  Font(family="Times", weight="bold", size=12)
fonte_titre = Font(family="Times", weight="bold", size=20)
fonte_sous_titre = Font(family="Times", weight="bold", size=16)


##################################################
def choix_fonte(mode,en_gras,en_italique):
    """
    Renvoie une fonte selon les paramètres
    Entrée : un mode (texte ou  liste,titre,sous-titre), gras ou pas, italique ou pas
    Sortie : la fonte
    """    

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



##################################################
## Question 1 ##

def afficher_ligne_v1(par,posy):
    """ Affiche le texte sur une seul ligne sans mise en forme
    Entrée : un paragraphe (c-à-d une longue ligne), la position verticale
    Sortie : affichage """   

    posx = 20  # Début de la ligne tout à gauche

    liste_mots = par.split()
    for mot in liste_mots:

        mot = mot + " " # Rajoute espace qui sépare les mots

        mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=NW,font=fonte_titre,fill=couleur_texte)
        canvas.create_rectangle(canvas.bbox(mot_canvas),width=2)

        # On place le nouveau mot après le précédent
        posx = canvas.bbox(mot_canvas)[2]

    return 

# Tests
# afficher_ligne_v1("Bonjour, voici mon premier texte !",100)
# root.mainloop()


##################################################
## Question 2 ##

def afficher_ligne_v2(par,posy):
    """ Affiche le texte selon le mode titre, sous-titre, texte, liste
    Entrée : un paragraphe (c-à-d une longue ligne), la position verticale
    Sortie : affichage """ 

    # Par défaut : texte, sans indentation
    mode = "texte"
    indentation = 20

    if par[0:2] == "##":       # Sous_titre
        mode = "sous_titre"
        par = par[2:]          # Supprime les ##
    elif par[0] == "#":        # Titre 
        mode = "titre"
        par = par[1:]          # Supprime le #       
    elif par[0] == "+":        # liste
        mode = "liste"
        par = u'\u2022' + par[1:]          # Remplace le "+" par un rond
        indentation = 40

    
    # Début de la ligne (décalé si liste)
    posx = indentation

    liste_mots = par.split()
    for mot in liste_mots:

        fonte = choix_fonte(mode,False,False)

        mot = mot + " " # Rajoute espace qui sépare les mots
        mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=NW,font=fonte,fill=couleur_texte)
        posx = canvas.bbox(mot_canvas)[2]

    return


# Tests
# afficher_ligne_v2("# Voici un titre",80)
# afficher_ligne_v2("## Et ici un sous titre",115)
# afficher_ligne_v2("Du texte normal, et une liste ci-dessous :",150)
# afficher_ligne_v2("+ Pomme",175)
# afficher_ligne_v2("+ Poire",200)
# afficher_ligne_v2("+ Scoubidou",225)
# root.mainloop()


##################################################
## Question 3 ##

def afficher_ligne_v3(par,posy):
    """ Affiche le texte selon gras et italique et selon le mode
    Entrée : un paragraphe (c-à-d une longue ligne), la position verticale
    Sortie : affichage """ 

    # Par défaut : texte, sans indentation
    mode = "texte"
    indentation = 20

    if par[0:2] == "##":       # Sous_titre
        mode = "sous_titre"
        par = par[2:]          # Supprime les ##
    elif par[0] == "#":        # Titre 
        mode = "titre"    
        par = par[1:]          # Supprime le #       
    elif par[0] == "+":        # liste
        mode = "liste"
        par = u'\u2022' + par[1:]          # Remplace le "+" par un rond
        indentation = 40

    # Gras / pas gras (par défaut ni gras, ni italique)
    en_gras = False
    en_italique = False
   
    # Début de la ligne (décalé si liste)
    posx = indentation

    liste_mots = par.split()
    for mot in liste_mots:

        if mot == "**":  # Bascule gras / pas gras
            en_gras = not(en_gras) 
            mot = ""           

        if en_gras:
            fonte = fonte_gras

        if mot == "*":       # Bascule italique / pas italique
            en_italique = not(en_italique)          
            mot = ""         

        fonte = choix_fonte(mode,en_gras,en_italique) 

        if mot != "":
            mot = mot + " " # Rajoute espace qui sépare les mots

        mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=NW,font=fonte,fill=couleur_texte)
        posx = canvas.bbox(mot_canvas)[2]

    return


# Tests
# afficher_ligne_v3("Mot ** en gras ** et lui en * italique *",100)
# afficher_ligne_v3("+ Pommes et surtout ** poires ** et * ananas *",125)
# root.mainloop()



##################################################
## Question 4 ##


# Interligne
espace_entre_lignes = 18


def afficher_paragraphe(par,posy):
    """ Affiche le texte selon gras et italique et selon le mode
    Entrée : un paragraphe (c-à-d une longue ligne), la position verticale
    Sortie : affichage """ 

    # Par défaut : texte, sans indentation
    mode = "texte"
    indentation = 20

    if par[0:2] == "##":       # Sous_titre
        mode = "sous_titre"
        par = par[2:]          # Supprime les ##
    elif par[0] == "#":        # Titre 
        mode = "titre"    
        par = par[1:]          # Supprime le #       
    elif par[0] == "+":        # liste
        mode = "liste"
        par = u'\u2022' + par[1:]          # Remplace le "+" par un rond
        indentation = 40

    # Gras / pas gras (par défaut ni gras, ni italique)
    en_gras = False
    en_italique = False
   
    # Début de la ligne (décalé si liste)
    posx = indentation

    liste_mots = par.split()
    for mot in liste_mots:

        if mot == "**":    # Bascule gras / pas gras
            en_gras = not(en_gras) 
            mot = ""           

        if en_gras:
            fonte = fonte_gras

        if mot == "*":    # Bascule italique / pas italique
            en_italique = not(en_italique)          
            mot = ""         

        fonte = choix_fonte(mode,en_gras,en_italique) 

        if mot != "":
            mot = mot + " "    # Rajoute espace qui sépare les mots

        mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=NW,font=fonte,fill=couleur_texte)
        posx = canvas.bbox(mot_canvas)[2]

        if posx > largeur:
            posx = indentation
            posy = posy + espace_entre_lignes

    return posy

# Tests
# afficher_paragraphe("# Titre Hello ! World",100)
# afficher_paragraphe("## Sous_titre Hello "*5,150)
# afficher_paragraphe("Hello Bonjour "*30,200)
# afficher_paragraphe("Hello ! ** GRAS **   * Italique *  ** TRES GRAS ** Rien  * Très italique * ** SUPER GRAS **",300)
# afficher_paragraphe("+ Pomme",350)
# afficher_paragraphe("+ Poire",370)
# afficher_paragraphe("Des mots, toujours de mots, encore des mots. "*10,10)
# root.mainloop()




##################################################
## Question 5 ##

def afficher_fichier(nom):
    """ Affiche les paragraphes d'un fichier
    Entrée : un nom de fichier au format markdown
    Sortie : affichage des paragraphes """ 

    # Ouvrir le fichier
    fichier = open(nom,"r") 
    liste_paragraphes = fichier.readlines()
    fichier.close()

    posy = 50

    # Traiter chaque paragraphe
    for par in liste_paragraphes:
        newposy = afficher_paragraphe(par,posy)
        posy = newposy + espace_entre_lignes
    
    root.mainloop()

    return


# Tests
# afficher_fichier("markdown1.md")
# afficher_fichier("markdown2.md")