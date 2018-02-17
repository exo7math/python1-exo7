
##############################
# Chercher et remplacer
##############################

##############################
##############################
# Rappel de l'activité 1

def chercher(chaine,sous_chaine):
    long_chaine = len(chaine)
    long_sous_chaine = len(sous_chaine)
    for i in range(long_chaine-long_sous_chaine+1):
        trouve = True
        for j in range(long_sous_chaine):
            if chaine[i+j] != sous_chaine[j]:
                trouve = False
                break
        if trouve == True:
            return i
    return None



##############################
# Activité 2 - Remplacer 
##############################


chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "PAS"
nouv_sous_chaine = "PLUS"


## Question 1 ##

print("--- Avec replace() ---")
nouv_chaine = chaine.replace(sous_chaine,nouv_sous_chaine)
print(nouv_chaine)


## Question 2 ##

#
# remplacer_une_fois() A la main en utilisant chercher()
def remplacer(chaine,sous_chaine,nouv_sous_chaine):
    pos = chercher(chaine,sous_chaine)

    if pos is not None:  # Si trouvé
        finpos = pos+len(sous_chaine)
        chaine = chaine[:pos]+nouv_sous_chaine+chaine[finpos:]

    return chaine

print("--- Remplacer : à la main ---")
nouv_chaine = remplacer(chaine,sous_chaine,nouv_sous_chaine)
print(nouv_chaine)


## Question 3 ##

#
# remplacer() remplace toutes les occurences


def remplacer_tout(chaine,sous_chaine,nouv_sous_chaine):

    pos = chercher(chaine,sous_chaine)
        
    while pos is not None:  # Tant que trouvé
        finpos = pos+len(sous_chaine)
        chaine = chaine[:pos]+nouv_sous_chaine+chaine[finpos:]
        pos = chercher(chaine,sous_chaine)

    return chaine

# Attention fonction un peu trop basique car A -> AB devrait boucler indféiniment.

print("--- Remplacer tout : à la main ---")
chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "ETRE"
nouv_sous_chaine = "AVOIR" 
nouv_chaine = remplacer_tout(chaine,sous_chaine,nouv_sous_chaine)
print(nouv_chaine)


