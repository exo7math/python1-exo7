# Boutons

def action_bouton_evolution():
    global tableau
    tableau = evolution(tableau)
    canvas.delete("all")
    afficher_lignes()
    afficher_tableau(tableau)
    return


bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_afficher = Button(root,text="Évoluer", width=20, command=action_bouton_evolution)
bouton_afficher.pack(side=BOTTOM, padx=5, pady=20)

bouton_clignotant = Button(root,text="Clignotant", width=20, command=clignotant)
bouton_clignotant.pack(side=TOP, padx=5, pady=5)

bouton_vaisseau = Button(root,text="Vaisseau", width=20, command=vaisseau)
bouton_vaisseau.pack(side=TOP, padx=5, pady=5)

bouton_pentadecathlon = Button(root,text="Pentadecathlon", width=20, command=pentadecathlon)
bouton_pentadecathlon.pack(side=TOP, padx=5, pady=5)

root.mainloop()