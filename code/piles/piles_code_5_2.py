def crochets_parentheses_correctes(expression):
    """ Teste si une expression a des crochets et des parenthèses bien placées
    Entrée : un expression (chaîne de caractère)
    Sortie : vrai/faux
    Action : utilise une pile """
    
    global pile
    pile = []    # On part d'une pile vide

    for car in expression:
        if car == "(" or car == "[":
            empile(car)

        if car == ")" or "]":
            if pile_est_vide():
                return False     # Problème : il manque une "(" 
            else:
                element = depile()
                if element == "[" and car == ")":
                    return False     # Problème du type [)
                if element == "(" and car == "]":
                    return False     # Problème du type (]

    # A la fin
    return pile_est_vide()


# Test
print("--- Expression avec crochets et parenthèses corrects ---")

expression = "(a+b)^2 = (a^2 + [b^2+[2(ab)]])"
print("L'expression",expression,"est bien parenthésées et crochetées ?",parentheses_correctes(expression))

expression = "((a+b)]^3 = [a+b]"
print("L'expression",expression,"est bien parenthésées et crochetées ?",parentheses_correctes(expression))

expression = "[a+b)^4] = (a+b)"
print("L'expression",expression,"est bien parenthésées et crochetées ?",parentheses_correctes(expression))