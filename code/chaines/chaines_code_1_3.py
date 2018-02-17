# mot = "chat"
# mot = "souris"
mot = "journal" 

derniere_lettre = mot[len(mot)-1]
avant_derniere_lettre = mot[len(mot)-2]

if derniere_lettre == "s":
    pluriel = mot
elif avant_derniere_lettre == "a" and derniere_lettre == "l":
    debut_mot = mot[0:len(mot)-2]
    pluriel = debut_mot + "aux"
else:
    pluriel = mot + 's'

print("Mon mot : ",mot)
print("Au pluriel : ",pluriel)