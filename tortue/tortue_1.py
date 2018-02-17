
##############################
# Tortue
##############################

##############################
# Activité 1 - Bouge ta tortue !
##############################

# Début du code

from turtle import *

width(5)    # Epaisseur du trait

# Lettre "P"

color('red')

left(90)        # 90 degrés à gauche
forward(200)    # On avance

right(90)
forward(100)

right(90)
forward(100)

right(90)
forward(100)

up()

# Fin du code 

# Lettre "Y"

color('blue')

goto(200,0)
down()
setheading(90)
forward(120)
left(30)
forward(75)
backward(75)
right(60)
forward(75)

exitonclick()
