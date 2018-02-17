
##############################
# Si ... alors ...
##############################

##############################
# Activité 1 - Quiz multiplications
##############################

from random import *

a = randint(1,10)
b = randint(1,10)

print("Combien font",a,"fois",b,"?")
reponse_str = input("Réponse : ")
reponse_int = int(reponse_str) 

if reponse_int == a*b:
    print("Bravo !")
else:
    print("Non, la réponse était",a*b)


