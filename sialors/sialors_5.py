
##############################
# Si ... alors ...
##############################

##############################
# Activité 4 - Le jeu de la devinette
##############################


##############################
## Question 1 ##

from random import *

# Jeu classique de la devinette

nb_mystere = randint(0,99)

for essai in range(7):
    print("Quel est le nombre mystère ?")
    reponse_str = input("Ta proposition : ")
    reponse_int = int(reponse_str) 
    if nb_mystere == reponse_int:
        print("Bravo !")
        break   # Arrête la boucle
    
    if nb_mystere < reponse_int:
        print("Non, le nombre à trouver est plus petit !")    
    
    if nb_mystere > reponse_int:
        print("Non, le nombre à trouver est plus grand !")

# Lorsque c'est fini :
if nb_mystere != reponse_int:
    print("Perdu ! Le nombre mystère était",nb_mystere)


##############################
## Question 2 ##

# Variante : l'ordinateur ment (1 fois sur 4)

# nb_mystere = randint(0,99)

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
#
#     if nb_mystere < reponse_int:
#         if verite == True:
#             print("Non, le nombre à trouver est plus petit !")    
#         else:
#             print("Non, le nombre à trouver est plus grand !") 
#   
#     if nb_mystere > reponse_int:
#         if verite == True:
#             print("Non, le nombre à trouver est plus grand !")
#         else: 
#             print("Non, le nombre à trouver est plus petit !")

# # Lorsque c'est fini :
# if nb_mystere != reponse_int:
#     print("Perdu ! Le nombre mystère était",nb_mystere)


##############################
## Question 3 ##

# Variante : le nombre mystère change un peu

# nb_mystere = randint(0,99)

# for essai in range(7):
#     print("Quel est le nombre mystère ?")
#     reponse_str = input("Ta proposition : ")
#     reponse_int = int(reponse_str) 

#     # Modification du nb mystère
#     hasard = randint(-3,3)
#     nb_mystere = nb_mystere + hasard
#     if nb_mystere < 1:
#         nb_mystere = 1
#     if nb_mystere > 99:
#         nb_mystere = 99

#     if nb_mystere == reponse_int:
#         print("Bravo !")
#         break   # Arrête la boucle
#     if nb_mystere < reponse_int:
#         print("Non, le nombre à trouver est plus petit !")    
#     if nb_mystere > reponse_int:
#         print("Non, le nombre à trouver est plus grand !")

# # Lorsque c'est fini :
# if nb_mystere != reponse_int:
#     print("Perdu ! Le nombre mystère était",nb_mystere)

