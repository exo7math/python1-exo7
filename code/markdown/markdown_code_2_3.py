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
afficher_ligne_v3("Mot ** en gras ** et lui en * italique *",100)
afficher_ligne_v3("+ Pommes et surtout ** poires ** et * ananas *",125)
root.mainloop()