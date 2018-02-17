
##############################
# Binaire -partie I
##############################


##############################
# Activité 1 - Binaire vers entier
##############################

## Question 1 ##

def binaire_vers_entier_1(liste_binaire):
    nombre = 0
    i = 0
    for b in reversed(liste_binaire):
        if b == 1:
            nombre = nombre + 2**i
        i = i + 1

    return nombre

## Question 1bis ##

def binaire_vers_entier_2(liste_binaire):
    nombre = 0
    n = len(liste_binaire)
    for i in range(n):
        if liste_binaire[i] == 1:
            nombre = nombre + 2**(n-1-i)

    return nombre

## Question 2 ##

def binaire_vers_entier_3(liste_binaire):
    nombre = 0
    for b in liste_binaire:
        if b == 0:
            nombre = nombre*2
        else:
            nombre = nombre*2 + 1

    return nombre


## Question 3 ##

def liste_vers_chaine(liste_binaire):
    liste_chaine = [str(b) for b in liste_binaire]
    chaine = "".join(liste_chaine)
    chaine = "0b" + chaine  
    return chaine  

def binaire_vers_entier_4(liste_binaire):
    
    chaine = liste_vers_chaine(liste_binaire)
    nombre = int(chaine,2)

    return nombre    


# Test
liste = [1,1,0,1,1,0,0,1]
print(binaire_vers_entier_1(liste))
print(binaire_vers_entier_2(liste))
print(binaire_vers_entier_3(liste))

liste = [1,1,0,1,1,0,0,1]
print(liste_vers_chaine(liste))
print(binaire_vers_entier_4(liste))


##############################
# Activité 2 - Opérations logiques
##############################

## Question 1 ##

def OU(l1,l2):
    n = len(l1)
    l = []
    for i in range(n):
        if l1[i]==1 or l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]
    return l

def ET(l1,l2):
    n = len(l1)
    l = []
    for i in range(n):
        if l1[i]==1 and l2[i]==1:
            l = l + [1]
        else:
            l = l + [0]
    return l

def NON(l1):
    l = []
    for b in l1:
        if b==1:
            l = l + [0]
        else:
            l = l + [1]
    return l

# Test   
print("--- Opérations logiques ---")
l1 = [1,0,1,0,1,0,1]
l2 = [1,0,0,1,0,0,1]
print(l1)
print(l2)
print(OU(l1,l2))
print(ET(l1,l2))
print(NON(l1))

# Bonus : Améliorer avec des listes de tailles différentes


## Question 2 ##


def tous_les_binaires(n):
   if n == 0: 
      return []
   if n == 1: 
      return [[0],[1]]  

   liste_n_1 = tous_les_binaires(n-1)
   liste_n = [ [0] + l for l in liste_n_1] + [ [1] + l for l in liste_n_1]

   return liste_n

# Test 
print("--- Tous les binaires ---")
print(tous_les_binaires(3))



## Question 3 ##

# Lois de Morgan


def test_loi_de_morgan(n):
    liste_tous = tous_les_binaires(n)
    for l1 in liste_tous:
        for l2 in liste_tous:
            non_l1_ou_l2 = NON(OU(l1,l2))
            non_l1_et_non_l2 = ET(NON(l1),NON(l2))
            if non_l1_ou_l2 == non_l1_et_non_l2:
                print("Vrai")
            else:
                print("Faux")

    return

# Test
print("--- Test loi de Morgan ---")
test_loi_de_morgan(3)


## Question 4 ##

def enlever_zeros(liste_binaire):
    zero = True
    liste = []
    for b in liste_binaire:
        if b == 1:
            zero = False
        if not zero:
            liste = liste + [b]
    # Cas de la liste vide qui doit être [0]
    if len(liste) == 0:
        liste = [0]
    return liste

# Test 
print("--- Zeros nons significatifs ---")
print(enlever_zeros([0,0,1,0,0,1,1,0,0,0]))


