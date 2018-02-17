
##############################
# Graphes et combinatoire de Ramsey
##############################


##############################
# Activité 3 - Binaire
##############################

## Echanger n <-> p pour être cohérent avec fiche binaire

def decimal_vers_binaire(p,n):
    chaine_b = bin(p)  # Conversion en une chaîne écriture binaire
    chaine_bb = chaine_b[2:]  # On enlève le préfixe
    # On transforme la chaine en une liste **d'entiers** 0 ou 1
    liste_binaire = []
    for b in chaine_bb:
        liste_binaire = liste_binaire + [int(b)]

    # On rajoute des zéros au début si besoin
    nb_zeros = n - len(liste_binaire)
    for i in range(nb_zeros):
        liste_binaire = [0] + liste_binaire

    return liste_binaire


# Version plus courte qui utilise "format()"
def decimal_vers_binaire_bis(p,n):
    modele = '{:0'+str(n)+'b}'
    chaine_binaire = modele.format(p)
    liste_binaire = [int(b) for b in list(chaine_binaire)]
    return liste_binaire


# Test 
if __name__ == '__main__':
    n = 8
    p = 37
    print(decimal_vers_binaire(p,n))
    print(decimal_vers_binaire_bis(p,n))








