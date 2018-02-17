def graphique_pourcentage(liste):
    """Graphique rectangulaire divisé en sous-rectangles""" 
    somme = sum(liste)
    posx = 100
    for x in liste:
        largeur = x/somme*100 * 5
        canvas.create_rectangle(posx,300,posx+largeur,200,fill=une_couleur())
        posx = posx + largeur

    # Bonus : Coordonnées horizontales en dessous
    canvas.create_line(100,325,600,325)   
    for i in range(0,11):
        canvas.create_line(100+i*50,325,100+i*50,330)
        canvas.create_text(100+i*50,340,text=str(i*10)+"%") 
    return    

# Test
echelle = 5
liste = [5,8,6,3,7,10,4,12]
graphique_pourcentage(liste)
root.mainloop()