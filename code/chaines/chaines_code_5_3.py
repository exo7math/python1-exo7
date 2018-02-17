def pourcentage_lettre(lettre,phrase):
    """ Calcule le ratio d'une lettre donnée dans phrase
    Entrée : une lettre et une phrase en majuscule
    Sortie : le pourcentage d'apparition de la lettre """

    nb_lettres = nombre_lettres(lettre,phrase)
    nb_total = nombre_total(phrase)
    pourcentage = nb_lettres/nb_total*100
    
    return pourcentage

# Test 
phrase = "ESPRIT EST TU LA"
pourcentage = pourcentage_lettre("S",phrase)
print("La phrase",phrase,"contient",pourcentage,"% de lettre S")
print("Pourcentage arrondi :","{0:.2f}".format(pourcentage))