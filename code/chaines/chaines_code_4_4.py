def carac_majuscule(car):
    """ Transforme une lettre minuscule en majuscule
    Entrée : un caractère minuscule parmi "a",...,"z"
    Sortie : le même caractère en majuscule """

    ordre = ord(car)
    nouv_ordre = ordre - 32
    nouv_car = chr(nouv_ordre)

    return nouv_car

# Test 
print("La majuscule de a est",carac_majuscule("a"))