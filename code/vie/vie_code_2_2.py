def afficher_tableau(tab):
    """ Affiche un tableau à l'écran
    Entrée : un tableau à deux dimension
    Sortie : rien (affichage à l'écran) """    

    for i in range(n):
        for j in range(p):
            if tab[i][j] != 0:
                canvas.create_rectangle(j*echelle,i*echelle,(j+1)*echelle,(i+1)*echelle,fill="red")
        
    return


# Boutons
def action_bouton_afficher():
    canvas.delete("all")
    afficher_lignes()
    afficher_tableau(tableau)
    return


bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_afficher = Button(root,text="Afficher", width=30, command=action_bouton_afficher)
bouton_afficher.pack(side=BOTTOM, padx=5, pady=20)

# Test
afficher_lignes()
# afficher_tableau(tableau)
root.mainloop()