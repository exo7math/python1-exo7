
##############################
# Tortue
##############################

##############################
# Activité 2 - Boucle "pour"
##############################

##############################
# Question 1

from turtle import *

# Un pentagone
width(5)
color('blue')

for i in range(5):
    forward(100)
    left(72)


##############################
# Question 2

# Un autre pentagone
color('red')

longueur = 200
angle = 72
for i in range(5):
    forward(longueur)
    left(angle)


##############################
# Question 3

# Un dodecagone (12 côtés quoi)

color("purple")
n = 12
angle = 360/n
for i in range(n):
    forward(100)
    left(angle)


##############################
# Question 4

# Une spirale

color("green")
longueur = 10
for i in range(25):
    forward(longueur)
    left(40)
    longueur = longueur + 10

exitonclick()


