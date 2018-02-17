def transforme_en_latin_cochon(mot):
    """ Transforme un mot en latin-cochon
    Entrée : un mot (une chaîne de caractères) 
    Sortie : le mot transformé en latin cochon s'il commence par une consonne. """

    premiere_lettre = mot[0]
    reste_mot = mot[1:len(mot)]

    if premiere_lettre not in ["A", "E", "I", "O", "U", "Y"]:
        latin_cochon = reste_mot + premiere_lettre + "UM"
    else:
        latin_cochon = mot

    return latin_cochon

# Test 
mot = "SALOPETTE"
latin = transforme_en_latin_cochon(mot)
print("Le mot",mot,"devient",latin,"!")