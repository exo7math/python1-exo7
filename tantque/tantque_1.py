
##############################
# Tant que - Booléen - Arithmétiques
##############################


##############################
# Activité 1 - Divisibilité, quotient, reste
##############################


##############################
## Question 1 ##

def quotient_reste(a,b):
    """ Affiche le quotient et le reste et vérifie
    la validité de la division euclidienne """

    q = a // b
    r = a % b
    print("Division de a =",a,"par b =",b)
    print("Le quotient vaut q =",q)
    print("Le reste vaut r =",r)

    if (r >=0) and (r < b):
        verif_reste = True
    else:
        verif_reste = False
    print("Vérification reste 0 <= r < b ?",verif_reste)

    if a == b*q +r:
        verif_egal = True
    else:
        verif_egal = False
    print("Vérification égalité a = bq + r ?",verif_egal)

    return q,r


# Test
print("--- Quotient et reste ---")
quotient_reste(100,7)


##############################
## Question 2 ##

def est_pair(n):
    """ Teste si l'entier n est pair ou pas (renvoie vrai ou faux) """
    reste = n % 2
    if reste == 0:
        return True
    else:
        return False


def est_pair_bis(n):
    """ Teste si l'entier n est pair ou pas (renvoie vrai ou faux) """
    chiffre = n % 10
    if (chiffre==0) or (chiffre==2) or (chiffre==4) or (chiffre==6) or (chiffre==8):
        return True
    else:
        return False


# En deux lignes !
def est_pair_ter(n):
    return (n % 2) == 0


# Test
print("--- Parité  ---")
print(est_pair(1023))


##############################
## Question 3 ##

def est_divisible(a,b):
    """ Teste si a est divisible par b """    
    if a % b == 0:
        return True
    else:
        return False


# Test
print("--- Divisibilité  ---")
print(est_divisible(125,5))

