def position(code,sequence):
    """ Détermine la position du code dans la séquence
    Entrée : une séquence de A,C,T,G (chaîne de caractères)
    Sortie : la position dans cette séquence (commence à 0) """

    for i in range(len(sequence)-len(code)):
        if code == sequence[i:i+len(code)]:
            return i  # Si trouvé, c'est fini

    return None  # Si pas du tout trouvé
            
# Test 
sequence = "GAAGACCTTCTCCTCCTGC"
code = "CCTC"
pos = position(code,sequence)
print("Dans la séquence",sequence,"le code",code,"apparaît en position",pos)