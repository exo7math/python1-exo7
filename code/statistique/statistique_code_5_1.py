from random import *

def cours_bourse(n):
    """ Simulation de n jours de bourse """
    val = 1000
    liste_val = [val]
    for i in range(n-1):
        val = val + randint(-10,12)/3
        liste_val = liste_val + [val]

    return liste_val

# Test
print(cours_bourse(100)) 