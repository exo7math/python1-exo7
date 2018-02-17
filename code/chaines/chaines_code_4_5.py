def majuscule(phrase):
    """ Transforme une phrase en majuscule
    Entrée : une phrase (une chaîne de caractères)
    Sortie : la même phrase avec les lettres en majuscules """
    
    nouv_phrase = ""
    for car in phrase:
        ordre = ord(car)
        if ordre >= 97 and ordre <= 122:
             # transformation en majuscule
            nouv_phrase = nouv_phrase + chr(ordre-32) 
        else: 
            # conserver le caractère
            nouv_phrase = nouv_phrase + car  

    return nouv_phrase

# Test 
phrase = "Bonjour le monde !"
print("La phrase",phrase,"devient",majuscule(phrase))


# On aura aussi besoin de :
def minuscule(phrase):
    """ Transforme une phrase en minuscule
    Entrée : une phrase (une chaîne de caractères)
    Sortie : la même phrase avec les lettres en minuscules """
    
    nouv_phrase = ""
    for car in phrase:
        ordre = ord(car)
        if ordre >= 65 and ordre <= 90:
             # transformation en minuscules
            nouv_phrase = nouv_phrase + chr(ordre+32) 
        else: 
            # conserver le caractère
            nouv_phrase = nouv_phrase + car  

    return nouv_phrase