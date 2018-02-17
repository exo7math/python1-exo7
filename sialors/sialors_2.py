
##############################
# Si ... alors ...
##############################

##############################
# Activité 2 - Tortue
##############################

from turtle import *

width(5)
color('blue')

mot = "AagAgAdAgAAgaAA"

for c in mot:

    if c == "A":
        forward(100)

    if c == "a":
        up()
        forward(100)
        down()   

    if c == "g":
        left(90)

    if c == "d":
        right(90) 

exitonclick()