def tous_les_binaires_sans_zeros(n):
    return [enlever_zeros(liste) for liste in tous_les_binaires(n)]
        
# Test 
print("--- Tous les binaires sans zéros ---")
print(tous_les_binaires_sans_zeros(4))

##############################
# Activité 3 - Palindrome en binaire
##############################

## Question 1 ##

def est_palindrome_1(liste):
    n = len(liste)

    drapeau = True
    for i in range(n):
        if liste[i] != liste[n-1-i]:
            drapeau =  False

    return drapeau


def est_palindrome_2(liste):
    liste_inverse = list(reversed(liste))
    return liste == liste_inverse

# Test 
print("--- Palindrome ---")
liste = [1,0,1,0,0,1,0,1]
print(est_palindrome_1(liste))
print(est_palindrome_2(liste))


## Question 2 ##

def tous_les_palindromes_binaires(n):
    liste_tous = tous_les_binaires_sans_zeros(n)
    liste_palindromes = []
    for l in liste_tous:
        if est_palindrome_1(l):
            liste_palindromes += [l]

    return liste_palindromes

# print("--- 1000ème palindrome ---")
# liste_palindromes = tous_les_palindromes_binaires(18)
# # print(liste_palindromes)
# # print(len(liste_palindromes))
# if len(liste_palindromes)>999:
#     print(liste_palindromes[999])
#     print(binaire_vers_entier_1(liste_palindromes[999]))


##############################
# Binaire -partie II
##############################


##############################
# Activité 1 - Ecriture décimale
##############################


## Question 1 ##

def decimale_vers_entier(liste_decimale):
    nombre = 0
    i = 0
    for d in reversed(liste_decimale):
        nombre = nombre + d*10**i
        i = i + 1

    return nombre


## Question 2 ##

def entier_vers_decimale(n):
    liste_decimale = []
    while n != 0:
        liste_decimale = [n%10] + liste_decimale
        n = n//10
    return liste_decimale


# Test
print("--- Ecriture décimale ---")
n = 1234
liste = entier_vers_decimale(n)
entier = decimale_vers_entier(liste)
print(n)
print(liste)
print(entier)


##############################
# Activité 2 - Ecriture binaire
##############################



def entier_vers_binaire(n):
    liste_binaire = []
    while n != 0:
        liste_binaire = [n%2] + liste_binaire
        n = n//2
    return liste_binaire

# Test
print("--- Ecriture binaire ---")
n = 1234
liste = entier_vers_binaire(n)
entier = binaire_vers_entier_1(liste)
print(n)
print(liste)
print(entier)


##############################
# Activité 3 - Palindrome
##############################


## Question 1 ##


def bi_palindrome(n):
    liste_binaire = entier_vers_binaire(n)
    if est_palindrome_1(liste_binaire):
        liste_decimale = entier_vers_decimale(n)
        if est_palindrome_1(liste_decimale):
            return True
    
    return False 

## Question 2 ##

# Idées chercher le 20 ème nombre palindrome à la fois en décimal et en binaire.

# Méthode 1 : en énumarant tous les entiers

def cherche_bi_palindrome(N):
    num = 0
    for n in range(N):
        if bi_palindrome(n) == True:
            num = num + 1
            print(num,":",n,"=",entier_vers_binaire(n))
            #print(entier_vers_decimale(n))
    return

# Test
cherche_bi_palindrome(1000)

## Question 3 ##
# Méthode 2 : en cherchant seulement parmi les palindromes binaires

def cherche_bi_palindrome_bis(B):
    liste_palindromes = tous_les_palindromes_binaires(B)
    num = 0
    for liste_binaire in liste_palindromes:
        n = binaire_vers_entier_1(liste_binaire)
        liste_decimale = entier_vers_decimale(n)
        if est_palindrome_1(liste_decimale):
            num = num + 1
            print(num,":",n,"=",entier_vers_binaire(n))
            #print(entier_vers_decimale(n))
    return

# Test (B = nb de bits)
cherche_bi_palindrome_bis(10)