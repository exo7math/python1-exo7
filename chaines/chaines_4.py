
##############################
# Chaînes de caractères - Analyse statistique d'un texte
##############################


##############################
# Activité 4 - Majuscules/minuscules
##############################

## Question 1 ##

# A la machine
code = [80,121,116,104,111,110,32,101,115,116,32,115,121,109,112,64]
phrase = ""
for c in code:
    phrase = phrase + chr(c)
print(phrase)


## Question 2 ##

for i in range(33,128):
    print(i," : ",chr(i))


## Question 3 ##

exp1 = 'chr(ord("a")-32)'
exp2 = 'chr(ord("B")+32)'

print(exp1," donne ",eval(exp1))
print(exp2," donne ",eval(exp2))


## Question 4 ##

def lettre_majuscule(car):
    """ Transforme une lettre minuscule en majuscule
    Entrée : un caractère minuscule parmi "a",...,"z"
    Sortie : le même caractère en majuscule """

    ordre = ord(car)
    nouv_ordre = ordre - 32
    nouv_car = chr(nouv_ordre)

    return nouv_car


# Test 
print("La majuscule de a est",lettre_majuscule("a"))



## Question 5 ##

def majuscules(phrase):
    """ Transforme une phrase en majuscules
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
print("La phrase",phrase,"devient",majuscules(phrase))


# On aura aussi besoin de :
def minuscules(phrase):
    """ Transforme une phrase en minuscules
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


## Question 6 ##

def formate_prenom_nom(personne):
    """ Transforme le nom d'une personne au format "Prenom NOM"
    Entrée : le prénom et le nom d'une personne (sans accent, séparé par une espace)
    Sortie : le nom complet au format "Prenom NOM" """
    
    # On sépare le prénom du nom
    prenom = ""
    nom = ""
    dans_le_prenom = True     # On est dans le prénom
    for car in personne:
        if dans_le_prenom:
            prenom = prenom + car
        else:
            nom = nom + car
        if car == " ":
            dans_le_prenom =  False    # Le prénom est fini

    # On formate le prénom
    nouv_prenom = majuscules(prenom[0])+minuscules(prenom[1:len(prenom)])

    # On formate le nom
    nouv_nom = majuscules(nom)
      
    return nouv_prenom+nouv_nom


# Test 
personne = "harry POTTER"
print(personne,"devient",formate_prenom_nom(personne))
personne = "LORD Voldemort"
print(personne,"devient",formate_prenom_nom(personne))


