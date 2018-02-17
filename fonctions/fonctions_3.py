
##############################
# Fonctions
##############################


##############################
# Activité 3 - Tortue
##############################

from turtle import *
width(5)    # Epaisseur du trait

##############################
## Question 1 ##

def triangle():
    color('red')
    forward(200)
    left(120)
    forward(200)
    left(120)
    forward(200)
    return


# Test
# triangle()
# exitonclick()

##############################
## Question 2 ##

def carre():
    color('green')
    for i in range(4):
        forward(200)
        left(90)
    return


# Test
# carre()
# exitonclick()


##############################
## Question 3 ##

def hexagone(longueur):
    color('blue')
    for i in range(6):
        forward(longueur)
        left(60)
    return


# Test
# hexagone(100)
# exitonclick()


##############################
## Question 4 ##

def polygone(n,longueur):
    color('purple')
    angle = 360/n
    for i in range(n):
        forward(longueur)
        left(angle)
    return


# Test
# polygone(10,70)
# exitonclick()

# Test tout
up()
goto(-450,0)
down()
triangle()
up()
goto(-200,0)
setheading(0)
down()
carre()
up()
goto(100,0)
setheading(0)
down()
hexagone(100)
up()
goto(320,0)
setheading(0)
down()
polygone(8,70)
up()
exitonclick()