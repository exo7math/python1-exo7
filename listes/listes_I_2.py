
##############################
# Listes I
##############################

##############################
##############################
# Cours 2

maliste = []
maliste = maliste + ["Un"]
maliste = ["Deux"] + maliste
maliste[1:5]


##############################
# Activité 2 - Manipulation de listes
##############################

## Question 1 ##

##############################
def rotation(liste):
    n = len(liste)
    new_liste = [liste[n-1]] + liste[0:n-1]
    return new_liste

# Test
print("--- Rotation ---")
print(rotation([1,2,3,4]))


## Question 2 ##

##############################
def inverser(liste):
    new_liste = []
    for element in liste:
        new_liste = [element] + new_liste
    return new_liste

# Test
print("--- Inverse ---")
print(inverser([1,2,3,4]))


## Question 3 ##

##############################
def supprimer_rang(liste,rang):
    n = len(liste)
    new_liste = liste[0:rang]+liste[rang+1:n]
    return new_liste

# Test
print("--- Supprimer rang ---")
print(supprimer_rang([8,7,6,5,4],2))

## Question 4 ##

##############################
def supprimer_element(liste,element):
    new_liste = []
    for x in liste:
        if x != element:
            new_liste = new_liste + [x]
    return new_liste

# Test
print("--- Supprimer élément ---")
print(supprimer_element([8,7,4,6,5,4],4))



##############################
##############################
# Cours 3 - Manipulation : conclusion

# reverse, reversed, [::-1]

print("--- Cours ---")
liste = [1,2,3,4]
print(liste[::-1])
liste.reverse()
print(liste)

print(list(reversed(liste)))



# Autre idées utiliser remove()


print("--- remove() ---")
liste = [2,5,3,8,5]
print(liste)
liste.remove(5)
print(liste)
liste.remove(5)
print(liste)


# Voir aussi "del"