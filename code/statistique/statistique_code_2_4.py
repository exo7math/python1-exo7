def graphique_secteurs(liste):
    """Graphique en camenbert"""
    somme = sum(liste)
    debut_angle = 0
    for x in liste:
        angle = x/somme*360 
        canvas.create_arc(200,100,550,450,start=debut_angle,extent=angle,style=PIESLICE,fill=une_couleur())
        debut_angle = debut_angle + angle
    return

# Test
echelle = 5
liste = [5,8,6,3,7,10,4,12]
graphique_secteurs(liste)
root.mainloop()
