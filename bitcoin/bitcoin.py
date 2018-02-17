
##############################
# Bitcoin
##############################



from random import randint
from time import *



##############################
# Activité 2 - Outils pour les listes
##############################

# Constante globale de longueur des blocs
N = 6

# Constante pour preuve de travail
Max = [0,0,25]


##############################

## Question 1 ##

# Addition des termes de deux listes de même longueur
def addition(liste1,liste2):
    liste_somme = []
    for i in range(len(liste1)):
        liste_somme = liste_somme + [ (liste1[i]+liste2[i]) % 100 ]

    return liste_somme
    
# Test
print("--- Test somme liste ---")   
print(addition([1,2,3,4,5,6],[1,1,1,1,1,1]))


##############################

## Question 2 ##

# Test si une liste est plus petite que liste_max
def est_plus_petit(liste,liste_max):
    i = 0
    n = len(liste_max)
    while (i < n) and (liste[i] <= liste_max[i]):
        i = i + 1
    if i == n:
        return True
    else:
        return False
    
# Test
print("--- Test plus petit liste ---")   
print(est_plus_petit([0,0,24,4,5,6],[0,0,50]))


##############################

## Question 3 ##

def phrase_vers_liste(phrase):
    # Transforme lettres en nombre modulo 100
    liste = [ord(c) % 100 for c in phrase]

    # Rajoute des 0 devant si besoin
    while len(liste) % N > 0:
        liste = [0] + liste

    return liste

# Test
print("--- Phrase vers liste ---")
phrase = "Vive moi !" 
print(phrase)
print(phrase_vers_liste(phrase))  



##############################
# Activité 3 - Fonction de hachage
##############################



##############################

## Question 3 ##
p = [7,11,13,17,19,23] # nb premiers

def un_tour(bloc):
    # Addition
    bloc[1] = (bloc[1]+bloc[0]) % 100
    bloc[3] = (bloc[3]+bloc[2]) % 100
    bloc[5] = (bloc[5]+bloc[4]) % 100

    # m = p*m + 1 (modulo 100)
    for i in range(N):
        bloc[i] = (p[i]*bloc[i]+1) %  100
    # permutation
    bloc = [bloc[N-1]] + bloc[:N-1]
    return bloc

# Test
print("--- Test un tour ---")
bloc = [0,1,2,3,4,5]
print(bloc)
print(un_tour(bloc))

bloc = [1,1,2,3,4,5]
print(bloc)
print(un_tour(bloc))


##############################

## Question 3 ##

def dix_tours(bloc):
    for i in range(10):
        bloc = un_tour(bloc)
    return bloc

# Test
print("--- Test dix tours ---")
bloc = [0,1,2,3,4,5]
print(bloc)
print(dix_tours(bloc))

bloc = [1,1,2,3,4,5]
print(bloc)
print(dix_tours(bloc))

bloc = [99,96,87,56,67,76]
print(bloc)
print(dix_tours(bloc))

bloc = [70,92,22,4,16,90]
print(bloc)
print(dix_tours(bloc))


##############################

## Question 3 ##
def hachage(liste):

    while len(liste)>N:
        bloc1 = liste[0:N]  # Premier bloc
        bloc2 = liste[N:2*N] # Second bloc
        fin_liste = liste[2*N:] # Le reste
        # print(bloc1)
        # print(bloc2)
        # print(fin_liste)

        #bloc1 = un_tour(bloc1)   # Un tour
        bloc1 = dix_tours(bloc1) # Dix tours

        #print(bloc1)

        nouv_bloc_deb = addition(bloc1,bloc2)

        liste = nouv_bloc_deb + fin_liste

    # Tours de fin pour la liste (qui ne contient plus que N nb)
    # liste = un_tour(liste) # Un tour
    liste = dix_tours(liste) # Un tour

    return liste

# Test
print("--- Hachage d'une liste ---")

liste = [1,2,3,4,5,6,1,2,3,4,5,6]
hach = hachage(liste)
print(liste)
print(hach)

liste = [1,1,3,4,5,6,1,2,3,4,5,6]
hach = hachage(liste)
print(liste)
print(hach)


