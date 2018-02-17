def graphique_barres(liste):
    """Graphique avec une barre par élément de la liste"""
    posx = 100
    for x in liste:
        hauteur = x * echelle
        canvas.create_rectangle(posx,400,posx+10,400-hauteur,fill="red")
        posx = posx + 30

    # Bonus : Coordonnées verticale à gauche
    max_liste = max(liste)
    canvas.create_line(90,400,90,400-echelle*max_liste)   
    for j in range(max_liste+1):
        canvas.create_line(85,400-echelle*j,90,400-echelle*j)
        canvas.create_text(80,400-echelle*j,text=str(j)) 

    return

# Test
echelle = 20
liste = [5,8,6,3,7,10,4]
graphique_barres(liste)
root.mainloop()