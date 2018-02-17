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
print("Longueur du mot 'Coucou' :",longueur_mot("Coucou",fonte_titre),"pixels")
encadre_mot("Coucou",fonte_titre)
root.mainloop()