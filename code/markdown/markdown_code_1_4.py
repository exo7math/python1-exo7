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