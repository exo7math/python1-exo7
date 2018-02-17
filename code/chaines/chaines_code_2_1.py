def distance_hamming(mot1,mot2):
    """ Calcule la distance de Hamming
    Entrée : deux mots de même longueur
    Sortie : la distance entre ces mots """

    distance = 0
    for i in range(len(mot1)):
        if mot1[i] != mot2[i]:
            distance = distance + 1

    return distance

# Test 
premier_mot = "JAPON"
second_mot = "SAVON"
dist = distance_hamming(premier_mot,second_mot)
print("La distance entre",premier_mot, "et", second_mot, "est", dist)