def presence_de_A(sequence):
    """ Détermine la présence du nucléotides A
    Entrée : une séquence de A,C,T,G (chaîne de caractères)
    Sortie : vrai ou faux """

    for nucleotide in sequence:
        if nucleotide == 'A':
            return True

    return False

# Test 
sequence = "AGACAGCGAGCATATGCAGGAAG"
reponse = presence_de_A(sequence)
print("Est-ce qu'il y a A dans la séquence",sequence," : ",reponse)