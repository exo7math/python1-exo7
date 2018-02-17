
##############################
# Listes II 
##############################


##############################
# Activité 1 - Manipulation de listes
##############################


## Question 1 ##

##############################
def multiplier(liste,k):
    return [k*x for x in liste]


## Question 2 ##

##############################
def puissance(liste,k):
    return [x**k for x in liste]


## Question 3 ##

##############################
def addition(liste1,liste2):
    liste_add = []
    for i in range(len(liste1)):
        liste_add.append(liste1[i]+liste2[i])
    return liste_add


## Question 4 ##

##############################
def non_zero(liste):
    return [x for x in liste if x != 0]


## Question 5 ##

##############################
def pairs(liste):
    return [x for x in liste if x % 2 == 0]


# Test
print("--- Multiplier ---")
print(multiplier([1,2,3,4,5],2))
print("--- Puissance ---")
print(puissance([1,2,3,4,5],3))
print("--- Addition ---")
print(addition([1,2,3],[4,5,6]))
print("--- Sans zéro ---")
print(non_zero([1,0,2,3,0,4,5,0]))
print("--- Pairs ---")
print(pairs([1,0,2,3,0,4,5,0]))


