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
afficher_fichier("markdown1.md")
# afficher_fichier("markdown2.md")