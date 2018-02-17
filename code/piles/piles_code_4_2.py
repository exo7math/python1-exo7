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