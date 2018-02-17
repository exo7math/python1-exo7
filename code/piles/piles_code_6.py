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