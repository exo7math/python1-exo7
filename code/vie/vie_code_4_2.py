def allumer_eteindre(i,j):
    """ Commute une cellule """
    global tableau
    if tableau[i][j] == 0:
        tableau[i][j] = 1
    else: 
        tableau[i][j] = 0
    return


def xy_vers_ij(x,y):
    """ Coordonnées (x,y) vers coordonnées (i,j) """
    i = y // echelle
    j = x // echelle
    return i, j


def action_clic_souris(event):
    canvas.focus_set()
    # print("Clic à", event.x, event.y)
    x = event.x
    y = event.y
    allumer_eteindre(*xy_vers_ij(x,y))
    canvas.delete("all")   
    afficher_lignes()    
    afficher_tableau(tableau)
    return

# Liaison clic de souris/action
canvas.bind("<Button-1>",action_clic_souris)

afficher_lignes()
afficher_tableau(tableau)
root.mainloop()