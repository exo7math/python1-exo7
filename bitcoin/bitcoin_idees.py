
from random import randint
from time import *


# Constante global de longueur des mots
N = 6 

# Constante pour preuve de travail
Max = [0,0,5]



##############################
p = [7,11,13,17,19,23] # nb premiers

def un_tour(mot):
    # Addition
    mot[1] = (mot[1]+mot[0]) % 100
    mot[3] = (mot[3]+mot[2]) % 100
    mot[5] = (mot[5]+mot[4]) % 100

    # m = p*m + 1 (modulo 100)
    for i in range(N):
        mot[i] = (p[i]*mot[i]+1) %  100
    # permutation
    mot = [mot[N-1]] + mot[:N-1]
    return mot

# Test
print("--- Test un tour ---")
mot = [0,1,2,3,4,5]
print(mot)
print(un_tour(mot))
mot = [0,1,3,3,4,5]
print(mot)
print(un_tour(mot))


##############################

def dix_tours(mot):
    for i in range(10):
        mot = un_tour(mot)
    return mot

# Test
print("--- Test dix tours ---")
mot = [0,1,2,3,4,5]
print(mot)
print(dix_tours(mot))
mot = [0,1,3,3,4,5]
print(mot)
print(dix_tours(mot))

##############################

# Addition des termes de deux listes de même longueur
def addition(liste1,liste2):
    liste_somme = []
    for i in range(len(liste1)):
        liste_somme = liste_somme + [ liste1[i]+liste2[i] ]

    return liste_somme
    
# Test
print("--- Test somme liste ---")   
print(addition([1,2,3,4,5,6],[1,1,1,1,1,1]))

# Test si une liste est plus petite que liste_max
def plus_petit(liste,liste_max):
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
print(plus_petit([0,0,24,4,5,6],[0,0,50]))

##############################

def phrase_vers_listes(phrase):
    # Transforme lettres en nombre modulo 100
    liste = [ord(c) % 100 for c in phrase]

    # Rajoute des 0 devant si besoin
    while len(liste) % N > 0:
        liste = [0] + liste

    return liste

# Test
print("--- Phrase vers liste ---")
phrase = "Bonjour le Monde!" 
print(phrase)
print(phrase_vers_listes(phrase))  


##############################
def hachage(liste):

    while len(liste)>N:
        mot1 = liste[0:N]  # Premier mot
        mot2 = liste[N:2*N] # Second mot
        fin_liste = liste[2*N:] # Le reste
        # print(mot1)
        # print(mot2)
        # print(fin_liste)

        #mot1 = un_tour(mot1)   # Un tour
        mot1 = dix_tours(mot1) # Dix tours

        #print(mot1)

        nouv_mot_deb = addition(mot1,mot2)

        liste = nouv_mot_deb + fin_liste

    # Tours de fin pour la liste (qui ne contient plus que N nb)
    # liste = un_tour(liste) # Un tour
    liste = dix_tours(liste) # Un tour

    return liste

# Test
print("--- Hachage d'une liste ---")
liste = [0,0,0,0,0,0,0,0,0,0,0,0]
hach = hachage(liste)
print(liste)
print(hach)


##############################


# from itertools import product

# def preuve_de_travail(liste):
#     for preuve in product(range(100),range(100),range(100)):
#         preuve = list(preuve) + [0,0,0]
#         liste_test = liste + preuve
#         hach = hachage(liste_test)
#         if hach[0] == 0 and hach[1] == 0 and hach[2] == 0: # and hach[3] < 50:
#             print(preuve,hach)
#             break
#     return preuve



def preuve_de_travail(liste):

    hach = [1,1,1,1,1,1]

    while not(plus_petit(hach,Max)): 
        preuve = [randint(0,99) for i in range(N)]
        liste_test = liste + preuve
        hach = hachage(liste_test)
    # print(preuve,hach)

    return preuve


# Test
print("--- Preuve de travail ---")    

start_time = time()
liste = [1,2,3,4,5,6]
# preuve = preuve_de_travail(liste)
end_time = time()
duree = end_time-start_time

print("Temps de calcul :",duree)


##############################
def verification_preuve_de_travail(preuve,liste):

    liste_test = liste + preuve
    hach = hachage(liste_test)
    # print(preuve,hach)
    if plus_petit(hach,Max):
        return True
    else:
        return False

# Test
print("--- Verif Preuve de travail ---")    

start_time = time()
#print(verification_preuve_de_travail(preuve,liste))
end_time = time()
duree = end_time-start_time

print("Temps de calcul :",duree)

##############################

def verification_livre():
    prec_preuve = Livre[-3]        
    transaction = Livre[-2]
    preuve = Livre[-1]
    hach = hachage(prec_preuve+phrase_vers_listes(transaction)+preuve)
    if plus_petit(hach,Max):
        return True
    else:
        return False


##############################



preuve_init = [0,0,0,0,0,0]   # valeur au pif
Livre = [preuve_init]
#Livre = Livre + ["Bob +135"]



def ajout_transaction(transaction):
    global Livre
    Livre = Livre + [transaction]
    return Livre

# Test
print(Livre)
ajout_transaction("Bob +135")
print(Livre)


##############################
def minage():
    global Livre
    transaction = Livre[-1]
    prec_preuve = Livre[-2]
    # print(transaction)
    # print(prec_hach)
    # print(phrase_vers_listes(transaction))
    bloc = prec_preuve + phrase_vers_listes(transaction)

    preuve = preuve_de_travail(bloc)

    Livre = Livre + [preuve]

    # Vérification minage
    # print(verification_preuve_de_travail(preuve,bloc))

    return Livre

# Test
# minage()
# print(Livre)



# Vrai exemple

start_time = time()

hach_init = [0,0,0,0,0,0]   # valeur au pif
Livre = [hach_init]
print(Livre)
ajout_transaction("Abel +135")
print(Livre)
minage()
print(Livre)
print(verification_livre())

ajout_transaction("Bob -77")
print(Livre)
minage()
print(Livre)
print(verification_livre())

ajout_transaction("Camille -25")
print(Livre)
minage()
print(Livre)
print(verification_livre())

end_time = time()
duree = end_time-start_time
print("Temps de calcul :",duree)