def graphique_cumulatif(liste):
    """Graphique avec rectangles superposés"""
    bas = 500
    for x in liste:
        hauteur = x * echelle
        canvas.create_rectangle(100,bas,200,bas-hauteur,fill=une_couleur())
        bas = bas - hauteur

    # Bonus : Coordonnées verticales à gauche
    max_liste = sum(liste)
    canvas.create_line(90,500,90,500-echelle*max_liste)   
    for j in range(0,max_liste+1,5):
        canvas.create_line(85,500-echelle*j,90,500-echelle*j)
        canvas.create_text(80,500-echelle*j,text=str(j)) 
    
    return

# Test
echelle = 5
liste = [5,8,6,3,7,10,4,12]
graphique_cumulatif(liste)
root.mainloop()