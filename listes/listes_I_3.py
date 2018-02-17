
##############################
# Listes I
##############################



##############################
# Activité 3 - Tri à bulle
##############################

def trier(liste):

    newliste = list(liste)  
    
    n = len(newliste)

    for i in range(n-1,-1,-1):
        for j in range(i):
            if newliste[j+1] < newliste[j]:
                el = newliste[j]
                newliste[j] = newliste[j+1]
                newliste[j+1] = el

    return newliste

# Test
print("--- Tri à bulles ---")
print(trier([13,11,7,4,6,8,12,6]))

liste = [13,11,7,4,6,8,12,6]
newliste = trier(liste)
print(liste)
print(newliste)


print(sorted([13,11,7,4,6,8,12,6]))

liste = [13,11,7,4,6,8,12,6]
liste.sort()
print(liste)
