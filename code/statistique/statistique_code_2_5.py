longueurs = [randint(5,15) for i in range(103)] 

liste = [15,8,6,13,17,10,14,12]

def action_bouton1():
    global echelle
    echelle = 15
    canvas.delete("all")
    graphique_barres(liste)
    return

def action_bouton2():
    global echelle
    echelle = 4
    canvas.delete("all")
    graphique_cumulatif(liste)
    return

def action_bouton3():
    canvas.delete("all")
    graphique_pourcentage(liste)
    return

def action_bouton4():
    canvas.delete("all")
    graphique_secteurs(liste)
    return

def nouvelle_liste():
    """Génère une nouvelle liste aléatoire"""
    global liste
    n = randint(3,10)
    liste = [randint(1,20) for i in range(n)] 
    canvas.delete("all")   
    return    

# Titre
root.title("Visualisation de données")

# Boutons
bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_changer = Button(root,text="Changer les données", width=30, command=nouvelle_liste)
bouton_changer.pack(side=BOTTOM, padx=5, pady=20)

bouton1 = Button(root,text="Graphique en barres", width=30, command=action_bouton1)
bouton1.pack(padx=5, pady=20)

bouton2 = Button(root,text="Graphique cumulatif", width=30, command=action_bouton2)
bouton2.pack(padx=5, pady=20)

bouton3 = Button(root,text="Graphique en pourcentage", width=30, command=action_bouton3)
bouton3.pack(padx=5, pady=20)

bouton4 = Button(root,text="Graphique en secteurs", width=30, command=action_bouton4)
bouton4.pack(padx=5, pady=20)

root.mainloop()