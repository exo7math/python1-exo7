def position_de_AT(sequence):
    """ Détermine la position de la première séquence AT
    Entrée : une séquence de A,C,T,G (chaîne de caractères)
    Sortie : la position dans cette séquence (commence à 0) """

    for i in range(len(sequence)-1):
        if sequence[i] == 'A' and sequence[i+1] == 'T':
            return i  # Si trouvé

    return None  # Si pas du tout trouvé
            
# Test 
sequence = "GTGGTTTGACCTCCCATGGCCAT"
position = position_de_AT(sequence)
print("Dans la séquence",sequence,"le code AT apparaît en position",position)