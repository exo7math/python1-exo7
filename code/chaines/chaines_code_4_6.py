def formate_prenom_nom(personne):
    """ Transforme le nom d'une personne au format "Prenom NOM"
    Entrée : le prénom et le nom d'une personne (sans accent, séparé par une espace)
    Sortie : le nom complet au format "Prenom NOM" """
    
    # On sépare le prénom du nom
    prenom = ""
    nom = ""
    dans_le_prenom = True     # On est dans le prénom
    for car in personne:
        if dans_le_prenom:
            prenom = prenom + car
        else:
            nom = nom + car
        if car == " ":
            dans_le_prenom =  False    # Le prénom est fini

    # On formate le prénom
    nouv_prenom = majuscule(prenom[0])+minuscule(prenom[1:len(prenom)])

    # On formate le nom
    nouv_nom = majuscule(nom)
      
    return nouv_prenom+nouv_nom

# Test 
personne = "harry POTTER"
print(personne,"devient",formate_prenom_nom(personne))
personne = "LORD Voldemort"
print(personne,"devient",formate_prenom_nom(personne))