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