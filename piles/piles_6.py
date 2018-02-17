
##############################
# Piles - Calculatrice polonaise
##############################

global pile

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
# Rappels - Activité 4
##############################

def operation(a,b,op):  
    if op == '+':
        return a + b
    if op == '*':
        return a * b

def calculatrice_polonaise(expression):  
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


##############################
# Activité 6 - Conversion vers l'écriture polonaise
##############################

def ecriture_polonaise(expression):
    """ Convertit une expression classique en notation polonaise
    Entrée : une expression classique
    Sortie : l'expression en notation polonaise
    Action : utilise une pile """
    
    global pile
    pile = []

    liste_expression = expression.split()

    polonaise = ""    # L'écriture polonaise

    for car in liste_expression:
        if car.isdigit():
            polonaise = polonaise + car + " "

        if car == "(":
            empile(car)

        if car == "*":
            empile(car)

        if car == "+":
            while not pile_est_vide():
                element = depile()                
                if element == "*":
                    polonaise = polonaise + element + " "            
                else:
                    empile(element)    # Remettre l'élément
                    break
            empile(car)            

        if car == ")":
            while not pile_est_vide():
                element = depile()                
                if element == "(":
                    break
                else:
                    polonaise = polonaise + element + " "

    while not pile_est_vide():
        element = depile()                
        polonaise = polonaise + element + " "    

    return polonaise

# Tests
print("--- Conversion en écriture polonaise ---")

exp = "2 + 3"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "2 * 3"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "( 2 + 3 ) * 4"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "4 * ( 2 + 3 )"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "2 + 4 * 5"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "2 * 4 * 5"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))

exp = "( 2 + 3 ) * ( 4 + 8 )"
print("l'expression",exp,"s'écrit",ecriture_polonaise(exp))


##
# Automatisation des tests et des vérifications

def test_polonaise(expression):
    classique = eval(expression)
    print("---\n",classique)
    conversion = ecriture_polonaise(expression)
    print(conversion)
    polonaise = calculatrice_polonaise(conversion)
    print(polonaise)
    return classique == polonaise


exp = "2 + 3"
print(exp, "OK ?",test_polonaise(exp))

exp = "2 * 3 * 7"
print(exp, "OK ?",test_polonaise(exp))
 
exp = "( 2 + 3 ) * ( 4 + 8 )"
print(exp, "OK ?",test_polonaise(exp))

exp = "( ( 2 + 3 ) * 11 ) * ( 4 + ( 8 + 5 ) )"
print(exp, "OK ?",test_polonaise(exp))

exp = "( 17 * ( 2 + 3 ) ) + ( 4 + ( 8 * 5 ) )"
print(exp, "OK ?",test_polonaise(exp))