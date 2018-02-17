# mot = "chat"
mot = "souris"

derniere_lettre = mot[len(mot)-1]

if derniere_lettre == "s":
    pluriel = mot
else:
    pluriel = mot + "s"

print("Mon mot : ",mot)
print("Au pluriel : ",pluriel)