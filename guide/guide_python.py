
##############################
# Guide - Python fonctions
##############################

def somme_produit(x,y):
    """ Calcule la somme et le produit de deux nombres. """
    S = x + y     # Somme
    P = x*y       # Produit
    return S, P   # Renvoie les résultats

# Appel de la fonction
som, prod = somme_produit(3,7)  # Résultats
print("Somme :",som)            # Affichage
print("Produit :",prod)         # Affichage