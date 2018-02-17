def transforme_en_verlan(mot):
    """ Transforme un mot en verlan
    Entrée : un mot (une chaîne de caractères)
    Sortie : le mot transformé verlan """

    verlan = ""
    for carac in mot:
        verlan = carac + verlan

    return verlan

# Test 
mot = "BONJOUR"
verlan = transforme_en_verlan(mot)
print("Le mot",mot,"devient",verlan,"!")