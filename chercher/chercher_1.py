
##############################
# Chercher et remplacer
##############################


##############################
# Activité 1 - Chercher
##############################

## Question 1 ##


def chercher_in(chaine,sous_chaine):
    return sous_chaine in chaine

# Test    
print("--- Avec 'in' ---")

chaine = "ETRE OU NE PAS ETRE"
sous_chaine = "PAS"
print(chercher_in(chaine,sous_chaine))


## Question 2 ##

def chercher_find(chaine,sous_chaine):
    position = chaine.find(sous_chaine)    
    return position

# Test 
print("--- Avec find() ---")

position = chercher_find(chaine,sous_chaine)
print(position)

position = chercher_find(chaine,"XYZ")
print(position)

## Question 3 ##

def chercher_index(chaine,sous_chaine):
    position = chaine.index(sous_chaine)    
    return position

# Test 
print("--- Avec index() ---")

position = chercher_index(chaine,sous_chaine)
print(position)

# position = chercher_index(chaine,"XYZ")
# print(position)


## Question 4 ##


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

# Test

print("--- A la main ---")

position = chercher(chaine,sous_chaine)
print(position)

position = chercher(chaine,"XYZ")
print(position)

