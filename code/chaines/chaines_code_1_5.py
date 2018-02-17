def conjugue(verbe):
    """ Conjugue au présent.
    Entrée : un verbe du premier groupe
    Sortie : affiche la conjugaison au présent """

    debut_verbe = verbe[0:len(verbe)-2]
    fin_verbe = verbe[len(verbe)-2:len(verbe)]

    if fin_verbe == "er":
        print("Je " + debut_verbe + "e\n")
        print("Tu " + debut_verbe + "es\n")  
        print("Il/elle " + debut_verbe + "e\n")
        print("Nous " + debut_verbe + "ons\n")
        print("Vous " + debut_verbe + "ez\n")
        print("Ils/elles " + debut_verbe + "ent\n")
    else:
        print("Ce n'est pas un verbe du premier groupe !")

    return

# Test 
verbe = input("Donne-moi un verbe du premier groupe : ")
conjugue(verbe)