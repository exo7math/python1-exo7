def calcul_quartiles(liste):
    """ Calcule les quartiles de la liste
    Entrée : une liste de nombre
    Sortie : leur quartile Q1, Q2=mediane, Q3 """        
    mediane = calcul_mediane(liste)

    liste_triee = sorted(liste)
    n = len(liste_triee)
    indice_milieu = n//2
    if n%2 == 0: # si n pair
        liste_inf = liste[:indice_milieu]
        liste_sup = liste[indice_milieu:]
    else: # n impair
        liste_inf = liste[:indice_milieu+1]
        liste_sup = liste[indice_milieu:]    
    Q1 =  calcul_mediane(liste_inf)
    Q3 =  calcul_mediane(liste_sup)

    return Q1, mediane, Q3

# Test 
print("--- Quartiles ---")
liste = [3,4,5,7,12,50,100]
print(liste)
print(calcul_quartiles(liste))


def quartiles_notes(effectifs_notes):
    """ Calcule les quartiles des notes
    Entrée : une liste d'effectifs de notes
    Sortie : les quartiles """   
    liste = notes_vers_liste(effectifs_notes)
    Q1,Q2,Q3 = calcul_quartiles(liste)

    return Q1, Q2, Q3

# Test 
print("--- Quartiles des notes ---")
effectifs_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
print(effectifs_notes)
print(quartiles_notes(effectifs_notes))