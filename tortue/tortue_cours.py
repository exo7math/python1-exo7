
##############################
# Tortue
##############################

##############################
# Cours - Tortue
##############################

from turtle import *

forward(100)   # On avance
left(90)       # 90 degrés à gauche
forward(50)
width(5)       # Epaisseur du trait
forward(100)
color('red')
right(90)
forward(200)

exitonclick()

#################
# Cours - Plusieurs tortues
#################

tortue1 = Turtle()   # Avec un 'T' majuscule !
tortue2 = Turtle()

tortue1.color('red')
tortue2.color('blue')

tortue1.forward(100)
tortue2.left(90)
tortue2.forward(100)