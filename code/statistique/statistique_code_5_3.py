def calcul_moyenne_mobile(liste,duree):
    """ Calcule la moyenne mobile """
    moyenne_mobile = []
    for i in range(len(liste)-duree+1):
        moyenne = sum(liste[i:i+duree])/duree
        moyenne_mobile = moyenne_mobile + [moyenne]

    return moyenne_mobile

# Test
liste = [1,2,3,4,5,6]
print(liste)
print(calcul_moyenne_mobile(liste,2))