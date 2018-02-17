def nombre_lettres(lettre,phrase):
    """ Compte le nombre d'occurrences d'une lettre donnée dans phrase
    Entrée : une lettre et une phrase en majuscule
    Sortie : le nombre de lettres """

    nb = 0
    for car in phrase:
        if car == lettre:
            nb = nb + 1

    return nb

# Test 
phrase = "ESPRIT EST TU LA"
print("La phrase",phrase,"contient",nombre_lettres("S",phrase),"fois la lettre S")