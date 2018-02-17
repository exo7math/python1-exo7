def parentheses_correctes(expression):
    """ Teste si une expression est bien parenthésée
    Entrée : un expression (chaîne de caractère)
    Sortie : vrai/faux
    Action : utilise une pile """
    
    global pile
    pile = []    # On part d'une pile vide

    for car in expression:
        if car == "(":
            empile(car)

        if car == ")":
            if pile_est_vide():
                return False     # Problème : il manque une "(" 
            else:
                depile()

    # A la fin : 
    if pile_est_vide():
        return True
    else: 
        return False


# Test
print("--- Expression correctemment parenthésée ---")

expression = "(a+b)^2 = a^2 + (b^2+2(ab))"
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))

expression = "((a+b)^3 = (a+b)"
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))

expression = "(a+b)^4) = ((a+b)"
print("L'expression",expression,"est bien parenthésées ?",parentheses_correctes(expression))