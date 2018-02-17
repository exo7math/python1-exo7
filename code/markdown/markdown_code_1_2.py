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
encadre_mot("Du texte avec Python",fonte_titre)
root.mainloop()