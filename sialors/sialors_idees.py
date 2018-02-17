
##############################
# Si ... alors ... - Idées
##############################

from random import *

##############################
# Activité 1 - 
##############################

##############################
# a = randint(1,10)
# b = randint(1,10)
# print("Combien font",a,"fois",b,"?")
# reponse_str = input("Réponse : ")
# reponse_int = int(reponse_str) 
# if reponse_int == a*b:
#     print("Bravo !")
# else:
#     print("Non, la réponse était",a*b)


# exit()


##############################
# Activité 2 - Tortue
##############################

# from turtle import *

# mot = "AagAgAdAgaAgaAA"


# width(2)
# color('blue')

# for c in mot:

#     if c == "A":
#         forward(100)

#     if c == "a":
#         up()
#         forward(100)
#         down()   

#     if c == "g":
#         left(90)

#     if c == "d":
#         right(90) 

# exitonclick()

##############################
# Activité 3 - Chiffres d'un nombre
##############################

##############################
for d in range(10):
    for u in range(10):
        n  = 10*d + u
        print(n)

##############################
for c in range(10):
    for d in range(10):
        for u in range(10):
            n  = 100*c + 10*d + u
            if u == 3 and (c+d+u >= 15) and (d == 0 or d == 2 or d == 4 or d == 6 or d== 8):
                print(n)


##############################
# Activité 4 - Le jeu de la devinette
##############################

# nb_mystere = randint(1,100)

# for essai in range(7):
#     print("Quel est le nombre mystère ?")
#     reponse_str = input("Ta proposition : ")
#     reponse_int = int(reponse_str) 
#     if nb_mystere == reponse_int:
#         print("Bravo !")
#         break   # Arrête la boucle
#     elif nb_mystere < reponse_int:
#         print("Non, le nombre à trouver est plus petit !")    
#     elif nb_mystere > reponse_int:
#         print("Non, le nombre à trouver est plus grand !")

# # Lorsque c'est fini :
# if nb_mystere != reponse_int:
#     print("Perdu ! Le nombre mystère était",nb_mystere)


##############################
# Variante 1 : l'ordinateur ment (1 fois sur 4)

# nb_mystere = randint(1,100)

# for essai in range(7):
#     print("Quel est le nombre mystère ?")
#     reponse_str = input("Ta proposition : ")
#     reponse_int = int(reponse_str) 

#     # 1 fois sur 4 (environ) l'ordinateur ment
#     verite = True
#     hasard = randint(1,4)
#     if hasard == 4:
#         verite = False 

#     if nb_mystere == reponse_int:
#         print("Bravo !")
#         break   # Arrête la boucle
#     elif nb_mystere < reponse_int:
#         if verite == True:
#             print("Non, le nombre à trouver est plus petit !")    
#         else:
#             print("Non, le nombre à trouver est plus grand !")    
#     elif nb_mystere > reponse_int:
#         if verite == True:
#             print("Non, le nombre à trouver est plus grand !")
#         else: 
#             print("Non, le nombre à trouver est plus petit !")

# # Lorsque c'est fini :
# if nb_mystere != reponse_int:
#     print("Perdu ! Le nombre mystère était",nb_mystere)



##############################
# Variante 2 : le nombre mystère change

nb_mystere = randint(1,100)

for essai in range(7):
    print("Quel est le nombre mystère ?")
    reponse_str = input("Ta proposition : ")
    reponse_int = int(reponse_str) 

    # Modification du nb mystère
    hasard = randint(-3,3)
    nb_mystere = nb_mystere + hasard
    if nb_mystere < 1:
        nb_mystere = 1
    if nb_mystere > 100:
        nb_mystere = 100

    if nb_mystere == reponse_int:
        print("Bravo !")
        break   # Arrête la boucle
    elif nb_mystere < reponse_int:
        print("Non, le nombre à trouver est plus petit !")    
    elif nb_mystere > reponse_int:
        print("Non, le nombre à trouver est plus grand !")

# Lorsque c'est fini :
if nb_mystere != reponse_int:
    print("Perdu ! Le nombre mystère était",nb_mystere)


##############################
# Activité 4 - Triangles
##############################