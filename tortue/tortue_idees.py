
##############################
# Tortue
##############################



from turtle import *

from math import *

goto(0,0)
forward(472)
left(90)
forward(400)

##############################
# Activité 1 - 
##############################

def activite_1():
    # reset()
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    right(45)
    backward(20)

    up()
    color('red')
    width(5)
    goto(-100,0)
    down()

    forward(100)

    #done()
    exitonclick()

# activite_1()

##############################
# Activité 2 - Boucle pour
##############################

def activite_2():
    # reset()

    width(5)
    color('blue')

    for i in range(5):
        forward(100)
        left(72)

    color('red')

    longueur = 200
    angle = 72
    for i in range(5):
        forward(longueur)
        left(angle)

    color('green')

    longueur = 300
    angle = 72
    for i in range(5):
        forward(longueur)
        left(angle)


    color("purple")
    n = 12
    angle = 360/n
    for i in range(n):
        forward(100)
        left(angle)


    exitonclick()


# activite_2()


##############################
# Activité 3 - Boucle pour itérée Triangle de Sierpinski
##############################



def activite_3():
    # reset()

    width(5)
    up()
    goto(-100,-100)
    down()

    for i in range(3):
        color("blue")
        forward(256)
        left(120)


        for i in range(3):
            color("red")
            forward(128)
            left(120)

            for i in range(3):
                color("green")
                forward(64)
                left(120)  


                for i in range(3):
                    color("orange")
                    forward(32)
                    left(120)                            

    exitonclick()

# activite_3()


##############################
# Activité  - Graphe d'une fonction
##############################

def activite_7():
    speed("fastest")

    for i in range(-200,200):
        x = i
        y = 1/ 100 * x ** 2
        y = 100*sin(0.1*x) 
        goto(x,y)


    exitonclick()

activite_7()






##############################
# Activité 5 - Table de multiplication
##############################



def activite_5():

    speed("fastest")

    n = 100
    b = 2
    R = 200

    for i in range(n):
        up()
        goto(R*cos(2*i*pi/n),R*sin(2*i*pi/n))
        down()
        j = (b*i) % n
        goto(R*cos(2*j*pi/n),R*sin(2*j*pi/n))


    exitonclick()


# activite_5()



##############################
# Activité 4 - Plusieurs tortue - Courbe de poursuite
##############################


    # tortue1 = Turtle()
    # tortue2 = Turtle()

    # tortue1.color('red')
    # tortue2.color('blue')

    # tortue1.forward(100)
    # tortue2.left(90)
    # tortue2.forward(100)

def activite_4():

    tortue1 = Turtle()
    tortue2 = Turtle()
    tortue3 = Turtle()
    tortue4 = Turtle()

    tortue1.speed("fastest")
    tortue2.speed("fastest")
    tortue3.speed("fastest")
    tortue4.speed("fastest")

    tortue3.color('yellow')
    tortue4.color('green')

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



    for i in range(40):


        position1 = tortue1.position()
        position2 = tortue2.position()
        position3 = tortue3.position()
        position4 = tortue4.position()

        tortue1.goto(position2)  # Va à la tortue suivante
        tortue1.goto(position1)  # Revient à sa place

        tortue2.goto(position3)
        tortue2.goto(position2)

        tortue3.goto(position4)
        tortue3.goto(position3)

        tortue4.goto(position1)
        tortue4.goto(position4)


        angle1 = tortue1.towards(position2)  # Récupèrer l'angle
        tortue1.setheading(angle1)  # S'oriente selon cet angle

        angle2 = tortue2.towards(position3)
        tortue2.setheading(angle2)

        angle3 = tortue3.towards(position4)
        tortue3.setheading(angle3)

        angle4 = tortue4.towards(position1)
        tortue4.setheading(angle4)

        tortue1.forward(10)   # Avance
        tortue2.forward(10)
        tortue3.forward(10)
        tortue4.forward(10)




    exitonclick()


# activite_4()


