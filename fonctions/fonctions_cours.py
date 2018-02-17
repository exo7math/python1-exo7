
##############################
# Fonctions
##############################



##############################
# Cours 1
##############################

##################################################
def dit_bonjour():

    print("Bonjour le monde !")

    return


# Appel
dit_bonjour()
dit_bonjour()

##################################################
def affiche_carres():

    for i in range(20):
        print(i**2)

    return

# Appel
affiche_carres()


##############################
# Cours 2
##############################

##################################################
def affiche_mois(numero):

    if numero == 1:
        print("Nous sommes en janvier.")
    if numero == 2:
        print("Nous sommes en février.")
    if numero == 3:
        print("Nous sommes en mars.")
    # etc.

    return


# Appel
affiche_mois(2)


##################################################
def calcule_cube(a):

    cube = a * a * a  # ou bien a**3

    return cube

# Appel
x = 3
y = 4
z = calcule_cube(x) + calcule_cube(y)
print(z)


##############################
# Cours 2
##############################

##################################################
def somme_produit(a,b):
    """Calcule la somme et le produit de deux nombres"""

    s = a + b
    p = a * b

    return s, p

# Appel
som, pro = somme_produit(6,7)
print(som,pro)

##############################
# Cours - Variable locale
##############################

x = 7

def plus_un(x):
    x = x + 1
    return x

def double(x):
    x = 2*x
    return x

print(x)
print(plus_un(x))
print(double(x))
print(x)




