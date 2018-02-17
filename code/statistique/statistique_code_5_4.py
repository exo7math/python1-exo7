def graphique_moyenne_mobile(liste):
    """ Affiche les moyennes mobiles à 7 et 30 jours """
    # moyenne 7 derniers jours
    moyenne_7 = calcul_moyenne_mobile(liste,7) 
    for i in range(len(moyenne_7)):  
        canvas.create_rectangle(100+i+6,300+1000-moyenne_7[i],100+i+6+1,300+1000-moyenne_7[i],outline="blue")

    # moyenne 30 derniers jours
    moyenne_30 = calcul_moyenne_mobile(liste,30)   
    for i in range(len(moyenne_30)):  
        canvas.create_rectangle(100+i+29,300+1000-moyenne_30[i],100+i+29+1,300+1000-moyenne_30[i],outline="sienna")

    return

# Test
liste = cours_bourse(365)
graphique_point(liste)           # Le cours au jour le jour
graphique_moyenne_mobile(liste)  # La moyenne à 7 et 30 jours
root.mainloop()