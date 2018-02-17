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
afficher_ligne_v2("# Voici un titre",80)
afficher_ligne_v2("## Et ici un sous titre",115)
afficher_ligne_v2("Du texte normal, et une liste ci-dessous :",150)
afficher_ligne_v2("+ Pomme",175)
afficher_ligne_v2("+ Poire",200)
afficher_ligne_v2("+ Scoubidou",225)
root.mainloop()