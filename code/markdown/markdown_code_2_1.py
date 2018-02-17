def afficher_ligne_v1(par,posy):
    """ Affiche le texte sur une seul ligne sans mise en forme
    Entrée : un paragraphe (c-à-d une longue ligne), la position verticale
    Sortie : affichage """   

    posx = 20    # Début de la ligne tout à gauche

    liste_mots = par.split()
    for mot in liste_mots:

        mot = mot + " "   # Rajoute espace qui sépare les mots

        mot_canvas = canvas.create_text(posx,posy, text=mot,anchor=NW,font=fonte_titre,fill=couleur_texte)
        canvas.create_rectangle(canvas.bbox(mot_canvas),width=2)

        # On place le nouveau mot après le précédent
        posx = canvas.bbox(mot_canvas)[2]

    return 

# Tests
afficher_ligne_v1("Bonjour, voici mon premier texte !",100)
root.mainloop()