liste = [0,1,2,3,4,5,1,1,1,1,1,1,10,10,10,10,10,10]
hach = hachage(liste)
print(liste)
print(hach)



##############################


##############################
# Activité 4 - Preuve de travail - Minage
##############################

##############################

## Question 3 ##

def verification_preuve_de_travail(liste,preuve):

    liste_test = liste + preuve
    hach = hachage(liste_test)
    # print(preuve,hach)
    if est_plus_petit(hach,Max):
        return True
    else:
        return False

# Test
print("--- Verif Preuve de travail ---")    

liste = [0,1,2,3,4,5]
preuve = [12, 3, 24, 72, 47, 77]
# Max = [0,0,7]

start_time = time()
print(verification_preuve_de_travail(liste,preuve))
end_time = time()
duree = end_time-start_time

print("Temps de calcul :",duree)

##############################

## Question 2 ##

def preuve_de_travail(liste):

    hach = [1,1,1,1,1,1]

    while not(est_plus_petit(hach,Max)): 
        preuve = [randint(0,99) for i in range(N)]
        liste_test = liste + preuve
        hach = hachage(liste_test)
    print(preuve,hach)

    return preuve

##############################

## Question 2 bis ##

from itertools import product

def preuve_de_travail_bis(liste):
    for preuve in product(range(100),range(100),range(100),range(100),range(100),range(100)):
        preuve = list(preuve)
        liste_test = liste + preuve
        hach = hachage(liste_test)
        if est_plus_petit(hach,Max):
            break

    print(preuve,hach)
    return preuve
    
##############################

## Question 3 ##

# Test
print("--- Preuve de travail ---")    

start_time = time()
liste = [0,1,2,3,4,5]
# preuve = preuve_de_travail(liste)
# preuve = preuve_de_travail_bis(liste)
end_time = time()
duree = end_time-start_time

print("Temps de calcul :",duree)


##############################
# Activité 5 - Tes bitcoins
##############################

##############################

## Question 1 ##

preuve_init = [0,0,0,0,0,0]   # valeur au pif
Livre = [preuve_init]

def ajout_transaction(transaction):
    global Livre
    Livre = Livre + [transaction]
    return Livre

# Test
print("--- Création du livre et ajout d'une transaction ---")
print(Livre)
ajout_transaction("Bob +135")
print(Livre)


##############################

## Question 2 ##

def minage():
    global Livre
    transaction = Livre[-1]
    prec_preuve = Livre[-2]
    # print(transaction)
    # print(prec_hach)
    # print(phrase_vers_liste(transaction))
    liste = prec_preuve + phrase_vers_liste(transaction)

    preuve = preuve_de_travail(liste)

    Livre = Livre + [preuve]

    return Livre

# Test
print("--- Minage  ---")
print(Livre)
minage()
print(Livre)

# Exemple pour fiche
print("--- Exemple pour fiche  ---")
Max = [0,0,7]
hach_init = [3,1,4,1,5,9]   # valeur au pif
Livre = [hach_init]
ajout_transaction("Abel +35")
print(Livre)
minage()
print(Livre)

##############################

## Question 3 ##

def verification_livre():
    prec_preuve = Livre[-3]        
    transaction = Livre[-2]
    preuve = Livre[-1]
    hach = hachage(prec_preuve+phrase_vers_liste(transaction)+preuve)
    if est_plus_petit(hach,Max):
        return True
    else:
        return False


# Test
print("--- Vérification du livre  ---")
print(Livre)
print(verification_livre())



##############################

## Question 4 ##
# Exemple complet

# Constante pour preuve de travail
Max = [0,0,7]


start_time = time()  # début chrono

hach_init = [0,0,0,0,0,0]   # valeur au pif
Livre = [hach_init]

# print(Livre)
# ajout_transaction("Abel +135")
# print(Livre)
# minage()
# print(Livre)
# print(verification_livre())

# ajout_transaction("Bob -77")
# print(Livre)
# minage()
# print(Livre)
# print(verification_livre())

# ajout_transaction("Camille -25")
# print(Livre)
# minage()
# print(Livre)
# print(verification_livre())

end_time = time()
duree = end_time-start_time
print("Temps de calcul :",duree)