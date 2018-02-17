
##############################
# Tortue
##############################


##############################
# Activité 3 - Graphe d'une fonction
##############################


from turtle import *
from math import *

speed("fastest")
width(2)
color('blue')
up()

for x in range(-200,200):
    if x == -199: down()
    # y = 1/ 100 * x ** 2   # Parabole
    y = 100*sin(1/20*x)     # Sinus
    goto(x,y)


exitonclick()

