def nombre_total(phrase):
    """ Compte le nombre total de lettres
    Entrée : une phrase en majuscule
    Sortie : le nombre total de lettres de "A" à "Z" """

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    nb = 0
    for car in phrase:
        if car in alphabet:
            nb = nb + 1

    return nb

# Test 
phrase = "ESPRIT EST TU LA"
print("La phrase",phrase,"contient",nombre_total(phrase),"lettres")