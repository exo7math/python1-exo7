
##############################
# Tortue
##############################

##############################
# Activité 4 - Plusieurs tortues - Courbe de poursuite
##############################

# Préparation

from turtle import *

tortue1 = Turtle()
tortue2 = Turtle()
tortue3 = Turtle()
tortue4 = Turtle()

tortue1.speed("fastest")
tortue2.speed("fastest")
tortue3.speed("fastest")
tortue4.speed("fastest")

tortue1.color('red')
tortue2.color('blue')
tortue3.color('orange')
tortue4.color('green')

# tortue1.width(5)
# tortue2.width(5)
# tortue3.width(5)
# tortue4.width(5)

tortue1.up()
tortue1.goto(-200,-200)
tortue1.down()

tortue2.up()
tortue2.goto(200,-200)
tortue2.down()

tortue3.up()
tortue3.goto(200,200)
tortue3.down()

tortue4.up()
tortue4.goto(-200,200)
tortue4.down()

print(tortue1.position())
print(tortue1.towards(0,0))


# Boucle principale

for i in range(40):

    position1 = tortue1.position()
    position2 = tortue2.position()
    position3 = tortue3.position()
    position4 = tortue4.position()

    tortue1.goto(position2)  # Va à la tortue suivante
    tortue1.goto(position1)       # Revient à sa place

    tortue2.goto(position3)
    tortue2.goto(position2)

    tortue3.goto(position4)
    tortue3.goto(position3)

    tortue4.goto(position1)
    tortue4.goto(position4)

    angle1 = tortue1.towards(position2)  # Récupèrer l'angle
    tortue1.setheading(angle1)   # S'oriente selon cet angle

    angle2 = tortue2.towards(position3)
    tortue2.setheading(angle2)

    angle3 = tortue3.towards(position4)
    tortue3.setheading(angle3)

    angle4 = tortue4.towards(position1)
    tortue4.setheading(angle4)

    tortue1.forward(10)    # Avance
    tortue2.forward(10)
    tortue3.forward(10)
    tortue4.forward(10)

exitonclick()



