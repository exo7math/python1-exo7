
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
# Activité 5 - Expression bien parenthésée
##############################

## Question 1 ##

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


## Question 2 ##

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

        if car == ")" or car == "]":
            if pile_est_vide():
                return False     # Problème : il manque "(" ou "[" 
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
print("L'expression",expression,"est bien parenthésées et crochetées ?",crochets_parentheses_correctes(expression))

expression = "((a+b)]^3 = [a+b]"
print("L'expression",expression,"est bien parenthésées et crochetées ?",crochets_parentheses_correctes(expression))

expression = "[a+b)^4] = (a+b)"
print("L'expression",expression,"est bien parenthésées et crochetées ?",crochets_parentheses_correctes(expression))

