
##############################
# Si ... alors ...
##############################

##############################
# Activité 3 - Chiffres d'un nombre
##############################


##############################
## Question 1 ##

for d in range(10):
    for u in range(10):
        n  = 10*d + u
        print(n)


##############################
## Question 2 ##

for c in range(10):
    for d in range(10):
        for u in range(10):
            n  = 100*c + 10*d + u
            if u == 3 and (c+d+u >= 15) and (d == 0 or d == 2 or d == 4 or d == 6 or d== 8):
                print(n)


##############################
## Question 3 ##

compteur = 0

for c in range(10):
    for d in range(10):
        for u in range(10):
            n  = 100*c + 10*d + u
            if u == 3 and (c+d+u >= 15) and (d == 0 or d == 2 or d == 4 or d == 6 or d== 8):
                compteur = compteur + 1

print("Nombre de solutions :",compteur)