def notes_vers_liste(effectifs_notes):
    """ Convertit des effectifs de notes en une liste de notes
    Entrée : une liste d'effectifs de notes
    Sortie : la liste des notes """        
    liste = []
    for i in range(len(effectifs_notes)):
        nb = effectifs_notes[i]
        liste = liste + [i]*nb

    return liste

# Test 
print("--- Liste à partir des effectifs ---")
effectifs_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
# effectifs_notes = [randint(1,5) for i in range(21)]
print(effectifs_notes)
print(notes_vers_liste(effectifs_notes))


def mediane_notes(effectifs_notes):
    """ Calcule la médiane des notes
    Entrée : une liste d'effectifs de notes
    Sortie : la médiane """   
    liste = notes_vers_liste(effectifs_notes)
    mediane = calcul_mediane(liste)

    return mediane

# Test 
print("--- Médiane des notes ---")
effectifs_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
print(effectifs_notes)
print(mediane_notes(effectifs_notes))