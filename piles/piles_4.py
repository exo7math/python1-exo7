
##############################
# Piles - Calculatrice polonaise
##############################

##############################
# Rappels - Activité 1
##############################

def empile(element):
    global pile
    pile = pile + [element]
    return None

def depile():
    global pile
    sommet = pile[len(pile)-1]
    pile = pile[0:len(pile)-1]
    return sommet   

def pile_est_vide():
    if len(pile) == 0:
        return True
    else:
        return False


##############################
# Activité 4 - Calculatrice polonaise
##############################

## Question 1 ##

def operation(a,b,op):
    """ Calcule l'opération 'a + b 'ou 'a * b'...
    Entrée : a,b (nombres) et 'op' un ccaractère '+'' ou '*'
    Sortie : le résultat du calcul """
    
    if op == '+':
        return a + b
    if op == '*':
        return a * b


# Tests
print("--- Opérations ---")
a=5 ; b=7
print("La somme de",a,"et",b,"vaut",operation(a,b,'+'))
print("Le produit de",a,"et",b,"vaut",operation(a,b,'*'))


## Question 2 ##

def calculatrice_polonaise(expression):
    """ Calcule l'expression codée en notation polonaise
    Entrée : une expression en notation polonaise
    Sortie : le résultat du calcul
    Action : utilise la pile """
    
    global pile
    pile = []

    liste_expression = expression.split()

    for car in liste_expression:
        if (car == '+') or (car == '*'):
            b = depile()
            a = depile()
            calcul_partiel = operation(a,b,car)
            empile(calcul_partiel)
        else:
            val = int(car)
            empile(val)

    return depile()


# Tests
print("--- Calculatrice polonaise ---")

exp = "2 3 +"
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))

exp = "2 3 + 5 *"
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))

exp = "8 7 3 + *"
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))

exp = "8 7 3 * +"
print("L'expression",exp,"vaut",calculatrice_polonaise(exp))