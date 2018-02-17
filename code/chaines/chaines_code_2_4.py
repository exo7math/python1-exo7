def est_un_palindrome(mot):
    """ Détermine si un mot est un palindrome
    Entrée : un mot (une chaîne de caractères)
    Sortie : vrai si le mot est un palindrome, faux sinon """

    verlan = transforme_en_verlan(mot)
    if mot == verlan:
        return True
    else: 
        return False

# Test 
mot = "KAYAK"
print("Le mot",mot,"est-il un palindrome ? : ",est_un_palindrome(mot))