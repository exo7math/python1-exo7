
##############################
# Chaînes de caractères - Analyse statistique d'un texte
##############################


##############################
# Activité 3 - Séquences d'ADN
##############################

## Question 1 ##

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


## Question 2 ##

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

    
## Question 3 ##

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


## Question 4 ##


def enquete():
    moutarde =  "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    rose =      "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    pervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    leblanc =   "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"

    code1 = "CATA"
    code2 = "ATGC"

    for suspect in [moutarde,rose,pervenche,leblanc]:
        print(position(code1,suspect))
        print(position(code2,suspect))

    return


# Execution de l'enquête
enquete()

